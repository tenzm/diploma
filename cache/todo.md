# Анализ кэшей для storage-agent и storage-mounter

## Текущий этап proxy-слоя

`storage-agent` выполняет роль proxy/gateway между `storage-mounter` и удалёнными реестрами моделей.
Сервис `storage-gateway` реализует приоритетную цепочку чтения:

```
storage-mounter → HTTP/UDS → storage-agent (mounter-bff) → storage-gateway
    → [L1] inMemoryChunkCache (SLRU)
    → [L2] localstorage disk (атомарные файлы)
    → [L3] external registry (HuggingFace, Ollama)
```

`storage-mounter` со своей стороны имеет:
- streaming ring-buffer (chunkId % capacity) как клиентский кэш
- prefetcher с look-ahead (асинхронные горутины)
- singleflight для дедупликации одновременных запросов
- sync.Pool для переиспользования байтовых буферов

---

## Список 1: Кэши для storage-agent (персистентное хранилище на диске)

### 1. Файловый кэш с иерархией директорий *(текущая реализация)*

**Описание.** Каждый чанк хранится как отдельный файл по пути
`<cache_dir>/<registry>/<repo>/<model>/<revision>/<hash[:2]>/<hash[2:4]>/<hash>/chunk_<N>`.
Запись атомарна через временный файл + `os.Rename`.

**Псевдокод (Go):**
```go
func (r *Repository) write(ctx context.Context, path string, chunk *Chunk) error {
    dir := filepath.Dir(path)
    os.MkdirAll(dir, 0755)

    tmp, _ := os.CreateTemp(dir, ".chunk-*")
    io.Copy(tmp, chunk.Reader())
    tmp.Sync()
    tmp.Close()

    return os.Rename(tmp.Name(), path) // атомарная операция
}
```

**Плюсы:** прост, поддерживает OS page cache, атомарная запись исключает частичное чтение.  
**Минусы:** нет структурированного индекса для LRU-вытеснения; вытеснение требует обхода файловой системы по времени последнего доступа (`atime`).

---

### 2. SLRU in-memory (Segmented LRU) *(текущая реализация, L1-уровень)*

**Описание.** Двусвязный список + два map (ключ → элемент, ключ → данные). Вытеснение с хвоста.
Ёмкость задаётся в байтах; при превышении вытесняются наименее недавно использованные чанки.

**Псевдокод (Go):**
```go
type slruCache struct {
    mu       sync.Mutex
    list     *list.List
    dataMap  map[cacheKey]*Chunk
    elemMap  map[cacheKey]*list.Element
    capacity uint64 // байты
    current  uint64
}

func (c *slruCache) Get(ref ModelRef, chunkId uint64) (*Chunk, bool) {
    c.mu.Lock()
    defer c.mu.Unlock()
    elem, ok := c.elemMap[cacheKey{ref, chunkId}]
    if !ok { return nil, false }
    c.list.MoveToFront(elem)
    return c.dataMap[cacheKey{ref, chunkId}], true
}

func (c *slruCache) Set(chunk *Chunk) {
    c.mu.Lock()
    defer c.mu.Unlock()
    size := uint64(cap(chunk.Data()))
    for c.current+size > c.capacity {
        c.evictTail()
    }
    elem := c.list.PushFront(cacheKey{chunk.Ref, chunk.Id})
    c.dataMap[cacheKey{chunk.Ref, chunk.Id}] = chunk
    c.elemMap[cacheKey{chunk.Ref, chunk.Id}] = elem
    c.current += size
}
```

**Плюсы:** O(1) get/evict; обслуживает горячие чанки без обращения к диску.  
**Минусы:** полностью теряется при перезапуске агента; размер ограничен RAM.

---

### 3. Файловый кэш + SQLite-индекс метаданных *(рекомендуется как расширение)*

**Описание.** Данные чанков хранятся на диске (как в п.1). SQLite хранит метаданные для LRU:
`(model_ref, chunk_id, size_bytes, last_access_unix)`. При вытеснении агент выбирает N
наименее давно использованных чанков из SQLite, удаляет файлы, удаляет строки.
Код в `localstorage/repository.go` уже содержит комментарий с предполагаемой схемой.

**Псевдокод (Go):**
```go
// CREATE TABLE chunks (
//   model_ref TEXT NOT NULL,
//   chunk_id  INTEGER NOT NULL,
//   size_bytes INTEGER NOT NULL,
//   last_access_unix INTEGER NOT NULL,
//   created_at_unix  INTEGER NOT NULL,
//   PRIMARY KEY (model_ref, chunk_id)
// );

func (r *Repository) TouchChunk(ctx context.Context, ref *ModelRef, chunkId uint64) error {
    _, err := r.db.ExecContext(ctx,
        `UPDATE chunks SET last_access_unix=? WHERE model_ref=? AND chunk_id=?`,
        time.Now().Unix(), ref.String(), chunkId)
    return err
}

func (r *Repository) EvictLRU(ctx context.Context, bytesToFree int64) error {
    rows, _ := r.db.QueryContext(ctx,
        `SELECT model_ref, chunk_id, size_bytes FROM chunks
         ORDER BY last_access_unix ASC LIMIT 200`)
    defer rows.Close()
    freed := int64(0)
    for rows.Next() && freed < bytesToFree {
        var ref string; var chunkId uint64; var size int64
        rows.Scan(&ref, &chunkId, &size)
        path := r.chunkPath(ref, chunkId)
        os.Remove(path)
        r.db.ExecContext(ctx,
            `DELETE FROM chunks WHERE model_ref=? AND chunk_id=?`, ref, chunkId)
        freed += size
    }
    return nil
}
```

**Плюсы:** структурированное вытеснение; порядок LRU сохраняется между перезапусками; совместим с текущей файловой структурой без изменения формата хранения.  
**Минусы:** SQLite создаёт write lock при каждом `TouchChunk`; при высокой нагрузке на запись (большой параллелизм) может стать узким местом. Решение: использовать WAL-mode SQLite или выполнять `TouchChunk` асинхронно через отдельный канал.

---

### 4. ARC (Adaptive Replacement Cache) для in-memory уровня *(альтернатива SLRU)*

**Описание.** ARC поддерживает четыре списка: T1 (recently inserted, one hit), T2 (frequently used),
B1 и B2 (ghost: evicted from T1/T2 без данных). Адаптивно сдвигает границу p между T1 и T2
при попаданиях в ghost-списки, балансируя между recency (LRU) и frequency (LFU).

**Псевдокод (Go):**
```go
type ARC struct {
    mu       sync.Mutex
    c        int // target size (байты)
    p        int // adaptive split: target size of T1
    t1, t2   *lruList // with data
    b1, b2   *lruList // ghost (keys only, no data)
}

func (a *ARC) Get(key cacheKey) (*Chunk, bool) {
    a.mu.Lock()
    defer a.mu.Unlock()
    if ch := a.t1.remove(key); ch != nil {
        a.t2.addFront(key, ch) // promote to frequent
        return ch, true
    }
    if ch := a.t2.get(key); ch != nil {
        a.t2.moveToFront(key) // already frequent
        return ch, true
    }
    return nil, false
}

func (a *ARC) Set(key cacheKey, chunk *Chunk) {
    a.mu.Lock()
    defer a.mu.Unlock()
    switch {
    case a.b1.contains(key):
        a.p = min(a.c, a.p + max(1, len(a.b2)/len(a.b1))) // hit in b1: recency was useful
        a.replace(key)
        a.b1.remove(key)
        a.t2.addFront(key, chunk)
    case a.b2.contains(key):
        a.p = max(0, a.p - max(1, len(a.b1)/len(a.b2))) // hit in b2: frequency was useful
        a.replace(key)
        a.b2.remove(key)
        a.t2.addFront(key, chunk)
    default:
        a.replace(key)
        a.t1.addFront(key, chunk)
    }
}
```

**Плюсы:** автоматически адаптируется к рабочей нагрузке; превосходит LRU при смешанном паттерне (горячие модели + разовые сканирования); не нужно вручную настраивать split-ratio.  
**Минусы:** сложнее в реализации и отладке; ghost-списки занимают дополнительную память (без данных, только ключи).

---

### 5. Write-behind async queue *(текущая реализация, сохранить)*

**Описание.** Запись чанка на диск асинхронна: `Repository.Write()` кладёт чанк в канал `writeCh`,
отдельная горутина-worker читает из канала и выполняет физическую запись.

**Псевдокод (Go):**
```go
func (r *Repository) Write(ctx context.Context, chunk *Chunk) error {
    select {
    case r.writeCh <- chunk:
        return nil
    case <-ctx.Done():
        return ctx.Err()
    default:
        return ErrQueueFull
    }
}

func (r *Repository) runWorker(ctx context.Context) {
    for {
        select {
        case chunk := <-r.writeCh:
            path, _ := r.chunkPath(chunk)
            r.write(ctx, path, chunk) // атомарный write через temp+rename
        case <-ctx.Done():
            return
        }
    }
}
```

**Плюсы:** Write() не блокирует путь чтения; запись дисковых чанков не влияет на latency ответа клиенту.  
**Минусы:** при падении процесса незаписанные чанки в очереди теряются. Это допустимо: при следующем запросе того же чанка агент перезагрузит его из internal registry (или пира).

---

## Список 2: Кэши для storage-mounter (буферизация при чтении через UDS)

### 1. Ring buffer / Circular buffer *(текущая реализация)*

**Описание.** Кольцевой буфер фиксированной ёмкости. Индекс в массиве вычисляется как
`chunkId % capacity`. При записи нового чанка возможно вытеснение старого чанка с тем же
индексом (collision eviction). Верификация попадания: `chunk != nil && chunk.Id == chunkId`.

**Псевдокод (Go):**
```go
type RingCache struct {
    mu       sync.RWMutex
    capacity uint64
    data     []*Chunk
}

func (c *RingCache) Get(ctx context.Context, chunkId uint64) (*Chunk, error) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    idx := chunkId % c.capacity
    ch := c.data[idx]
    if ch != nil && ch.Id == chunkId {
        return ch, nil // hit
    }
    return nil, nil // miss (slot empty or collision)
}

func (c *RingCache) Set(ctx context.Context, chunk *Chunk) (bool, error) {
    idx := chunk.Id % uint64(c.capacity)
    c.mu.Lock()
    defer c.mu.Unlock()
    evicted := c.data[idx] != nil
    c.data[idx] = chunk
    return evicted, nil
}
```

**Плюсы:** O(1) без lock-contention под RWMutex; минимальная память; идеален для последовательного чтения одного файла.  
**Минусы:** при одновременном открытии нескольких файлов модели (шарды .safetensors) чанки разных файлов с одинаковым номером коллидируют и вытесняют друг друга.

---

### 2. Prefetch window (look-ahead) *(текущая реализация, сохранить)*

**Описание.** При каждом `Read(chunkId)` prefetcher асинхронно запускает горутины для
`prefetchAhead - 1` следующих чанков. Если следующий чанк уже в кэше — горутина не запускается.

**Псевдокод (Go):**
```go
func (p *Prefetcher) Read(ctx context.Context, meta *FileMetadata, ref *ModelRef, chunkId uint64) (*Chunk, error) {
    // Асинхронная предзагрузка следующих N чанков
    for i := 1; i < p.prefetchAhead; i++ {
        ahead := chunkId + uint64(i)
        if cached, _ := p.cache.Get(ctx, ahead); cached == nil || cached.Id != ahead {
            go p.fetchOne(ctx, meta, ref, ahead)
        }
    }
    // Синхронное чтение текущего чанка
    return p.fetchOne(ctx, meta, ref, chunkId)
}

func (p *Prefetcher) fetchOne(ctx context.Context, meta *FileMetadata, ref *ModelRef, chunkId uint64) (*Chunk, error) {
    // singleflight: только одна горутина загружает один chunkId
    key := fmt.Sprintf("%v/%d", ref, chunkId)
    result, err, _ := p.sf.Do(key, func() (any, error) {
        buf := p.pool.Get(int(meta.ChunkSize))
        chunk, _ := meta.NewChunk(chunkId, buf)
        p.cache.Set(ctx, chunk)
        return chunk, p.chunkReader.Read(ctx, chunk)
    })
    return result.(*Chunk), err
}
```

**Плюсы:** скрывает latency сетевого/дискового чтения за временем обработки GPU текущего чанка.  
**Минусы:** при нелинейном паттерне чтения (random seek) prefetch тратит пропускную способность впустую.

---

### 3. sync.Pool byte buffer pool *(текущая реализация, сохранить)*

**Описание.** Мультиразмерный пул байтовых буферов. Для каждого уникального размера чанка
хранится отдельный `sync.Pool`. Это исключает аллокации `make([]byte, chunkSize)` при каждом
запросе, что критично при высоком параллелизме (сотни горутин FUSE).

**Псевдокод (Go):**
```go
type MultiPool struct {
    mu    sync.RWMutex
    pools map[int]*sync.Pool
}

func (p *MultiPool) Get(size int) []byte {
    p.mu.RLock()
    pl, ok := p.pools[size]
    p.mu.RUnlock()
    if !ok {
        p.mu.Lock()
        pl = &sync.Pool{New: func() any {
            buf := make([]byte, size)
            return &buf
        }}
        p.pools[size] = pl
        p.mu.Unlock()
    }
    return *pl.Get().(*[]byte)
}

func (p *MultiPool) Put(buf []byte) {
    size := cap(buf)
    p.mu.RLock()
    pl, ok := p.pools[size]
    p.mu.RUnlock()
    if ok {
        pl.Put(&buf)
    }
}
```

**Плюсы:** снижает давление на GC; при chunk_size = 32 МБ и 100 параллельных читателях экономит 3.2 ГБ аллокаций за одну волну запросов.  
**Минусы:** пулы для разных размеров не взаимозаменяемы; если chunk_size меняется между моделями, пул накапливает буферы разных размеров.

---

### 4. Per-file LRU cache *(рекомендуется для multi-file сценариев)*

**Описание.** При одновременном чтении нескольких файлов (.safetensors шарды) кольцевой буфер
даёт коллизии. Per-file LRU хранит отдельный LRU-кэш для каждого открытого файла.

**Псевдокод (Go):**
```go
type PerFileLRU struct {
    mu         sync.RWMutex
    caches     map[string]*chunkLRU // filepath → LRU кэш
    maxPerFile int                   // лимит чанков на файл
}

func (p *PerFileLRU) Get(filepath string, chunkId uint64) (*Chunk, bool) {
    p.mu.RLock()
    c, ok := p.caches[filepath]
    p.mu.RUnlock()
    if !ok { return nil, false }
    return c.get(chunkId)
}

func (p *PerFileLRU) Set(filepath string, chunk *Chunk) {
    p.mu.Lock()
    if _, ok := p.caches[filepath]; !ok {
        p.caches[filepath] = newChunkLRU(p.maxPerFile)
    }
    p.mu.Unlock()

    p.mu.RLock()
    p.caches[filepath].set(chunk.Id, chunk)
    p.mu.RUnlock()
}
```

**Плюсы:** изолирует кэш каждого файла; чанк файла A не вытесняет чанк файла B.  
**Минусы:** потребление памяти растёт пропорционально числу открытых файлов; нужна очистка при закрытии файла.

---

## Резюме: какой кэш использовать и почему

### storage-agent (персистентный кэш на диске)

| Уровень | Компонент | Рекомендация |
|---------|-----------|-------------|
| L0 (RAM hot) | SLRU in-memory | **Сохранить, расширить до ARC** для адаптации к паттерну нагрузки |
| L1 (disk) | Файловый кэш (temp+rename) | **Сохранить** — оптимален для больших бинарных блоков |
| L1 metadata | — | **Добавить SQLite-индекс** для структурированного LRU-вытеснения |
| Write path | Write-behind async queue | **Сохранить** — decouples I/O от пути чтения |

**Обоснование:**
- Для чанков ML-моделей размером 16–128 МБ файловый кэш (один файл на чанк) является оптимальным: запись/чтение — последовательный I/O; файловая система — естественный индекс; OS page cache автоматически кэширует горячие чанки в RAM.
- BadgerDB/Pebble/LevelDB (LSM-деревья) не подходят для чанков >4 МБ из-за write amplification и ограничений Value Log.
- BoltDB (B-tree) плох для больших значений — все данные хранятся в одном файле, что создаёт конкуренцию за блокировки.
- ARC предпочтительнее чистого LRU, когда агент обслуживает смешанную нагрузку: повторные обращения к популярным моделям (frequency) + разовые сканирования при первой загрузке (recency). ARC автоматически адаптирует split между двумя паттернами без ручной настройки.
- SQLite в WAL-режиме обеспечивает достаточную пропускную способность для TouchChunk-операций: время записи одной строки < 1 мс, что не влияет на latency чтения чанка (десятки миллисекунд).

**Итоговая рекомендация:** файловый кэш + SQLite WAL + ARC in-memory + write-behind queue.

---

### storage-mounter (буферизация чтения по UDS из сокета)

| Компонент | Рекомендация |
|-----------|-------------|
| Ring buffer | **Сохранить для single-file**; заменить на Per-file LRU при multi-file |
| Prefetcher (look-ahead) | **Сохранить** — критически важен для скрытия I/O latency |
| singleflight dedup | **Сохранить** — предотвращает thundering herd на storage-agent |
| sync.Pool | **Сохранить** — критически важен для снижения GC при высоком параллелизме |

**Обоснование:**
- Паттерн чтения ML-весов (.safetensors) — преимущественно последовательный: слои модели читаются линейно от начала файла к концу. Ring buffer с look-ahead prefetching идеально покрывает этот сценарий.
- При чтении шардированных моделей (несколько .safetensors файлов одновременно) ring buffer даёт коллизии — чанки разных файлов с одинаковым chunkId вытесняют друг друга. В этом сценарии следует перейти на per-file LRU.
- 2Q и ARC избыточны для mounter: mounter работает с in-memory буфером небольшой ёмкости (10–30 чанков), персистентность не нужна, а ARC/2Q добавляют overhead без значимого прироста hit rate при последовательном паттерне.
- Мультиразмерный sync.Pool критически важен: при FUSE каждый syscall read() создаёт запрос на один чанк; при chunk_size = 32 МБ и 64 параллельных горутинах без пула создаётся 2 ГБ новых аллокаций за секунду, что насыщает GC.

**Итоговая рекомендация:** ring buffer (→ per-file LRU при multi-file) + prefetcher + singleflight + sync.Pool.
