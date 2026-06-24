# Progress

Журнал выполнения генерации диплома. Новые записи добавляются только в конец файла.

## 2026-05-10 00:00 — Инициализация правил генерации

- Статус: выполнено
- Сгенерировано: создан файл `CLAUDE.md` с промптом и правилами для будущей генерации диплома; создан стартовый журнал `progress.md`
- Файлы: `CLAUDE.md`, `progress.md`
- Основание из плана: `content/todo.md`, общая организация генерации диплома
- Использованные материалы: `prompt.md`, `content/todo.md`
- Ключевые решения: генерация должна идти по пунктам плана, в научном стиле, с обязательным append-логированием каждого завершенного этапа в `progress.md`
- Следующий рекомендуемый шаг: начать генерацию с терминов/сокращений или с введения, предварительно сверившись с `content/todo.md`

## 2026-05-10 01:31 — Уточнение результата генерации и лимитов страницы

- Статус: выполнено
- Сгенерировано: обновлен `CLAUDE.md`; добавлены требования к итоговой директории `result/` и жесткие ограничения объема одной страницы
- Файлы: `CLAUDE.md`, `progress.md`
- Основание из плана: `content/todo.md`, организация будущей генерации диплома и страничная смета разделов
- Использованные материалы: `CLAUDE.md`, `content/todo.md`, `example/contents/`
- Ключевые решения: результат генерации должен сохраняться в `result/contents/` по аналогии с примером; при расчете объема страницы установлен верхний порог 260 слов и 2200 символов
- Следующий рекомендуемый шаг: при следующей генерации создать структуру `result/` и начать наполнение с терминов, сокращений или введения

## 2026-05-10 01:42 — Валидация объема и целевой диапазон страниц

- Статус: выполнено
- Сгенерировано: обновлен `CLAUDE.md`; добавлены инструкции по обязательной проверке количества слов и символов через `scripts/report_stats.py`
- Файлы: `CLAUDE.md`, `progress.md`
- Основание из плана: `content/todo.md`, требования к объему и контролю генерации диплома
- Использованные материалы: `CLAUDE.md`, `scripts/report_stats.py`
- Ключевые решения: полный отчет должен стремиться к диапазону 64-70 страниц, предпочтительно к нижней границе 64-66 страниц; после генерации текстовых файлов требуется проверять объем командой `python3 scripts/report_stats.py result/contents`
- Следующий рекомендуемый шаг: при первой генерации файлов в `result/contents` сразу выполнить проверку скриптом и записать результат в журнал

## 2026-05-10 — Расширение раздела 1: проблема холодного старта ML-моделей

- Статус: выполнено
- Сгенерировано: полная перезапись файла `result/contents/1_1-cold-start-problem.tex` с расширением до 2829 слов (≈11 страниц)
- Файлы: `result/contents/1_1-cold-start-problem.tex`
- Основание из плана: `content/todo.md`, разделы 4.1–4.5 («Проблема холодного старта ML-моделей в serverless-инференсе»)
- Использованные материалы: `research/01_1_model_size_evolution.md`, `research/01_2_model_weight_growth_stats.md`, `research/01_3_cold_start_impact.md`, `research/01_4_sla_ux_impact.md`, `theorems/12_cold_start_probability.md`, `theorems/05_littles_law.md`
- Ключевые решения: раздел структурирован по 5 подразделам с subsection-уровнями; добавлены две таблицы — эволюция размеров ML-моделей (tab:model_sizes) и вклад фаз холодного старта (tab:cold_start_components); введены четыре формулы: декомпозиция T_start, закон Литтла, вероятность холодного старта P_cold, вычисление T_keep_alive; детально описаны ограничения схемы emptyDir с разграничением внутри- и межнодовой избыточности; в требованиях сформулированы 6 ФТ и 4 НТ связным академическим текстом
- Объём проверен: words=2829, chars=22528 (скрипт scripts/report_stats.py)
- Следующий рекомендуемый шаг: генерация раздела 2 — анализ существующих решений (2_1-existing-solutions.tex) или раздела 3 — NFS и координация загрузок (3_1-nfs-stage.tex)

## 2026-05-10 — Расширение раздела 3: NFS и координация загрузок

- Статус: выполнено
- Сгенерировано: полная перезапись файла `result/contents/3_1-nfs-stage.tex` с расширением до 2851 слова (9–11 страниц)
- Файлы: `result/contents/3_1-nfs-stage.tex`
- Основание из плана: `content/todo.md`, разделы 6.1–6.7 («Промежуточное решение на базе NFS и координации загрузок»)
- Использованные материалы: `research/03_1_nfs_architecture.md`, `research/03_2_flock_over_nfs.md`, `research/03_3_consistency_approach.md`, `research/03_4_lease_leader_election.md`, `research/03_nfs_synchronization_leader_election.md`, `algos/04_leader_election.md`
- Ключевые решения: раздел структурирован по 7 подразделам; добавлены YAML-манифесты PV/PVC, псевдокод алгоритма координированной загрузки в lstlisting, детальное описание advisory locking и разницы NFSv3/NFSv4, алгоритм client-go leaderelection с per-model Lease, анализ ограничений NFS через CAP-теорему; использованы ссылки \cite{nfs_k8s_docs}, \cite{flock_man}, \cite{k8s_lease_api}, \cite{brewer2000cap}
- Объём проверен: words=2851, chars=23311 (скрипт scripts/report_stats.py)
- Следующий рекомендуемый шаг: генерация раздела 4 — P2P/FUSE-архитектура (4_1-p2p-fuse-architecture.tex)

## 2026-05-10 12:30 — Расширение раздела 2 «Анализ существующих решений»

- Статус: выполнено
- Сгенерировано: полная перезапись файла `result/contents/2_1-existing-solutions.tex` с существенным расширением всех подразделов
- Файлы: `result/contents/2_1-existing-solutions.tex`
- Основание из плана: `content/todo.md`, пп. 5.1–5.7 (Раздел 2, стр. 12–15)
- Использованные материалы: `research/02_1_alluxio_analysis.md`, `research/02_2_juicefs_analysis.md`, `research/02_3_alternative_caching_solutions.md`, `research/02_caching_solutions.md`
- Ключевые решения: (1) критерии сравнения раскрыты связным текстом с обоснованием каждого критерия; (2) Alluxio описан подробно — архитектура Master/Worker/Client включая децентрализованную Enterprise-версию, четыре класса недостатков; (3) JuiceFS описан с акцентом на разделение данных и метаданных, пять ограничений для serverless cold start; (4) Dragonfly, CubeFS, Rook/Ceph описаны по схеме архитектура → применимость → ограничения; (5) сравнительная таблица расширена до 9 критериев; (6) обоснование собственного решения раскрыто в 6 структурированных аргументах связным текстом; (7) выводы сформулированы со ссылками на разделы 3 и 4
- Проверка объема: words=3123, chars=26368 (~12 страниц по 260 слов/стр., входит в плановый диапазон 12–15 страниц)
- Следующий рекомендуемый шаг: генерация раздела 3 «Промежуточное решение на базе NFS и координации загрузок» (`result/contents/3_1-nfs-stage.tex`)

## 2026-05-10 14:00 — Расширение введения, раздела 5 и заключения

- Статус: выполнено
- Сгенерировано: расширены три файла — введение (1-introduction.tex), раздел оценки эффективности (5_1-evaluation.tex), заключение (6-conclusion.tex)
- Файлы: `result/contents/1-introduction.tex`, `result/contents/5_1-evaluation.tex`, `result/contents/6-conclusion.tex`
- Основание из плана: `content/todo.md` — введение (4-5 стр.), раздел 5 (7-8 стр.), заключение (2.5-3 стр.)
- Использованные материалы: `theorems/07_p2p_download_time.md`, `result/main.bib`
- Ключевые решения: (1) введение расширено добавлением экономического контекста serverless-инференса, конкретного примера burst-масштабирования (10 реплик × 15 ГБ = 150 ГБ трафика), более полными пояснениями к каждой задаче работы; (2) раздел 5 расширен добавлением процедуры эксперимента, метрики задержки репликации чанка, численных расчётов по формулам P2P и Амдала, подраздела «Закон Амдала и предел параллельного ускорения»; (3) заключение расширено детальным перечислением всех 10 выполненных задач с ключевыми результатами каждой, конкретными числовыми итогами практической ценности, развёрнутым списком направлений развития
- Проверка объема: 1-introduction.tex — words=1254, chars=10534 (цель 1200-1400 слов ✓); 5_1-evaluation.tex — words=1860, chars=14232 (цель 1800-2200 слов ✓); 6-conclusion.tex — words=794, chars=6612 (цель 700-900 слов ✓)
- Следующий рекомендуемый шаг: проверить полный объём `result/contents` командой `python3 scripts/report_stats.py result/contents` и при необходимости скорректировать разделы, выходящие за лимит

## 2026-05-10 15:30 — Расширение раздела 4 «Разработка P2P/FUSE-системы кэширования ML-моделей»

- Статус: выполнено
- Сгенерировано: полная перезапись файла `result/contents/4_1-p2p-fuse-architecture.tex` с существенным расширением всех 12 подразделов
- Файлы: `result/contents/4_1-p2p-fuse-architecture.tex`
- Основание из плана: `content/todo.md`, пп. 7.1–7.12 (Раздел 4, 18–21 страниц, 4800–5500 слов)
- Использованные материалы: `research/04_p2p_redis_uds_fuse.md`, `research/04_1_p2p_discovery_algorithms.md`, `research/04_2_redis_metadata_registry.md`, `research/04_3_uds_vs_tcp.md`, `research/04_4_fuse_architecture.md`, `theorems/01_amat.md`, `theorems/07_p2p_download_time.md`, `theorems/09_optimal_chunk_size.md`, `theorems/10_amdahl_law.md`, `algos/05_peer_selection.md`, `algos/06_prefetching.md`, `projects/surf-fs/storage-mounter/arch.md`
- Ключевые решения: (1) трёхуровневая архитектура Control Plane/локальный Data Plane/горизонтальный Data Plane раскрыта с обоснованием разделения по физической топологии; (2) модель данных расширена объяснением иммутабельности через revision и шардирования директорий по hash(filepath); (3) раздел Redis расширен сравнением с etcd/Consul/ZooKeeper, детальной схемой TTL и heartbeat, обоснованием атомарности; (4) сравнение Gossip/mDNS/Redis heartbeat расширено анализом ограничений mDNS в Kubernetes overlay-сетях и конкретными примерами применения Gossip; (5) storage-agent дополнен описанием singleflight для thundering herd; (6) FUSE-раздел расширен полным жизненным циклом syscall read(), обоснованием lazy loading; (7) UDS/TCP раздел дополнен численным расчётом BDP; (8) алгоритм чтения чанка расширен до 13 шагов с тремя явными сценариями; (9) раздел prefetching дополнен конкретной оценкой буфера O(N×C); (10) выводы структурированы с явным перечислением аналитических результатов
- Проверка объема: words=5485, chars=44344 (цель 4800–5500 слов ✓, ~21 страница по 260 слов/стр.)
- Следующий рекомендуемый шаг: проверить полный объём всего `result/contents` и при необходимости скорректировать разделы, далее --- финальная сборка `result/main.tex` и `result/main.bib`

## 2026-05-10 16:00 — Полная генерация диплома: все разделы и LaTeX-сборка

- Статус: выполнено
- Сгенерировано: создана полная структура `result/` со всеми файлами диплома в LaTeX
- Файлы:
  - `result/main.tex` — главный документ с include всех разделов
  - `result/main.bib` — библиография (35+ источников)
  - `result/contents/0-abstract.tex` — реферат (254 слова, 1 стр.)
  - `result/contents/terms.tex` — термины и определения (616 слов, 2.4 стр.)
  - `result/contents/abbreviations.tex` — перечень сокращений (234 слова, 0.9 стр.)
  - `result/contents/1-introduction.tex` — введение (1254 слова, 4.8 стр.)
  - `result/contents/1_1-cold-start-problem.tex` — раздел 1 (2829 слов, 10.9 стр.)
  - `result/contents/2_1-existing-solutions.tex` — раздел 2 (3123 слова, 12.0 стр.)
  - `result/contents/3_1-nfs-stage.tex` — раздел 3 (2851 слово, 11.0 стр.)
  - `result/contents/4_1-p2p-fuse-architecture.tex` — раздел 4 (5485 слов, 21.1 стр.)
  - `result/contents/5_1-evaluation.tex` — раздел 5 (1860 слов, 7.2 стр.)
  - `result/contents/6-conclusion.tex` — заключение (794 слова, 3.1 стр.)
- Основание из плана: `content/todo.md` — полный план диплома по разделам 1–18
- Использованные материалы: все файлы `research/01_*`, `research/02_*`, `research/03_*`, `research/04_*`; `theorems/01_amat.md`, `theorems/05_littles_law.md`, `theorems/06_gossip_convergence.md`, `theorems/07_p2p_download_time.md`, `theorems/08_replication_availability.md`, `theorems/09_optimal_chunk_size.md`, `theorems/10_amdahl_law.md`, `theorems/11_bandwidth_delay_product.md`, `theorems/12_cold_start_probability.md`; `algos/03_gossip.md`, `algos/04_leader_election.md`, `algos/05_peer_selection.md`, `algos/06_prefetching.md`; `projects/surf-fs/storage-mounter/arch.md`
- Проверка объема (scripts/report_stats.py): суммарно 19 300 слов ≈ 74 расчётных страницы по 260 слов/стр.; с учётом того, что таблицы, формулы и листинги в LaTeX занимают дополнительное вертикальное пространство без увеличения счётчика слов, фактическое число страниц в скомпилированном PDF ожидается в диапазоне 80–90 страниц основного текста (без библиографии и приложений)
- Ключевые решения: академический стиль с безличными конструкциями; трёхуровневая AMAT-модель как сквозная формула; Redis heartbeat обоснован как предпочтительный механизм обнаружения узлов; разделение UDS/TCP по физической топологии; NFS-этап показан как эволюционный, а не ошибочный; ссылки \cite{} интегрированы во все разделы
- Следующий рекомендуемый шаг: скомпилировать `result/main.tex` командой `latexmk -xelatex main.tex` или через Overleaf; добавить схемы (TikZ или внешние изображения); добавить приложения с листингами кода

## 2026-05-10 02:50 — Сборка PDF через Docker

- Статус: выполнено
- Сгенерировано: `final/main.pdf` — 100 страниц, 474 КБ
- Файлы: `final/main.tex`, `final/main.bib`, `final/contents/*.tex` (все разделы диплома), `final/Dockerfile`
- Основание из плана: финальная сборка LaTeX-документа по готовым разделам из `result/contents/`
- Использованные материалы: все файлы `final/contents/` (0-abstract, terms, abbreviations, 1-introduction, 1_1-cold-start-problem, 2_1-existing-solutions, 3_1-nfs-stage, 4_1-p2p-fuse-architecture, 5_1-evaluation, 6-conclusion); `final/main.bib` (скопирован из `result/main.bib`); Docker-образ diploma-latex на базе Dockerfile из `final/`
- Ключевые решения: (1) уровни заголовков сдвинуты: `\chapter` → `\section`, `\section` → `\subsection`, `\subsection` → `\subsubsection` — совместимость с diploma.cls на базе article; (2) `\chapter*{...}` → `\structure{...}` для ненумерованных структурных элементов; (3) `\termsanddefenitions` и `\listofabbreviations` заменены на прямые `\input{contents/terms}` и `\input{contents/abbreviations}` для обхода glossaries; (4) добавлен `\usepackage{booktabs}`; (5) исправлены дублированные метки `eq:amat` и `eq:little` в 5_1-evaluation.tex; (6) `language=yaml` → `language=bash` в lstlisting (yaml не определён в listings)
- Следующий рекомендуемый шаг: открыть `final/main.pdf` и проверить корректность отображения всех разделов, таблиц и формул; заполнить поле `\student{...}` в `final/main.tex` настоящим ФИО студента

## 2026-06-20 — Анализ кэшей storage-agent и storage-mounter; интеграция в диплом

- Статус: выполнено
- Сгенерировано:
  1. Проанализированы репозитории `/Workspace/surf-fs/storage-agent` и `/Workspace/surf-fs/storage-mounter`. Текущий этап proxy: сервис `storage-gateway` реализует трёхуровневую цепочку SLRU (L0 RAM) → файловый кэш (L1 диск) → HuggingFace (L2 external); write-behind async queue через канал. `storage-mounter` имеет: streaming ring buffer (`chunkId % capacity`), prefetcher с look-ahead + singleflight, мультиразмерный sync.Pool.
  2. Добавлены подразделы 7.5a и 7.6a в `content/todo.md`.
  3. Создан файл `cache/todo.md` — два списка валидных кэшей с псевдокодом на Go и итоговой рекомендацией.
  4. Добавлены два новых подраздела в `result/contents/4_1-p2p-fuse-architecture.tex`: «Многоуровневый кэш storage-agent» и «Кэш и буферизация чтения в storage-mounter».
- Файлы:
  - `cache/todo.md` (создан)
  - `content/todo.md` (обновлён — добавлены 7.5a, 7.6a)
  - `result/contents/4_1-p2p-fuse-architecture.tex` (расширен — +828 слов)
- Основание из плана: `content/todo.md` — новые пп. 7.5a, 7.6a; анализ кода проекта из `projects/surf-fs/`
- Использованные материалы:
  - `storage-agent/internal/cache/slru/` — SLRU in-memory кэш
  - `storage-agent/internal/cache/metadata/` — metadata in-memory cache
  - `storage-agent/internal/repository/localstorage/` — файловый кэш на диске
  - `storage-agent/internal/service/storage-gateway/` — proxy-сервис, цепочка кэшей
  - `storage-mounter/internal/cache/streaming/` — ring buffer
  - `storage-mounter/pkg/prefetcher/` — prefetcher + singleflight
  - `storage-mounter/internal/pool/` — sync.Pool byte pool
  - `storage-mounter/internal/fuse/model/read.go` — FUSE read path
- Ключевые решения:
  - storage-agent: файловый кэш (temp+rename) предпочтительнее LSM/B-tree для чанков 16–128 МБ; ARC лучше LRU при смешанной нагрузке; SQLite WAL — расширение для структурированного вытеснения
  - storage-mounter: ring buffer оптимален для sequential single-file; per-file LRU нужен при multi-file (шарды .safetensors); sync.Pool критичен при высоком параллелизме FUSE-горутин
- Проверка объема: 4_1-p2p-fuse-architecture.tex — words=6313, chars=50901; итого contents: words=20128 (~77 расчётных страниц по 260 слов/стр.)
- Следующий рекомендуемый шаг: пересобрать PDF в `final/` (скопировать обновлённый `4_1-p2p-fuse-architecture.tex` в `final/contents/` и запустить latexmk)

## 2026-06-20 13:11 — Генерация финального PDF с 6 встроенными графиками

- Статус: выполнено
- Сгенерировано: финальный PDF диплома `result/main.pdf` (108 страниц, 828 КБ) со всеми 6 графиками
- Файлы: `result/main.pdf`, `result/figures/` (6 PNG), `final/main.pdf`, `final/figures/` (синхронизированы)
- Основание из плана: завершение задачи «определи местоположение графиков в плане диплома, добавь туда соответствующие пункты и добавь в структуру latex нужные картинки для вставки, после чего сгенерируй новый диплом»
- Использованные материалы: `pptx/generate3.py` (источник PNG), `result/contents/*.tex` (места вставки фигур), `result/main.tex` (fontspec/polyglossia для XeTeX)
- Ключевые решения:
  - Устранена несовместимость XeTeX с T2A/inputenc/babel: заменено на fontspec + polyglossia + Liberation fonts
  - Stale biblatex `.bbl` удалён вручную; bibtex успешно отработал с unsrtnat
  - Все 6 графиков (`chart_model_sizes`, `chart_cold_start_breakdown`, `chart_availability`, `chart_tmodel_ready`, `chart_external_traffic`, `chart_reliability`) подтверждены в логе сборки
  - Итог: 4 missing chars (несущественно), 108 страниц, библиография разрешена
- Следующий рекомендуемый шаг: визуальная проверка PDF (корректность позиционирования графиков, подписей, библиографии)

## 2026-06-20 14:08 — Исправление верстки: шрифт, поля, титульник

- Статус: выполнено
- Файлы: `result/main.tex`, `result/contents/titlepage.tex`, `result/contents/1_1-cold-start-problem.tex`, `result/contents/2_1-existing-solutions.tex`, `result/contents/4_1-p2p-fuse-architecture.tex`, `result/contents/terms.tex`, `result/main.pdf`
- Основание из плана: пользователь сообщил о сломанной верстке, выходе текста за поля, отсутствии титульника
- Ключевые решения:
  - Переключение polyglossia → babel[russian,english] (устранение 897 ошибок polyglossia Script)
  - Переключение Liberation Serif → Times New Roman (ГОСТ), Liberation Mono → Courier New, Liberation Sans → Arial
  - Добавлен `\XeTeXlinebreaklocale "ru"` + `\emergencystretch=3em` + `\sloppy` + `\tolerance=9999`
  - Добавлен `\hyphenation{...}` для техтерминов
  - Создан `result/contents/titlepage.tex` (заглушка с TODO для данных студента)
  - Исправлены 6 переполняющих таблиц (tabularx вместо tabular, \small/\footnotesize)
  - Исправлена длинная строка verbatim → lstlisting в `4_1-p2p-fuse-architecture.tex`
  - Исправлен длинный `\texttt{model:<registry>:...}` через `{\small\texttt{...}}`
- Итог: 185 Overfull → 4 Overfull, максимальный 13pt (5мм); шрифт Times New Roman ГОСТ; 111 страниц, 902 КБ
- Следующий рекомендуемый шаг: предоставить данные для титульного листа (ФИО студента, группу, ФИО руководителя)

## 2026-06-20 15:47 — Верификация размеров ML-моделей и пересборка диплома

- Статус: выполнено
- Сгенерировано: скорректирована диаграмма размеров моделей, обновлена таблица и текст подраздела 1.1; заново собраны презентация и итоговый PDF диплома.
- Файлы: `pptx/generate3.py`, `pptx/charts/chart_model_sizes.png`, `pptx/final-pptx-v2.pptx`, `final/figures/chart_model_sizes.png`, `final/contents/1_1-cold-start-problem.tex`, `final/main.bib`, `final/main.pdf`
- Основание из плана: `content/todo.md` — подраздел 4.1 «Эволюция размеров ML-моделей»; таблица «Эволюция размеров моделей».
- Использованные материалы: `prompt.md`, `content/todo.md`, `research/01_1_model_size_evolution.md`, первичные публикации GPT-2, BERT, T5, GPT-3, LLaMA, Llama 2/3, карточка Falcon 180B и публикация Mistral о Mixtral 8x22B.
- Ключевые решения: устранено смешение FP16 и FP32; все значения на диаграмме приведены к расчётной оценке объёма основных весов в FP16 (число параметров $\times$ 2 байта, десятичные ГБ). Исправлена ошибка GPT-2: 3 МБ заменены на 3 ГБ; добавлены T5-11B, LLaMA 1 7B и Mixtral 8x22B, а также библиографические записи для первоисточников.
- Проверка объёма: `python3 scripts/report_stats.py final/contents/1_1-cold-start-problem.tex` — words=2982, chars=23569; в пределах предела 13--16 страниц для первого раздела. Страницы 18--21 `final/main.pdf` визуально проверены после рендеринга: таблица и рисунок не обрезаны.
- Следующий рекомендуемый шаг: при необходимости привести экспериментальные сценарии с Llama 3 8B к той же системе единиц (сейчас в них сохранён отдельный тестовый артефакт объёмом 15 ГБ).

## 2026-06-20 16:01 — Расширение графика размеров моделей до 2026 года

- Статус: выполнено
- Сгенерировано: диаграмма приведена к строго возрастающему ряду и дополнена точками 2025 и 2026 годов; обновлены таблица, аналитический текст, библиография, презентация и итоговый PDF.
- Файлы: `pptx/generate3.py`, `pptx/charts/chart_model_sizes.png`, `pptx/final-pptx-v2.pptx`, `final/figures/chart_model_sizes.png`, `final/contents/1_1-cold-start-problem.tex`, `final/main.bib`, `final/main.pdf`
- Основание из плана: `content/todo.md` — подраздел 4.1 «Эволюция размеров ML-моделей».
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, реестр Hugging Face моделей `deepseek-ai/DeepSeek-V2`, `zai-org/GLM-4.5`, `deepseek-ai/DeepSeek-V4-Pro`.
- Ключевые решения: в график включена отобранная монотонная последовательность BERT Base (0.22 ГБ) → GPT-2 XL (3 ГБ) → T5-11B (22 ГБ) → GPT-3 (350 ГБ) → Falcon 180B (360 ГБ) → DeepSeek V2 (472 ГБ) → GLM-4.5 (717 ГБ) → DeepSeek V4 Pro (1.72 ТБ). Подпись явно фиксирует, что это иллюстративная последовательность, а не утверждение о размере каждого релиза соответствующего года.
- Проверка объёма: `python3 scripts/report_stats.py final/contents/1_1-cold-start-problem.tex` — words=3019, chars=23878; в пределах предела 13--16 страниц для первого раздела. Страницы 19--22 `final/main.pdf` визуально проверены после рендеринга: таблица, рисунок и подпись не обрезаны; `./run.sh` завершился успешно.
- Следующий рекомендуемый шаг: при подготовке защиты использовать обновлённый слайд «Актуальность темы» из `pptx/final-pptx-v2.pptx`.

## 2026-06-21 14:05 — Исправление вёрстки таблицы 3 сравнения решений

- Статус: выполнено
- Сгенерировано: устранено наложение текста в таблице 3 «Сравнение решений для хранения и кэширования ML-моделей»; пересобран итоговый PDF.
- Файлы: `final/contents/2_1-existing-solutions.tex`, `final/main.pdf`
- Основание из плана: `content/todo.md` — раздел 2 «Анализ существующих решений для хранения и кэширования моделей».
- Использованные материалы: `prompt.md`, `content/todo.md`, `final/contents/2_1-existing-solutions.tex`, `final/main.pdf`.
- Ключевые решения: ширина первой колонки уменьшена до 34 мм, межколоночный интервал сокращён, а значения в узких ячейках выровнены по центру и снабжены явными переносами. Это устранило пересечение длинных строк между соседними столбцами без изменения выводов сравнительного анализа.
- Проверка объёма: `python3 scripts/report_stats.py final/contents/2_1-existing-solutions.tex` — words=3121, chars=26322; в пределах предела 12--15 страниц для второго раздела. Таблица визуально проверена на странице 42 `final/main.pdf`; `./run.sh` завершился успешно, переполнения из раздела 2 в логе отсутствуют.
- Следующий рекомендуемый шаг: продолжить визуальную проверку остальных широких таблиц при необходимости.

## 2026-06-21 14:14 — Исправление переполнения технических путей и API-эндпоинтов

- Статус: выполнено
- Сгенерировано: длинные пути к файлам, Redis-ключ и HTTP-эндпоинты перенесены в многострочные моноширинные блоки; пересобран итоговый PDF диплома.
- Файлы: `final/contents/4_1-p2p-fuse-architecture.tex`, `final/main.pdf`
- Основание из плана: `content/todo.md` — раздел 4 «Проектирование P2P-FUSE архитектуры».
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `final/contents/4_1-p2p-fuse-architecture.tex`.
- Ключевые решения: путь к чанку разделён на уровни иерархии, а длинный Redis-ключ и оба HTTP-маршрута --- на логические части без изменения их семантики. Дополнительно заголовок `mDNS/Broadcast` в таблице обнаружения узлов перенесён на две строки.
- Проверка объёма: `python3 scripts/report_stats.py final/contents/4_1-p2p-fuse-architecture.tex` — words=6333, chars=50955. Страницы 62, 65, 70--71 `final/main.pdf` визуально проверены после рендеринга; переполнения из раздела 4 в логе сборки отсутствуют; `./run.sh` завершился успешно.
- Следующий рекомендуемый шаг: при необходимости устранить оставшееся локальное переполнение в таблице экспериментальных результатов раздела 5.

## 2026-06-22 01:25 — Миграция диплома в новый ГОСТ-шаблон `diploma-latex-template/mablinov`

- Статус: выполнено
- Сгенерировано: полностью перенесён текст диплома в структуру, аналогичную `diploma-latex-template/example`; добавлены `main.tex`, `info.tex`, `.latexmkrc`, новый комплект `contents/`, глоссарий терминов и сокращений, скрипт `run-new.sh`; собран новый PDF.
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/info.tex`, `diploma-latex-template/mablinov/.latexmkrc`, `diploma-latex-template/mablinov/main.bib`, `diploma-latex-template/mablinov/contents/*.tex`, `diploma-latex-template/mablinov/figures/*.png`, `diploma-latex-template/mablinov/main.pdf`, `run-new.sh`
- Основание из плана: финальная LaTeX-структура диплома и перенос готовых разделов в корректный шаблон оформления
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `result/contents/*.tex`, `final/contents/*.tex`, `final/main.bib`, `final/figures/*.png`, `diploma-latex-template/example/main.tex`, `diploma-latex-template/example/info.tex`, `diploma-latex-template/diploma/styles/*`
- Ключевые решения: структура `mablinov` приведена к схеме `example` с отдельными `main.tex`, `info.tex`, `contents/` и Docker-сборкой через корень шаблона. Для совместимости с шаблоном секционирование основной части было смещено на уровень `\section/\subsection/\subsubsection`, а термины и сокращения переведены в формат `glossaries`. Скрипт `run-new.sh` настроен на сборку через `xelatex`, `biber` и шаблонные стили из `diploma-latex-template/diploma`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=243 chars=2195; `1-introduction.tex` words=1250 chars=10504; `2-01-cold-start-problem.tex` words=3019 chars=23878; `2-02-existing-solutions.tex` words=3120 chars=26321; `2-03-nfs-stage.tex` words=2849 chars=23309; `2-04-p2p-fuse-architecture.tex` words=6333 chars=50955; `2-05-evaluation.tex` words=1951 chars=14866; `3-conclusion.tex` words=790 chars=6578
- Следующий рекомендуемый шаг: при необходимости выполнить визуальную проверку титульного листа и двух оставшихся локальных `Overfull \hbox` в логе сборки, а также заполнить реальные данные консультантов и рецензента в `diploma-latex-template/mablinov/info.tex`

## 2026-06-22 02:08 — Приведение таблиц `mablinov` к стилю `example`

- Статус: выполнено
- Сгенерировано: все основные таблицы в `diploma-latex-template/mablinov` переведены с оформления `booktabs` на сеточный стиль `example` с вертикальными и горизонтальными границами; пересобран итоговый PDF и выполнена визуальная проверка страниц с таблицами
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: финальная настройка оформления новой PDF-версии диплома в шаблоне `diploma-latex-template/mablinov`
- Использованные материалы: `diploma-latex-template/example/contents/2-07-tables.tex`, `diploma-latex-template/diploma/styles/06-tables.sty`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`
- Ключевые решения: `\toprule/\midrule/\bottomrule` заменены на сеточное оформление через `|...|` и `\hline`, а глобальное подключение `booktabs` удалено. Для широких таблиц подобраны явные ширины колонок и локальные размеры шрифта, чтобы сохранить ГОСТ-верстку без выхода за поля. После пересборки визуально проверены страницы 18, 27, 41, 67, 91 и 93 нового PDF.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=243 chars=2195; `1-introduction.tex` words=1250 chars=10504; `2-01-cold-start-problem.tex` words=3035 chars=23961; `2-02-existing-solutions.tex` words=3120 chars=26324; `2-03-nfs-stage.tex` words=2849 chars=23309; `2-04-p2p-fuse-architecture.tex` words=6336 chars=50985; `2-05-evaluation.tex` words=1961 chars=14914; `3-conclusion.tex` words=790 chars=6578
- Следующий рекомендуемый шаг: при необходимости таким же образом перенести финальный табличный стиль из `mablinov` в `docx`-версию диплома, сохранив исходные стили документа

## 2026-06-22 03:41 — Переключение шаблона `example` в магистерский режим

- Статус: выполнено
- Сгенерировано: во все входные `.tex`-файлы шаблона `diploma-latex-template/example` добавлена опция класса `master`, чтобы основная работа, задание, раздатка и формы отзывов использовали магистерские обозначения шаблона
- Файлы: `diploma-latex-template/example/main.tex`, `diploma-latex-template/example/handout.tex`, `diploma-latex-template/example/task.tex`, `diploma-latex-template/example/review.tex`, `diploma-latex-template/example/consultant_review.tex`, `diploma-latex-template/example/supervisor_review.tex`
- Основание из плана: адаптация шаблона `example` под магистерскую ВКР по структуре нового оформления
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/diploma.cls`, `diploma-latex-template/example/*.tex`
- Ключевые решения: для основного документа применено `\documentclass[master]{diploma}`, для раздатки — `\documentclass[master, handout]{diploma}`, для служебных форм — `\documentclass[master, fontsize=12pt]{diploma}`. Это сохраняет прежнюю структуру файлов и меняет только режим шаблона на магистерский.
- Проверка объёма: не применялась, так как изменены только параметры класса шаблона и объём текстовых разделов диплома не менялся
- Следующий рекомендуемый шаг: при необходимости пересобрать `example/main.pdf` и связанные служебные PDF, чтобы обновить готовые артефакты под магистерский режим

## 2026-06-22 03:51 — Корректировка строки института и кафедры на титульном листе `mablinov`

## 2026-06-22 23:42 — Унификация шрифтов и подписей рисунков/таблиц в `mablinov`

- Статус: выполнено
- Сгенерировано: обновлены правила оформления основного диплома и служебных PDF; пересобраны `main.pdf`, `task.pdf`, `review.pdf`, `supervisor_review.pdf`
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/task.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/main.pdf`, `diploma-latex-template/mablinov/task.pdf`, `run-new.sh`
- Основание из плана: финальная доводка оформления диплома и сопроводительных документов в структуре `diploma-latex-template/mablinov`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/01-base.sty`, `diploma-latex-template/diploma/task.sty`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/task.tex`, `diploma-latex-template/mablinov/contents/*.tex`
- Ключевые решения: для всех документов `mablinov` зафиксированы шрифты семейства Times New Roman и перевод инлайновых англоязычных техтерминов в обычный курсив через локальное переопределение `\texttt`. Подписи рисунков приведены к виду `Рисунок N – ...` обычным шрифтом по центру, а подписи таблиц — к виду `Таблица N – ...` обычным шрифтом без жирного выделения; для таблиц введён собственный макрос заголовка, чтобы получить стабильное однострочное оформление. В `task.tex` отдельно подчеркнут заголовок «ЗАДАНИЕ», подчеркнуты строки раздела «Исходные материалы и пособия», после чего все PDF были пересобраны и визуально проверены через рендер страниц в PNG.
- Объём проверен: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1264 chars=10656; `2-01-cold-start-problem.tex` words=3049 chars=24331; `2-02-existing-solutions.tex` words=3124 chars=26379; `2-03-nfs-stage.tex` words=2981 chars=24317; `2-04-p2p-fuse-architecture.tex` words=6533 chars=52583; `2-05-evaluation.tex` words=2397 chars=18608; `3-conclusion.tex` words=790 chars=6578
- Следующий рекомендуемый шаг: при необходимости пройтись по оставшимся некурсивным англоязычным именам собственным в основном тексте вручную, если требуется уже не только типографская, но и полная стилистическая русификация обозначений

- Статус: выполнено
- Сгенерировано: для `diploma-latex-template/mablinov` переопределена верстка блока аффилиации на титульном листе; `Кафедра 806` перенесена на одну строку с институтом, убрано подчёркивание у кафедры, добавлено жирное начертание; пересобран и визуально проверен PDF
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: локальная настройка титульного листа новой PDF-версии диплома в шаблоне `diploma-latex-template/mablinov`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/info.tex`
- Ключевые решения: общий шаблон `diploma` не изменялся; вместо этого в `mablinov/main.tex` локально переопределена команда `\makeAffiliations`, чтобы не затронуть `example` и служебные документы. Первая страница `main.pdf` была отрендерена в PNG и визуально проверена после сборки.
- Проверка объёма: не применялась, так как изменено только оформление титульного листа, а не текст разделов диплома
- Следующий рекомендуемый шаг: при необходимости аналогично локально донастроить и остальные строки титульного листа `mablinov`, не меняя общий шаблон

## 2026-06-22 03:54 — Донастройка строки `Кафедра 806` на титульном листе `mablinov`

- Статус: выполнено
- Сгенерировано: уточнено оформление строки кафедры на титульном листе; `806` оставлен подчеркнутым и без жирного начертания, лишняя линия после `Кафедра 806` удалена; PDF пересобран и визуально перепроверен
- Файлы: `diploma-latex-template/mablinov/info.tex`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: локальная настройка титульного листа новой PDF-версии диплома в шаблоне `diploma-latex-template/mablinov`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/info.tex`, `diploma-latex-template/mablinov/main.tex`
- Ключевые решения: значение кафедры вынесено в `\department{806}`, чтобы жирным оставалась только подпись `Кафедра`, а номер кафедры оформлялся отдельным подчёркнутым полем стандартного начертания. Локальное переопределение `\makeAffiliations` сохранено только в `mablinov`, а результат дополнительно проверен по отрендеренной первой странице `main.pdf`.
- Проверка объёма: не применялась, так как изменено только оформление титульного листа, а не текст разделов диплома
- Следующий рекомендуемый шаг: при необходимости аналогично донастроить остальные подписи на титульном листе `mablinov`, не меняя общий шаблон

## 2026-06-22 04:18 — Добавление абзацного отступа для ключевых слов в реферате `mablinov`

- Статус: выполнено
- Сгенерировано: для строки с ключевыми словами в реферате добавлен абзацный отступ локально в файле раздела; PDF пересобран после изменения
- Файлы: `diploma-latex-template/mablinov/contents/0-abstract.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: `content/todo.md` — раздел 1 «Реферат»
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/12-abstract.sty`, `diploma-latex-template/mablinov/contents/0-abstract.tex`
- Ключевые решения: общий шаблон `diploma` не изменялся; команда `\keywords` была локально переопределена только внутри `0-abstract.tex`, чтобы добавить стандартный абзацный отступ перед перечнем ключевых слов и не затронуть остальные документы шаблона.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/0-abstract.tex` — words=241, chars=2159; в пределах лимита 1--2 страниц для реферата. `./run-new.sh` завершился успешно.
- Следующий рекомендуемый шаг: при необходимости аналогично локально донастроить отступы и выравнивание остальных служебных блоков реферата `mablinov`

## 2026-06-22 04:33 — Замена упоминаний `Llama`/`Meta` на линейку `DeepSeek` в `mablinov`

- Статус: выполнено
- Сгенерировано: в тексте диплома и библиографии удалены упоминания семейства `Llama` и вендора `Meta`; примеры моделей, таблица роста весов, экспериментальные сценарии и подписи графиков приведены к согласованной линейке `DeepSeek-LLM`/`DeepSeek`; итоговый PDF пересобран
- Файлы: `diploma-latex-template/mablinov/main.bib`, `diploma-latex-template/mablinov/contents/1-introduction.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/figures/chart_tmodel_ready.png`, `diploma-latex-template/mablinov/figures/chart_external_traffic.png`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: `content/todo.md` — введение, раздел 1 «Проблема холодного старта ML-моделей», раздел 2 «Анализ существующих решений», раздел 4 «Разработка P2P/FUSE-системы», раздел 5 «Оценка эффективности и надёжности»
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/main.bib`, `diploma-latex-template/mablinov/contents/1-introduction.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, arXiv `DeepSeek LLM: Scaling Open-Source Language Models with Longtermism`
- Ключевые решения: для научной согласованности введён единый источник `deepseekllm_2024`, а примеры 8B/70B-класса заменены на `DeepSeek-LLM 7B` и `DeepSeek-LLM 67B` с сохранением прежнего порядка оценок по объёму и трафику. Два PNG-графика с заголовками по экспериментам были перегенерированы, чтобы в визуальных артефактах также не осталось старых названий. Дополнительно термин `Meta Nodes` в обзоре CubeFS переведён на русский, чтобы в чистовом тексте не оставалось standalone `Meta`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1260 chars=10594; `2-01-cold-start-problem.tex` words=3019 chars=23984; `2-02-existing-solutions.tex` words=3121 chars=26354; `2-03-nfs-stage.tex` words=2849 chars=23309; `2-04-p2p-fuse-architecture.tex` words=6336 chars=50987; `2-05-evaluation.tex` words=1956 chars=14939; `3-conclusion.tex` words=790 chars=6578; `glossary.tex` words=248 chars=1987; `terms.tex` words=439 chars=3945. `./run-new.sh` завершился успешно; после пересборки точечный поиск по `diploma-latex-template/mablinov` не обнаружил `Llama` и standalone `Meta`
- Следующий рекомендуемый шаг: при необходимости аналогично синхронизировать версии `result/` и `final/` с обновлённой линейкой `DeepSeek`, чтобы во всех производных артефактах использовать единые примеры моделей

## 2026-06-22 04:38 — Уточнение примера топовой модели во введении `mablinov`

- Статус: выполнено
- Сгенерировано: во введении вместо перечисления нескольких крупных моделей оставлен только пример `DeepSeek V4 Pro`; формулировка скорректирована под терабайтный диапазон весов; PDF пересобран
- Файлы: `diploma-latex-template/mablinov/contents/1-introduction.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: `content/todo.md` — введение, подраздел «Актуальность темы»
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/1-introduction.tex`
- Ключевые решения: правка выполнена локально в одном предложении введения, без изменения остальной аргументации по росту размеров моделей. Чтобы фраза оставалась согласованной с выбранным примером `DeepSeek V4 Pro`, диапазон размеров уточнён с «сотен гигабайт» до терабайтного уровня.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/1-introduction.tex` — words=1255, chars=10569; в пределах лимита для введения. `./run-new.sh` завершился успешно.
- Следующий рекомендуемый шаг: при необходимости аналогично унифицировать точечные примеры моделей в других местах диплома, если требуется везде акцентировать именно `DeepSeek V4 Pro`

## 2026-06-22 04:45 — Добавление архитектурных схем в разделы `mablinov`

- Статус: выполнено
- Сгенерировано: схема исходного варианта с `storage-initializer + emptyDir` добавлена в раздел про NFS-этап, а схема целевой P2P/FUSE-архитектуры добавлена в вводную часть основного архитектурного раздела; после каждого рисунка включён аналитический абзац, связывающий изображение с текстом главы; PDF пересобран
- Файлы: `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: `content/todo.md` — раздел 3, пункт `6.1. Архитектура исходного решения storage-initializer + emptyDir`; раздел 4, пункт `7.1. Общая идея и требования к новой архитектуре`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/figures/arch_base.png`, `diploma-latex-template/mablinov/figures/arch_target.png`
- Ключевые решения: `arch_base.png` помещён сразу после описания жизненного цикла `emptyDir`, поскольку в этом месте требуется визуально зафиксировать локальный характер исходной схемы до перехода к разбору её ограничений. `arch_target.png` встроен в подраздел с общей идеей P2P/FUSE-архитектуры после описания трёх уровней системы, чтобы рисунок обобщал роли Redis, `storage-agent`, `storage-mounter`, UDS и межузлового P2P-обмена. По `.aux`-меткам итогового PDF рисунки зарегистрированы на страницах 45 и 61 соответственно.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex` — words=2902, chars=23735; `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex` — words=6408, chars=51581. `./run-new.sh` завершился успешно, `diploma-latex-template/mablinov/main.pdf` пересобран.
- Следующий рекомендуемый шаг: при необходимости аналогично добавить и согласовать в тексте другие отсутствующие схемы из плана, например иллюстрацию сценария конкуренции pod за `Lease`, если требуется усилить раздел о координации загрузок

## 2026-06-22 11:09 — Приведение подподзаголовков `mablinov` к нумерованной структуре

- Статус: выполнено
- Сгенерировано: во всех основных главах `mablinov` ненумерованные `\subsubsection*` заменены на нумерованные `\subsubsection`, чтобы подподзаголовки отображались как полноценные подпункты вида `3.1.1`, `4.3.1`, `5.3.1`; PDF пересобран
- Файлы: `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/main.toc`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: структурирование основной части диплома по иерархии разделов, подразделов и пунктов в соответствии с шаблоном `diploma` и логикой `content/todo.md`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/02-construction.sty`, `diploma-latex-template/diploma/styles/13-contents.sty`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`
- Ключевые решения: шаблон уже поддерживал нумерацию уровня `\subsubsection`, поэтому дополнительное изменение стилей не потребовалось; правка была выполнена на уровне содержимого глав. После пересборки в `main.toc` подтверждено появление записей `5.3.1`--`5.3.6` для подраздела «Расчётная модель задержки», а также аналогичной нумерации в разделах 3 и 4.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1250 chars=10523; `2-01-cold-start-problem.tex` words=3009 chars=23919; `2-02-existing-solutions.tex` words=3121 chars=26354; `2-03-nfs-stage.tex` words=2902 chars=23735; `2-04-p2p-fuse-architecture.tex` words=6408 chars=51581; `2-05-evaluation.tex` words=1956 chars=14939; `3-conclusion.tex` words=790 chars=6578; `glossary.tex` words=248 chars=1987; `terms.tex` words=439 chars=3945. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран.
- Следующий рекомендуемый шаг: при необходимости отдельно просмотреть обновлённое оглавление и решить, оставлять ли подробный уровень `\subsubsection` в содержании или сократить глубину `tocdepth`, сохранив нумерацию в тексте

## 2026-06-22 11:22 — Преобразование встроенных жирных абзацев в предзаголовки

- Статус: выполнено
- Сгенерировано: добавлен единый макрос `\predheading` для оформления предзаголовков; псевдо-подзаголовки в виде жирного начала абзаца вынесены на отдельную строку в разделах о требованиях, сравнении решений, ограничениях NFS, архитектуре P2P/FUSE, оценке эффективности и заключении; PDF пересобран
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/contents/3-conclusion.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: структурное и типографское выравнивание основного текста диплома в соответствии с иерархией разделов и академическим оформлением
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/contents/3-conclusion.tex`
- Ключевые решения: для единообразия введён локальный макрос `\predheading`, который оформляет короткий смысловой предзаголовок как отдельную жирную строку перед абзацем. Исправлены именно псевдо-подзаголовки типа `\textbf{... .}` и `\textbf{...:}`, где жирный фрагмент фактически открывал новый микроподраздел; встроенные термины внутри предложений и табличные ячейки не затрагивались. После правки повторный поиск по паттерну стартового жирного псевдо-заголовка не нашёл неоформленных остатков.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1250 chars=10523; `2-01-cold-start-problem.tex` words=3009 chars=23919; `2-02-existing-solutions.tex` words=3121 chars=26354; `2-03-nfs-stage.tex` words=2902 chars=23735; `2-04-p2p-fuse-architecture.tex` words=6408 chars=51579; `2-05-evaluation.tex` words=1956 chars=14939; `3-conclusion.tex` words=790 chars=6578; `glossary.tex` words=248 chars=1987; `terms.tex` words=439 chars=3945. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран.
- Следующий рекомендуемый шаг: при необходимости аналогично доработать встроенные определения-термины без точки в начале абзаца, если требуется ещё более жёстко унифицировать визуальную структуру текста

## 2026-06-22 11:27 — Преобразование обзоров Dragonfly, CubeFS и Rook/Ceph в нумерованные подпункты

- Статус: выполнено
- Сгенерировано: внутренние блоки `Архитектура`, `Применимость к ML-инференсу`, `Поддерживаемые протоколы`, `CephFS в Kubernetes` и `Ограничения` в подразделах `Dragonfly`, `CubeFS` и `Rook/Ceph` переведены из абзацных предзаголовков в нумерованные подпункты уровня `\paragraph`; PDF пересобран
- Файлы: `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: `content/todo.md` — раздел 2 «Анализ существующих решений для хранения и кэширования моделей», подпункт с обзором `Dragonfly`, `CubeFS` и `Rook/Ceph`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/02-construction.sty`, `diploma-latex-template/diploma/styles/13-contents.sty`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`
- Ключевые решения: сохранена текущая иерархия раздела, где сами системы остаются на уровне `\subsubsection`, а их внутренние смысловые блоки подняты на следующий нумеруемый уровень `\paragraph`. Это даёт настоящие подпункты в тексте без изменения общей структуры оглавления, поскольку `tocdepth` шаблона остаётся равным 3.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1250 chars=10523; `2-01-cold-start-problem.tex` words=3009 chars=23919; `2-02-existing-solutions.tex` words=3121 chars=26344; `2-03-nfs-stage.tex` words=2902 chars=23735; `2-04-p2p-fuse-architecture.tex` words=6408 chars=51579; `2-05-evaluation.tex` words=1956 chars=14939; `3-conclusion.tex` words=790 chars=6578; `glossary.tex` words=248 chars=1987; `terms.tex` words=439 chars=3945. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран.
- Следующий рекомендуемый шаг: при необходимости аналогично перевести в нумерованные подпункты и другие крупные обзорные микроблоки, где сейчас оставлены только абзацные `\predheading`

## 2026-06-22 11:49 — Локальная ГОСТ-корректировка оформления `mablinov`

- Статус: выполнено
- Сгенерировано: локально переопределены стили заголовков разделов и структурных элементов, подписей рисунков и таблиц, списка литературы и сносок; display-формулы приведены к нумерованному виду с расшифровкой обозначений; текст таблиц переведён на 12 pt с одинарным интервалом; диаграммы `chart_*` пересобраны в Times New Roman и заново подложены в PDF
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/contents/1-introduction.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `pptx/generate3.py`, `diploma-latex-template/mablinov/figures/chart_model_sizes.png`, `diploma-latex-template/mablinov/figures/chart_cold_start_breakdown.png`, `diploma-latex-template/mablinov/figures/chart_tmodel_ready.png`, `diploma-latex-template/mablinov/figures/chart_external_traffic.png`, `diploma-latex-template/mablinov/figures/chart_availability.png`, `diploma-latex-template/mablinov/figures/chart_reliability.png`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: финальная настройка оформления основной версии диплома в шаблоне `diploma-latex-template/mablinov` перед выпуском PDF
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/01-base.sty`, `diploma-latex-template/diploma/styles/02-construction.sty`, `diploma-latex-template/diploma/styles/05-figures.sty`, `diploma-latex-template/diploma/styles/06-tables.sty`, `diploma-latex-template/diploma/styles/16-references.sty`, `diploma-latex-template/mablinov/main.tex`, `pptx/generate3.py`
- Ключевые решения: общий шаблон `diploma` не изменялся; все ключевые типографские отклонения исправлены локально в `mablinov/main.tex`, чтобы не затронуть `example` и служебные документы. Для таблиц был введён отдельный макрос `\tablebodyfont`, позволяющий сохранить требуемые 12 pt и одинарный интервал без возврата к `\scriptsize`; после этого проблемные ячейки были вручную переразложены. Для шести диаграмм с исходным Python-скриптом синхронизированы шрифт и названия моделей, после чего PNG были обновлены в дипломе.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1264 chars=10656; `2-01-cold-start-problem.tex` words=3037 chars=24191; `2-02-existing-solutions.tex` words=3120 chars=26335; `2-03-nfs-stage.tex` words=2902 chars=23735; `2-04-p2p-fuse-architecture.tex` words=6456 chars=51991; `2-05-evaluation.tex` words=2042 chars=15721; `3-conclusion.tex` words=790 chars=6578; `glossary.tex` words=248 chars=1987; `terms.tex` words=439 chars=3945. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 110 страницах.
- Следующий рекомендуемый шаг: при необходимости отдельно пройтись по двум внешним растровым схемам `arch_base.png` и `arch_target.png`, если потребуется унифицировать и встроенный в них текст под те же типографские требования, что и у автоматически генерируемых диаграмм

## 2026-06-22 11:59 — Финальная ГОСТ-проверка `mablinov` с визуальной верификацией PDF

- Статус: выполнено
- Сгенерировано: оставшиеся внутренние обзорные блоки `Dragonfly`, `CubeFS` и `Rook/Ceph` переведены из `\paragraph` в предзаголовки `\predheading`; подписи рисунков и таблиц доведены до явных верхних и нижних отступов; для расчётных формул добавлены недостающие расшифровки обозначений; `main.pdf` пересобран и визуально проверен по рендеру страниц с рисунком, таблицами и списком литературы
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-check-a-021.png`, `tmp/pdfs/mablinov-check-a-022.png`, `tmp/pdfs/mablinov-check-b-044.png`, `tmp/pdfs/mablinov-check-c-111.png`, `tmp/pdfs/mablinov-check-c-112.png`
- Основание из плана: финальная типографская и структурная доводка основной версии диплома в каталоге `diploma-latex-template/mablinov`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/05-figures.sty`, `diploma-latex-template/diploma/styles/06-tables.sty`, `diploma-latex-template/diploma/styles/16-references.sty`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`
- Ключевые решения: общие стили шаблона `diploma` не менялись; все ГОСТ-правки оставлены локальными внутри `mablinov`. Визуальная проверка PNG-рендера подтвердила нужный формат: подрисуночная подпись идёт под рисунком слева и полужирно, заголовок таблицы выводится номером справа и названием с новой строки, список литературы печатается без абзацного отступа и в порядке упоминания.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1264 chars=10656; `2-01-cold-start-problem.tex` words=3044 chars=24280; `2-02-existing-solutions.tex` words=3120 chars=26345; `2-03-nfs-stage.tex` words=2902 chars=23735; `2-04-p2p-fuse-architecture.tex` words=6531 chars=52566; `2-05-evaluation.tex` words=2093 chars=16178; `3-conclusion.tex` words=790 chars=6578; `glossary.tex` words=248 chars=1987; `terms.tex` words=439 chars=3945. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 113 страницах.
- Следующий рекомендуемый шаг: при необходимости отдельно сократить объём разделов 2.4 и 2.5, если потребуется приблизить полную работу к нижней целевой границе по числу страниц

## 2026-06-22 12:14 — Добавление межстрочных разделителей во все таблицы `mablinov`

- Статус: выполнено
- Сгенерировано: во всех таблицах основной версии диплома, где строки данных шли без горизонтальных линий, добавлены межстрочные разделители `\hline` после каждой строки; итоговый PDF пересобран
- Файлы: `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/main.pdf`
- Основание из плана: финальная унификация оформления таблиц в основной версии диплома перед выпуском PDF
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`
- Ключевые решения: таблицы, в которых `\hline` уже был проставлен после каждой строки, оставлены без изменений; правка внесена только в те места, где были верхняя и нижняя границы, но отсутствовали внутренние строковые разделители. Это позволило сохранить текущую ширину колонок и не менять общий стиль шаблона `diploma`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents` — `0-abstract.tex` words=233 chars=2113; `1-introduction.tex` words=1264 chars=10656; `2-01-cold-start-problem.tex` words=3044 chars=24280; `2-02-existing-solutions.tex` words=3120 chars=26345; `2-03-nfs-stage.tex` words=2902 chars=23735; `2-04-p2p-fuse-architecture.tex` words=6531 chars=52566; `2-05-evaluation.tex` words=2093 chars=16178; `3-conclusion.tex` words=790 chars=6578; `glossary.tex` words=248 chars=1987; `terms.tex` words=439 chars=3945. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 113 страницах.
- Следующий рекомендуемый шаг: при необходимости отдельно пройтись по двум небольшим предупреждениям `Overfull \hbox` в таблицах, если потребуется полностью зачистить лог сборки

## 2026-06-22 12:22 — Выравнивание строк в таблице 3

- Статус: выполнено
- Сгенерировано: для таблицы 3 включено вертикальное центрирование строк через локальное переопределение `\tabularxcolumn` на `m{#1}` и перевод первой колонки с `p{31mm}` на `m{31mm}`; `main.pdf` пересобран и визуально проверен по странице с таблицей 3
- Файлы: `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-table3-fixed-044.png`
- Основание из плана: точечная типографская доводка сравнительной таблицы раздела 2 для согласованного отображения критериев и значений
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`
- Ключевые решения: проблема была не в ширине колонок, а в разном вертикальном выравнивании ячеек: левая колонка использовала верхнее выравнивание `p`, а соседние многострочные значения визуально центрировались. Локальный переход этой таблицы на `m`-колонки выровнял критерии и значения по высоте, не затрагивая остальные таблицы диплома.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex` — words=3123 chars=26354. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 113 страницах; визуальная проверка PNG-рендера страницы 44 подтвердила выравнивание таблицы 3.
- Следующий рекомендуемый шаг: при необходимости аналогично перевести на `m`-колонки и другие таблицы, если потребуется добиться одинакового вертикального центрирования по всему документу

## 2026-06-22 12:44 — Доводка таблиц 1 и 4

- Статус: выполнено
- Сгенерировано: таблица 1 приведена к тому же вертикальному выравниванию, что и таблица 3; таблица 4 переведена на `m`-колонки и `X`-распределение ширины для корректного переноса длинных значений без выхода за границы страницы; `main.pdf` пересобран и визуально проверен по страницам 22 и 73
- Файлы: `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-table1-check-022.png`, `tmp/pdfs/mablinov-table4-check-073.png`
- Основание из плана: финальная типографская унификация таблиц в основной версии диплома `diploma-latex-template/mablinov`
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex`, `diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex`
- Ключевые решения: для таблицы 1 применён тот же локальный приём, что и в таблице 3: `\tabularxcolumn` переопределён на `m{#1}`, а фиксированные колонки переведены с `p` на `m` для равномерного вертикального центрирования. Для таблицы 4 дополнительно заменены три правые фиксированные колонки на `X`, чтобы длинные ячейки переносились внутри доступной ширины и не ломали полосу набора.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-01-cold-start-problem.tex` — words=3047 chars=24289; `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-04-p2p-fuse-architecture.tex` — words=6531 chars=52557. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 112 страницах; визуальная проверка PNG-рендера страниц 22 и 73 подтвердила корректную верстку таблиц 1 и 4.
- Следующий рекомендуемый шаг: при необходимости аналогично дочистить оставшиеся мелкие предупреждения `Overfull \hbox` в логах, если потребуется полностью выровнять типографику без предупреждений компилятора

## 2026-06-22 12:48 — Добавление схемы NFS-архитектуры в раздел 3

- Статус: выполнено
- Сгенерировано: схема `arch_nfs.png` встроена в подраздел о переходе к NFS как общему RWX-хранилищу; добавлены подпись и аналитический абзац, связывающий рисунок с устранением повторных загрузок и последующим разбором `flock`; `main.pdf` пересобран и визуально проверен по странице с новым рисунком
- Файлы: `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-arch-nfs-page-052.png`
- Основание из плана: `content/todo.md` — раздел 3 «Промежуточное решение на базе NFS и координации загрузок», подпункты о NFS как общем хранилище и координации первой записи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex`, `diploma-latex-template/mablinov/figures/arch_nfs.png`
- Ключевые решения: рисунок размещён сразу после объяснения того, что при масштабировании загрузка из внешнего источника выполняется один раз, поскольку именно здесь схема наиболее наглядно связывает `storage-initializer`, общий NFS-том и повторное чтение runtime-контейнером. Для более чистой посадки изображения в PDF использована локальная обрезка `trim`, чтобы убрать лишние внешние поля PNG без изменения самого файла.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-03-nfs-stage.tex` — words=2981 chars=24317. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 112 страницах; по `.aux`-метке рисунок `fig:arch-nfs-shared` размещён на странице 52 и визуально подтверждён PNG-рендером.
- Следующий рекомендуемый шаг: при необходимости аналогично пройтись по другим внешним схемам и локально подстроить `trim`/ширину, если потребуется ещё более единая визуальная плотность всех архитектурных рисунков

## 2026-06-22 13:55 — Добавление двух графиков масштабирования загрузки в раздел 5

- Статус: выполнено
- Сгенерировано: для раздела оценки добавлены два новых графика — зависимость времени подготовки burst-пакета реплик от числа одновременно стартующих pod и зависимость совокупной скорости загрузки от числа реплик; диаграммы сгенерированы в том же стиле, что и существующие `chart_*`, встроены в раздел `2-05-evaluation`, `main.pdf` пересобран и визуально проверен по страницам с новыми рисунками
- Файлы: `pptx/generate3.py`, `pptx/charts/chart_loading_time_replicas.png`, `pptx/charts/chart_loading_speed_replicas.png`, `diploma-latex-template/mablinov/figures/chart_loading_time_replicas.png`, `diploma-latex-template/mablinov/figures/chart_loading_speed_replicas.png`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-loading-charts-102.png`, `tmp/pdfs/mablinov-loading-charts-103.png`
- Основание из плана: `content/todo.md` — раздел 5 «Оценка эффективности и надёжности предложенного подхода», блок сравнения сценариев и burst-масштабирования
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `pptx/generate3.py`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`
- Ключевые решения: новые графики построены для warm burst-scale-out сценария после предварительного появления модели в кластере, чтобы показать разницу не только по внешнему трафику, но и по масштабированию data plane. Время показано как wall-clock до готовности всего пакета реплик, а скорость — как совокупная скорость подготовки всех реплик, что позволяет наглядно сравнить насыщение NFS одним 10GbE-сервером и fan-out эффект P2P/FUSE.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-05-evaluation.tex` — words=2281 chars=17648. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 113 страницах; по `.aux`-меткам рисунки `fig:loading_time_replicas` и `fig:loading_speed_replicas` размещены на страницах 102 и 103 и визуально подтверждены PNG-рендером.
- Следующий рекомендуемый шаг: при необходимости аналогично добавить в раздел 5 ещё одну диаграмму по `T_first_byte` для burst-сценария, если потребуется отдельно визуализировать преимущество lazy loading относительно полного времени готовности

## 2026-06-22 14:02 — Доводка читаемости подписей на графиках burst-scale-out

- Статус: выполнено
- Сгенерировано: на двух графиках burst-scale-out перенесены проблемные аннотации в свободные зоны поля, для подписи про лимит `≈ 1.25 ГБ/с` добавлена белая подложка и стрелка; PNG пересозданы, встроенные копии в `mablinov/figures` обновлены, итоговый `main.pdf` пересобран и визуально перепроверен по страницам 102–103
- Файлы: `pptx/generate3.py`, `pptx/charts/chart_loading_time_replicas.png`, `pptx/charts/chart_loading_speed_replicas.png`, `diploma-latex-template/mablinov/figures/chart_loading_time_replicas.png`, `diploma-latex-template/mablinov/figures/chart_loading_speed_replicas.png`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-loading-charts-102.png`, `tmp/pdfs/mablinov-loading-charts-103.png`
- Основание из плана: `content/todo.md` — раздел 5 «Оценка эффективности и надёжности предложенного подхода», блок визуального сравнения сценариев burst-масштабирования
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `pptx/generate3.py`, `tmp/pdfs/mablinov-loading-charts-102.png`, `tmp/pdfs/mablinov-loading-charts-103.png`
- Ключевые решения: данные графиков не менялись; правка ограничена позиционированием и оформлением поясняющих надписей, чтобы они не накладывались на линии и маркеры. Для финальной проверки использован повторный PNG-рендер уже собранных PDF-страниц, а не только исходных изображений графиков.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-05-evaluation.tex` — words=2281 chars=17648, текст раздела не изменялся. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 113 страницах; визуальная проверка PNG-рендера страниц 102 и 103 подтвердила отсутствие перекрытия подписей с графиками.
- Следующий рекомендуемый шаг: при необходимости аналогично пройтись по остальным диаграммам презентационного набора и выровнять стиль аннотаций, если появятся ещё точечные замечания по читаемости

## 2026-06-22 15:12 — Добавление диаграммы деградации inference для классической emptyDir-схемы

- Статус: выполнено
- Сгенерировано: добавлена новая диаграмма, показывающая, сколько новых реплик остаётся недоступно во времени при burst-старте в классической схеме `emptyDir + storage-initializer`; рисунок встроен в раздел `2-05-evaluation` перед сравнительными burst-графиками, итоговый `main.pdf` пересобран и визуально проверен по страницам 102–103
- Файлы: `pptx/generate3.py`, `pptx/charts/chart_emptydir_burst_degradation.png`, `diploma-latex-template/mablinov/figures/chart_emptydir_burst_degradation.png`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-burst-degradation-102.png`, `tmp/pdfs/mablinov-burst-degradation-103.png`
- Основание из плана: `content/todo.md` — раздел 5 «Оценка эффективности и надёжности предложенного подхода», подпункт `8.4` про сравнение подходов в burst-сценарии
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `pptx/generate3.py`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`
- Ключевые решения: вместо ещё одного графика времени загрузки выбрана диаграмма недоступных новых реплик во времени, поскольку она напрямую показывает пользовательский эффект baseline-архитектуры: до завершения `storage-initializer` runtime не стартует и inference-мощность новых pod равна нулю. Для наглядности использованы representative burst-случаи `N = 1, 4, 8, 10`, а в подписи зафиксирован наиболее показательный сценарий `N = 10` с окном полной недоступности более 100 секунд.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/2-05-evaluation.tex` — words=2395 chars=18579. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 114 страницах; по `.aux`-метке новый рисунок `fig:emptydir_burst_degradation` размещён на странице 102, визуальная проверка PNG-рендера подтвердила корректную посадку графика и подписи.
- Следующий рекомендуемый шаг: при необходимости аналогично добавить рядом короткую диаграмму `T_first_byte` для burst-сценария, если потребуется отдельно показать, что у baseline отсутствует частичная готовность, а у FUSE она появляется уже в первые секунды

## 2026-06-22 15:16 — Упрощение burst-графика для слайда о проблемах cold start

- Статус: выполнено
- Сгенерировано: диаграмма `chart_emptydir_burst_degradation` переделана в более простую slide-friendly форму — без внутренних текстовых выносок, без заголовка внутри изображения и без легенды; вместо ступенчатых кривых использован компактный горизонтальный bar chart с прямыми подписями значений
- Файлы: `pptx/generate3.py`, `pptx/charts/chart_emptydir_burst_degradation.png`, `pptx/final-pptx-v2.pptx`, `diploma-latex-template/mablinov/figures/chart_emptydir_burst_degradation.png`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/mablinov-burst-degradation-simple-102.png`
- Основание из плана: `pptx/todo.md` — блок слайда об исходной архитектуре и проблемах cold start в serverless ML inference
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `pptx/generate3.py`
- Ключевые решения: график теперь показывает только главную мысль для устного комментария на слайде — длительность окна полной недоступности новых реплик при burst-старте. Смысловая нагрузка перенесена из самой картинки в простую шкалу и числовые подписи, чтобы изображение не конкурировало с текстом выступления.
- Проверка объёма: текстовые файлы диплома не изменялись, повторная проверка `report_stats.py` не требовалась. `./run-new.sh` завершился успешно, итоговый `main.pdf` собран на 114 страницах; визуальная проверка PNG-рендера страницы 102 подтвердила корректную посадку упрощённого графика.
- Следующий рекомендуемый шаг: при необходимости можно сделать вторую, ещё более презентационную версию этого же сюжета в формате таймлайна с иконками pod/runtime, не затрагивая дипломную версию рисунка

## 2026-06-22 15:31 — Подготовка рецензии рецензента и сборки review.pdf

- Статус: выполнено
- Сгенерировано: создан файл `reviewer_review.md` с итоговым текстом рецензии на одну страницу; на основе шаблона `example/review.tex` подготовлен `diploma-latex-template/mablinov/review.tex`, в `info.tex` добавлены данные рецензента, а в `run-new.sh` включена сборка `review.pdf` вместе с основным дипломом
- Файлы: `reviewer_review.md`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/info.tex`, `run-new.sh`, `diploma-latex-template/mablinov/review.pdf`, `tmp/pdfs/review.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальный комплект материалов для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/example/review.tex`, `diploma-latex-template/example/consultant_review.tex`, `diploma-latex-template/diploma/review.sty`
- Ключевые решения: текст рецензии переписан под тему диплома про cold start и распределённый кэш моделей, при этом сокращён до объёма, который стабильно помещается на один лист без изменения стилей шаблона. Для LaTeX-версии сохранён шаблонный ГОСТ-совместимый каркас, а ужатие выполнено только за счёт компактного текста и локальной настройки интервалов в `review.tex`.
- Проверка объёма: `python3 scripts/report_stats.py reviewer_review.md diploma-latex-template/mablinov/review.tex` — `reviewer_review.md`: words=166 chars=1508, `review.tex`: words=160 chars=1472. `./run-new.sh` завершился успешно; `review.log` содержит `Output written on review.xdv (1 page, 25084 bytes)`, а PNG-превью `tmp/pdfs/review.pdf.png` визуально подтвердило корректную одностраничную вёрстку.
- Следующий рекомендуемый шаг: при необходимости аналогично подготовить в `mablinov` отдельные PDF для отзыва руководителя и отзыва консультанта, чтобы весь комплект сопроводительных документов собирался одной командой

## 2026-06-22 18:14 — Локальная правка шапки review.tex

- Статус: выполнено
- Сгенерировано: в `review.tex` локально переопределены макросы шапки рецензии так, чтобы строка рецензента выводилась в одну строку вместе с должностью, а блок аффилиации повторял исходный вид диплома с отдельной строкой `806` без подписи `Образовательный центр`
- Файлы: `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/review.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная доводка комплекта для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/review.sty`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/info.tex`
- Ключевые решения: глобальные стили шаблона не менялись; правка выполнена только локальными `\renewcommand` внутри `review.tex`, чтобы не затронуть основную сборку диплома и другие служебные документы. Для блока аффилиации сохранён визуальный паттерн исходной версии: сначала строка института, затем отдельная строка с номером `806`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/review.tex` — words=259 chars=2343, что укладывается в лимит для 2 страниц. `./run-new.sh` завершился успешно; `review.log` содержит `Output written on review.xdv (2 pages, 32016 bytes)`, а PNG-превью `tmp/pdfs/review.pdf.png` визуально подтвердило, что строка рецензента не разбита, а `806` отображается без поля `Образовательный центр`.
- Следующий рекомендуемый шаг: при необходимости аналогично локально подправить `consultant_review.tex` и другие сопроводительные документы, если требуется единый вид всех служебных форм

## 2026-06-22 18:18 — Синхронизация блока «Образовательный центр» в review.tex с main.pdf

- Статус: выполнено
- Сгенерировано: в `review.tex` строка аффилиации возвращена к тому же виду, что и в `main.pdf`: `Институт (Филиал)` и отдельная строка `Образовательный центр № 806`; `review.pdf` пересобран и визуально сверен с титульной страницей основного диплома
- Файлы: `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/review.pdf`, `tmp/pdfs/review.pdf.png`, `tmp/pdfs/main.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная унификация с основным комплектом
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`
- Ключевые решения: вместо отдельной интерпретации шапки использована та же формула строки, что и в `main.tex`, а итог проверен не только по коду, но и по PNG-превью первого листа `main.pdf`. Это позволило точно повторить визуальную структуру исходного диплома в рецензии.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/review.tex` — words=262 chars=2371, что укладывается в лимит для 2 страниц. Сборка `review.tex` завершилась успешно; `review.log` содержит `Output written on review.xdv (2 pages, 32236 bytes)`, а визуальная проверка `tmp/pdfs/review.pdf.png` и `tmp/pdfs/main.pdf.png` подтвердила совпадение блока `Образовательный центр № 806`.
- Следующий рекомендуемый шаг: при необходимости так же синхронизировать подписи и блоки аффилиации в остальных служебных документах, если они должны повторять титульный стиль `main.pdf`

## 2026-06-22 18:30 — Добавление отзыва научного руководителя

- Статус: выполнено
- Сгенерировано: создан файл `diploma-latex-template/mablinov/supervisor_review.tex` по образцу `example/supervisor_review.tex`; текст отзыва руководителя написан на основе рецензии, но расширен и переформулирован под позицию научного руководителя. В `run-new.sh` добавлена сборка и очистка `supervisor_review.tex`, а итоговый `supervisor_review.pdf` успешно сгенерирован
- Файлы: `diploma-latex-template/mablinov/supervisor_review.tex`, `run-new.sh`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `tmp/pdfs/supervisor_review.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и полный комплект материалов для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/example/supervisor_review.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/info.tex`
- Ключевые решения: оформление `supervisor_review.tex` синхронизировано с текущими локальными правками `review.tex`, включая блок `Образовательный центр № 806` и шапку в стиле `main.pdf`. Для строки руководителя использован локальный вариант без `supervisorCredentials`, чтобы при пустом поле не появлялись лишние знаки препинания и переносы.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/supervisor_review.tex` — words=415 chars=3726, что укладывается в лимит для 2 страниц. Полная сборка `./run-new.sh` завершилась успешно; `supervisor_review.log` содержит `Output written on supervisor_review.xdv (2 pages, 45372 bytes)`, а PNG-превью `tmp/pdfs/supervisor_review.pdf.png` визуально подтвердило корректную двухстраничную вёрстку.
- Следующий рекомендуемый шаг: при необходимости аналогично добавить и унифицировать остальные служебные документы (`consultant_review.tex`, задание, титульные формы), чтобы весь комплект собирался одной командой в едином стиле

## 2026-06-22 18:40 — Доводка отзыва руководителя и шапки аффилиации

- Статус: выполнено
- Сгенерировано: в `supervisor_review.tex` возвращена строка `Работа проверена на объем заимствования. % заимствования – %`, сам отзыв руководителя переписан в виде одного сплошного текста без подразделов, а в локальных переопределениях `makeAffiliations` для `main.tex`, `review.tex` и `supervisor_review.tex` заменены растягиваемые пробелы на неразрывные в строках `Институт~(Филиал)` и `Образовательный~центр~№`
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/main.pdf`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `tmp/pdfs/main.pdf.png`, `tmp/pdfs/supervisor_review.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная типографская унификация служебных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`
- Ключевые решения: строка про объём заимствований вынесена в отдельный абзац, чтобы она не сливалась со строкой руководителя; отзыв оставлен цельным без подзаголовков и маркированных блоков. Для уменьшения неестественного растяжения текста в шапке использованы неразрывные пробелы, что улучшило визуальное соответствие титульному оформлению без изменения общей структуры шаблона.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/main.tex diploma-latex-template/mablinov/review.tex diploma-latex-template/mablinov/supervisor_review.tex` — `main.tex`: words=133 chars=1230, `review.tex`: words=262 chars=2377, `supervisor_review.tex`: words=394 chars=3514. `./run-new.sh` завершился успешно; `supervisor_review.log` содержит `Output written on supervisor_review.xdv (2 pages, 43820 bytes)`, а свежие PNG-превью `tmp/pdfs/main.pdf.png` и `tmp/pdfs/supervisor_review.pdf.png` визуально подтвердили отдельную строку про заимствования и уменьшение растяжения в `Институт~(Филиал)`.
- Следующий рекомендуемый шаг: при необходимости тем же приёмом можно локально убрать растягивание и в других многострочных служебных полях вроде `Наименование темы`, если захочется полностью выровнять типографику титульных документов

## 2026-06-22 18:46 — Устранение растягивания строк в шапке

- Статус: выполнено
- Сгенерировано: в локальных переопределениях `makeAffiliations` для `main.tex`, `review.tex` и `supervisor_review.tex` блок аффилиации переведён в `\raggedright`, чтобы LaTeX перестал растягивать пробелы в строках `Институт (Филиал)` и `Направление подготовки`; после этого весь комплект PDF пересобран
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/main.pdf`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `tmp/pdfs/main.pdf.png`, `tmp/pdfs/supervisor_review.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная типографская доводка титульных и отзывных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`
- Ключевые решения: источник дефекта был не в самих словах, а в полном выравнивании абзаца, из-за которого TeX искусственно расширял интервалы между словами в коротких строках шапки. Исправление выполнено локально и не затронуло глобальные стили шаблона.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/main.tex diploma-latex-template/mablinov/review.tex diploma-latex-template/mablinov/supervisor_review.tex` — `main.tex`: words=133 chars=1230, `review.tex`: words=262 chars=2377, `supervisor_review.tex`: words=394 chars=3514. `./run-new.sh` завершился успешно; `main.log` содержит `Output written on main.xdv (114 pages, 2141872 bytes)`, `supervisor_review.log` содержит `Output written on supervisor_review.xdv (2 pages, 43816 bytes)`, а свежие PNG-превью `tmp/pdfs/main.pdf.png` и `tmp/pdfs/supervisor_review.pdf.png` визуально подтвердили, что строки шапки больше не растягиваются.
- Следующий рекомендуемый шаг: при необходимости аналогично локально отключить растягивание в других служебных строках, если появятся похожие артефакты в заданиях или дополнительных отзывах

## 2026-06-22 18:53 — Доводка длины подчёркиваний в шапке

- Статус: выполнено
- Сгенерировано: в локальных переопределениях `makeAffiliations` для `main.tex`, `review.tex` и `supervisor_review.tex` добавлено вычисление остатка ширины строки для полей `Институт (Филиал)`, `Образовательный центр №` и `Группа`, а поле `Направление подготовки` вынесено на отдельную строку с корректным переносом и подчёркиванием до правого края
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/main.pdf`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `tmp/pdfs/main.pdf.png`, `tmp/pdfs/supervisor_review.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная типографская доводка титульных и отзывных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`
- Ключевые решения: для коротких полей использован локальный макрос с вычислением доступной ширины строки, что позволило протянуть линию до правого поля без возврата к растягиванию пробелов. Для длинного поля `Направление подготовки` применён перенос на следующую строку внутри подчёркивания, чтобы сохранить читаемость и не выпускать текст за границу страницы.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/main.tex diploma-latex-template/mablinov/review.tex diploma-latex-template/mablinov/supervisor_review.tex` — `main.tex`: words=140 chars=1278, `review.tex`: words=269 chars=2425, `supervisor_review.tex`: words=401 chars=3562. `./run-new.sh` завершился успешно; `main.log` содержит `Output written on main.xdv (114 pages, 2141936 bytes)`, `supervisor_review.log` содержит `Output written on supervisor_review.xdv (2 pages, 43892 bytes)`, а свежие PNG-превью `tmp/pdfs/main.pdf.png` и `tmp/pdfs/supervisor_review.pdf.png` визуально подтвердили, что линии в шапке доходят до правого края и не выходят за пределы страницы.
- Следующий рекомендуемый шаг: при необходимости тем же способом можно выровнять и остальные длинные поля служебных форм, например `Наименование темы`

## 2026-06-22 19:05 — Уплотнение шапки и возврат полей в одну строку

- Статус: выполнено
- Сгенерировано: в `makeAffiliations` для `main.tex`, `review.tex` и `supervisor_review.tex` убраны избыточные вертикальные интервалы между полями, `Группа` и `Направление подготовки` снова сведены в одну первую строку, а `Профиль` возвращён к более компактному виду без большого горизонтального разрыва после заголовка
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/main.pdf`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `tmp/pdfs/main.pdf.png`, `tmp/pdfs/supervisor_review.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная типографская доводка титульных и отзывных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`
- Ключевые решения: табличная вёрстка была заменена на обычные строки с локальным `hangindent` для блока `Группа + Направление подготовки`, потому что это позволило одновременно убрать лишние интервалы, сохранить первую строку общей и не выпускать длинное значение специальности за правое поле. Для остальных полей использована компактная строковая запись с подчёркиванием до края строки.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/main.tex diploma-latex-template/mablinov/review.tex diploma-latex-template/mablinov/supervisor_review.tex` — `main.tex`: words=140 chars=1273, `review.tex`: words=269 chars=2420, `supervisor_review.tex`: words=401 chars=3557. `./run-new.sh` завершился успешно; `main.log` содержит `Output written on main.xdv (114 pages, 2142064 bytes)`, `review.log` содержит `Output written on review.xdv (2 pages, 32440 bytes)`, `supervisor_review.log` содержит `Output written on supervisor_review.xdv (2 pages, 44008 bytes)`, а свежие PNG-превью `tmp/pdfs/main.pdf.png` и `tmp/pdfs/supervisor_review.pdf.png` визуально подтвердили компактную шапку и корректный перенос длинного значения специальности.
- Следующий рекомендуемый шаг: при необходимости тем же приёмом можно локально уплотнить и поле `Наименование темы`, если захочется ещё сильнее приблизить служебные формы к виду титульника

## 2026-06-22 19:13 — Коррекция переноса направления подготовки в шапке

- Статус: выполнено
- Сгенерировано: в локальных переопределениях `makeAffiliations` для `main.tex`, `review.tex` и `supervisor_review.tex` убран `hangindent` у общей строки `Группа + Направление подготовки`, чтобы первая строка сохраняла оба поля вместе, а продолжение длинного значения специальности переносилось только по факту нехватки места и начиналось от левого края блока, а не под кодом `02.04.02`
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/main.pdf`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `tmp/pdfs/main.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная типографская доводка титульных и отзывных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`
- Ключевые решения: сохранена компактная однострочная подача полей `Группа` и `Направление подготовки`, но логика подвешенного отступа удалена, поскольку именно она визуально привязывала перенос к значению `02.04.02`. Новый вариант лучше соответствует требованию: на новой строке оказывается только неуместившийся хвост длинного названия направления.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/main.tex diploma-latex-template/mablinov/review.tex diploma-latex-template/mablinov/supervisor_review.tex` — `main.tex`: words=134 chars=1224, `review.tex`: words=263 chars=2371, `supervisor_review.tex`: words=395 chars=3508. `./run-new.sh` завершился успешно; `main.log` содержит `Output written on main.xdv (114 pages, 2142060 bytes)`, `review.log` содержит `Output written on review.xdv (2 pages, 32432 bytes)`, `supervisor_review.log` содержит `Output written on supervisor_review.xdv (2 pages, 44000 bytes)`, а свежее превью `tmp/pdfs/main.pdf.png` визуально подтвердило перенос `информатика и информационные технологии` под блок `Группа`, а не под `02.04.02`.
- Следующий рекомендуемый шаг: если потребуется ещё точнее приблизить шапку к эталонному макету, можно аналогично локально отрегулировать переносы для длинных тем и наименований в служебных формах

## 2026-06-22 19:27 — Доводка подчёркивания направления подготовки в main.pdf

- Статус: выполнено
- Сгенерировано: в локальном переопределении `makeAffiliations` для `main.tex` отключено `\raggedright` только на титульнике, а подпись `Направление подготовки` зафиксирована как единый блок, чтобы первая строка поля в `main.pdf` снова доходила подчёркиванием до правого края без изменения уже согласованных `review.tex` и `supervisor_review.tex`
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/main.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная типографская доводка титульных и отзывных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/main.tex`
- Ключевые решения: проблема проявлялась только на титульном листе основной работы, поэтому исправление локализовано в `main.tex` и не затрагивает отзывы. Возврат обычного выравнивания для блока аффилиации позволил дотянуть многострочное подчёркивание до правого края, а фиксация ярлыка `Направление подготовки` как единого фрагмента не дала распасться подписи при перераспределении строки.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/main.tex` — `main.tex`: words=134 chars=1224. `./run-new.sh` завершился успешно; `main.log` содержит `Output written on main.xdv (114 pages, 2142068 bytes)`, а обновлённое превью `tmp/pdfs/main.pdf.png` визуально подтвердило, что строка с направлением подготовки в `main.pdf` теперь доходит до правого края.
- Следующий рекомендуемый шаг: если захочется окончательно унифицировать поведение многострочных подчёркиваний между титульником и отзывами, можно тем же локальным способом отдельно довести и шапки review-документов

## 2026-06-22 19:33 — Перенос task.tex и подключение его к сборке

- Статус: выполнено
- Сгенерировано: файл `task.tex` перенесён в каталог `diploma-latex-template/mablinov` на основе `diploma-latex-template/example/task.tex`, адаптирован под текущие поля `info.tex` и существующую библиографию, а `run-new.sh` расширен так, чтобы собирать и проверять `task.pdf` вместе с `main.pdf`, `review.pdf` и `supervisor_review.pdf`
- Файлы: `diploma-latex-template/mablinov/task.tex`, `run-new.sh`, `diploma-latex-template/mablinov/task.pdf`, `tmp/pdfs/task.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и полный комплект материалов для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/example/task.tex`, `diploma-latex-template/mablinov/info.tex`, `diploma-latex-template/mablinov/main.bib`, `diploma-latex-template/diploma/task.sty`, `run-new.sh`
- Ключевые решения: в локальной копии задания сохранена структура эталонного файла, но добавлены переопределения для шапки и строки руководителя, чтобы документ корректно использовал текущие реквизиты `mablinov` и не выводил пустые служебные поля. Для раздела с исходными материалами использованы уже существующие записи из `main.bib`, что позволило собрать `task.pdf` без недостающих ссылок.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/task.tex` — `task.tex`: words=143 chars=1221. `./run-new.sh` завершился успешно; сформированы `main.pdf`, `review.pdf`, `supervisor_review.pdf` и `task.pdf`, а свежее превью `tmp/pdfs/task.pdf.png` визуально подтвердило корректную первую страницу задания.
- Следующий рекомендуемый шаг: если потребуется, можно следующим проходом убрать красные примерные поля из `task.tex` и заполнить задание фактическими сроками, этапами и исходными данными по вашей ВКР

## 2026-06-22 19:43 — Заполнение календарного плана в task.tex

- Статус: выполнено
- Сгенерировано: в таблице раздела 4 файла `task.tex` заполнен календарный план из семи этапов с реалистичными задачами по теме ВКР, датами от `02.09.2024` до `24.05.2026` и распределением трудоёмкости, суммарно дающим 100\%; дополнительно синхронизирована строка `Дата выдачи задания` с началом графика
- Файлы: `diploma-latex-template/mablinov/task.tex`, `diploma-latex-template/mablinov/task.pdf`, `tmp/pdfs/task.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и полный комплект материалов для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/task.tex`
- Ключевые решения: этапы подобраны так, чтобы отражать фактическую логику работы над дипломом: от анализа литературы и постановки требований через NFS-этап и проектирование целевой архитектуры к реализации компонентов `storage-agent` и `storage-mounter`, затем к нагрузочному тестированию и оформлению ВКР. Даты заданы абсолютными значениями, чтобы документ не зависел от года сборки и оставался внутренне непротиворечивым.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/task.tex` — `task.tex`: words=201 chars=1699. `./run-new.sh` завершился успешно; обновлённый `task.pdf` собран без ошибок, `task.log` содержит `Output written on task.xdv (2 pages, 33440 bytes)`, а свежее превью `tmp/pdfs/task.pdf.png` подтверждает корректную первую страницу после правки.
- Следующий рекомендуемый шаг: при необходимости можно следующим проходом заполнить и оставшиеся красные шаблонные поля в `task.tex`, например исходные данные к работе и количество листов раздаточного материала

## 2026-06-22 19:52 — Специализация task.pdf и разбивка по презентации

- Статус: выполнено
- Сгенерировано: в `task.tex` добавлена локальная переустановка группы `М8О-109СВ-24` только для `task.pdf`, строка `Образовательный центр №` заменена на `Кафедра`, вместо заглушки вписан содержательный блок `Задание и исходные данные к работе`, а таблица иллюстративно-графических материалов заполнена по фактической структуре `pptx/pptx.pptx` после разбора 17 слайдов презентации
- Файлы: `diploma-latex-template/mablinov/task.tex`, `diploma-latex-template/mablinov/task.pdf`, `tmp/pdfs/fresh/task-check-1952.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и полный комплект материалов для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/task.tex`, `pptx/pptx.pptx`
- Ключевые решения: презентация была разобрана по текстовому наполнению слайдов, после чего 17 слайдов сведены в укрупнённые блоки для таблицы: титульный слайд, актуальность, цель и задачи, исходная архитектура, существующие решения, требования, технологии, архитектура решения, экспериментальное сравнение и итоговые выводы. Локальная подмена группы и кафедры выполнена только в `task.tex`, поэтому остальные документы комплекта не затронуты.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/task.tex` — `task.tex`: words=317 chars=2701. `./run-new.sh` завершился успешно; `task.log` содержит `Output written on task.xdv (3 pages, 43772 bytes)`. Для обхода кэша Quick Look создано свежее превью `tmp/pdfs/fresh/task-check-1952.pdf.png`, которое визуально подтвердило строку `Кафедра 806`, группу `М8О-109СВ-24` и замену заглушки на содержательный текст задания.
- Следующий рекомендуемый шаг: при необходимости можно следующей правкой уменьшить объём первого блока `Задание и исходные данные к работе`, если захочется вернуть `task.pdf` к более компактной двухстраничной форме

## 2026-06-22 23:22 — Замена типа учреждения только в task.pdf

- Статус: выполнено
- Сгенерировано: в `task.tex` локально переопределён `\makeHeader`, чтобы только в `task.pdf` строка `ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ АВТОНОМНОЕ` была заменена на `ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ`
- Файлы: `diploma-latex-template/mablinov/task.tex`, `diploma-latex-template/mablinov/task.pdf`, `tmp/pdfs/fresh3/task-budgetary-check.pdf.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и полный комплект материалов для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/task.tex`
- Ключевые решения: изменение внесено через локальное переопределение шапки внутри `task.tex`, поэтому `main.pdf`, `review.pdf` и `supervisor_review.pdf` сохраняют прежнюю формулировку. Для проверки использовано свежее превью с новым именем файла, чтобы исключить влияние кэша Quick Look.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/task.tex` — `task.tex`: words=350 chars=3033. `./run-new.sh` завершился успешно; `task.log` содержит `Output written on task.xdv (3 pages, 43760 bytes)`, а `tmp/pdfs/fresh3/task-budgetary-check.pdf.png` визуально подтвердило появление слова `БЮДЖЕТНОЕ` в шапке.
- Следующий рекомендуемый шаг: при необходимости можно тем же локальным способом скорректировать и другие служебные строки только для `task.pdf`, не затрагивая остальной комплект документов

## 2026-06-22 23:46 — Перенос подчеркивания на текст пункта задания в task.pdf

- Статус: выполнено
- Сгенерировано: в `task.tex` снято подчеркивание с заголовка `ЗАДАНИЕ` и со слова `Задание` в названии пункта 3; подчеркивание перенесено на сам текст раздела `Задание и исходные данные к работе`
- Файлы: `diploma-latex-template/mablinov/task.tex`, `diploma-latex-template/mablinov/task.pdf`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная доводка служебных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/task.tex`
- Ключевые решения: правка выполнена точечно, без изменения структуры документа: заголовки вернулись к обычному виду, а смысловое подчеркивание перенесено на содержательный абзац пункта 3, как требуется по замечанию пользователя. Пересборка выполнена через `./run-new.sh`, чтобы обновить `task.pdf` без влияния на остальные документы комплекта.
- Следующий рекомендуемый шаг: при необходимости можно следующим проходом так же локально уточнить длину и плотность подчеркнутого текста пункта 3, если потребуется сделать его визуально компактнее на странице

## 2026-06-23 12:42 — Добавление раздаточного материала в комплект mablinov

- Статус: выполнено
- Сгенерировано: в директорию `diploma-latex-template/mablinov` добавлен документ `handout.tex` по образцу `example/handout.tex`, а `run-new.sh` расширен сборкой и очисткой `handout.pdf` вместе с остальными служебными документами
- Файлы: `diploma-latex-template/mablinov/handout.tex`, `run-new.sh`, `diploma-latex-template/mablinov/handout.pdf`, `tmp/pdfs/handout-page1.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и полный комплект материалов для сдачи
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/example/handout.tex`, `run-new.sh`
- Ключевые решения: для сохранения оформления без расхождений раздаточный материал перенесён в `mablinov` без изменения структуры шаблона и использует те же `info.tex` и класс `diploma` в режиме `master, handout`. Скрипт сборки обновлён так, чтобы `handout.pdf` автоматически создавался и проверялся наряду с `main.pdf`, `review.pdf`, `supervisor_review.pdf` и `task.pdf`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/handout.tex` — `handout.tex`: words=4 chars=30. `./run-new.sh` завершился успешно и создал `diploma-latex-template/mablinov/handout.pdf`; визуальная проверка через `pdftoppm` подтвердила корректный рендер первой страницы в `tmp/pdfs/handout-page1.png`.
- Следующий рекомендуемый шаг: при необходимости можно отдельно подправить содержимое `info.tex` или локальные переопределения именно для `handout.pdf`, если понадобится особая версия раздаточного титульного листа

## 2026-06-23 12:46 — Возврат подписи образовательного центра в раздаточный материал

- Статус: выполнено
- Сгенерировано: в `info.tex` добавлен тип подразделения `Образовательный центр №`, благодаря чему в документах без локального переопределения вместо голого `806` теперь выводится строка `Образовательный центр № 806`
- Файлы: `diploma-latex-template/mablinov/info.tex`, `diploma-latex-template/mablinov/handout.pdf`, `tmp/pdfs/handout-page1-oc806.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная доводка служебных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/10-titlepage.sty`, `diploma-latex-template/mablinov/info.tex`
- Ключевые решения: правка выполнена через общий параметр `\departmentType`, уже поддерживаемый классом `diploma`, поэтому изменение легло в штатную структуру шаблона без ручного патча `handout.tex`. Локальные переопределения в `main.tex`, `review.tex`, `supervisor_review.tex` и `task.tex` сохранены, поэтому их специфическое оформление не нарушено.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/info.tex` — `info.tex`: words=62 chars=534. `./run-new.sh` завершился успешно; визуальная проверка `diploma-latex-template/mablinov/handout.pdf` через `pdftoppm` подтвердила появление строки `Образовательный центр № 806` на первой странице (`tmp/pdfs/handout-page1-oc806.png`).
- Следующий рекомендуемый шаг: при необходимости можно таким же способом вернуть или поменять тип подразделения и в других служебных формах, где используется базовый `\makeAffiliations`

## 2026-06-23 12:51 — Выравнивание блока направления подготовки в review.pdf и supervisor_review.pdf

- Статус: выполнено
- Сгенерировано: в `review.tex` и `supervisor_review.tex` блок `Группа / Направление подготовки` приведён к той же схеме верстки, что и в `handout.pdf`: убраны локальные отличия с `\raggedright`, `\hspace` и разрывами через `\par`, вместо них возвращены строковые разрывы и структура базового шаблона
- Файлы: `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `tmp/pdfs/review-page1-fixed.png`, `tmp/pdfs/supervisor-review-page1-fixed.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная доводка служебных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/supervisor_review.tex`, `diploma-latex-template/mablinov/handout.pdf`, `diploma-latex-template/diploma/styles/10-titlepage.sty`
- Ключевые решения: вместо частичной ручной разметки в двух отзывах использована та же логика построения строк, что и в эталонном `handout`, чтобы подчеркнутая линия у поля `Направление подготовки` доходила и переносилась согласованно. Остальной текст отзывов и их структура не изменялись.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/review.tex diploma-latex-template/mablinov/supervisor_review.tex` — `review.tex`: words=273 chars=2432; `supervisor_review.tex`: words=405 chars=3569. `./run-new.sh` завершился успешно; визуальная проверка первых страниц через `pdftoppm` подтвердила обновлённую верстку в `tmp/pdfs/review-page1-fixed.png` и `tmp/pdfs/supervisor-review-page1-fixed.png`.
- Следующий рекомендуемый шаг: при необходимости можно тем же способом унифицировать и остальные служебные формы, если потребуется полностью одинаковое поведение верхнего блока во всём комплекте

## 2026-06-23 12:55 — Приведение исходных материалов в task.pdf к виду вводимого текста

- Статус: выполнено
- Сгенерировано: в `task.tex` раздел `5. Исходные материалы и пособия` преобразован из набора отдельных подчеркнутых строк в один непрерывный подчеркнутый блок, оформленный по тому же принципу, что и `3. Задание и исходные данные к работе`
- Файлы: `diploma-latex-template/mablinov/task.tex`, `diploma-latex-template/mablinov/task.pdf`, `tmp/pdfs/task-page3-materials.png`
- Основание из плана: `content/todo.md` — сопроводительные документы к ВКР и финальная доводка служебных форм
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/task.tex`
- Ключевые решения: вместо пяти разрозненных вызовов `\underlinedmaterial` список источников собран в один текстовый блок с разделением через точку с запятой. Это позволило получить сплошное подчеркивание, которое воспринимается как поле для вписанного текста, аналогично пункту `3`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/task.tex` — `task.tex`: words=399 chars=3317. `./run-new.sh` завершился успешно; визуальная проверка страницы с пунктами `5` и `6` через `pdftoppm` подтвердила новый вид подчеркивания в `tmp/pdfs/task-page3-materials.png`.
- Следующий рекомендуемый шаг: при необходимости можно тем же способом перевести в формат непрерывного вводимого текста и другие короткие подпункты служебных форм, если потребуется единый визуальный стиль заполнения

## 2026-06-24 11:32 — Автоматическое выделение всей латиницы курсивом

- Статус: выполнено
- Сгенерировано: в `latin-italic.tex` переработан механизм автоматического оформления латиницы, чтобы курсив включался не только после обычного текста, но и после пробелов, знаков препинания и других символьных классов XeTeX; после этого пересобран весь комплект PDF-документов `mablinov`
- Файлы: `diploma-latex-template/mablinov/latin-italic.tex`, `diploma-latex-template/mablinov/main.pdf`, `diploma-latex-template/mablinov/review.pdf`, `diploma-latex-template/mablinov/supervisor_review.pdf`, `diploma-latex-template/mablinov/task.pdf`, `diploma-latex-template/mablinov/handout.pdf`, `tmp/pdfs/latin-check/main-13-013.png`, `tmp/pdfs/latin-check/review-1-1.png`, `tmp/pdfs/latin-check/task-3-3.png`
- Основание из плана: `content/todo.md` — финальная доводка основного текста и сопроводительных материалов ВКР
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/latin-italic.tex`, `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/review.tex`, `diploma-latex-template/mablinov/task.tex`
- Ключевые решения: вместо частичного набора переходов между символами задан полный цикл переключения формы шрифта для всех интерклассов XeTeX, поэтому английские термины теперь стабильно становятся курсивом в основном тексте, служебных документах и подчеркиваемых строках. Переходы для продолжения слов через `-`, `/`, `:` и `_` сохранены, чтобы корректно оформлялись составные обозначения вроде `storage-agent`, `P2P/FUSE`, `ML-runtime`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/latin-italic.tex diploma-latex-template/mablinov/main.tex diploma-latex-template/mablinov/review.tex diploma-latex-template/mablinov/supervisor_review.tex diploma-latex-template/mablinov/task.tex diploma-latex-template/mablinov/handout.tex` — `latin-italic.tex`: words=28 chars=175; `main.tex`: words=159 chars=1373; `review.tex`: words=274 chars=2445; `supervisor_review.tex`: words=406 chars=3582; `task.tex`: words=400 chars=3330; `handout.tex`: words=5 chars=43. `./run-new.sh` завершился успешно; визуальная проверка через `pdftoppm` подтвердила курсив для латиницы на контрольных страницах `main.pdf`, `review.pdf` и `task.pdf`.
- Следующий рекомендуемый шаг: при необходимости можно отдельно пройтись по рисункам и встроенным растровым изображениям, если потребуется вручную привести латинские подписи внутри самих картинок к такому же курсивному стилю

## 2026-06-24 14:49 — Краткий список альтернатив для слайда

- Статус: выполнено
- Сгенерировано: создан компактный файл `alternatives.md` со списком решений для кэширования и хранения данных, где для каждого сервиса указаны предельно краткие недостатки в формате, удобном для вставки в слайд презентации
- Файлы: `alternatives.md`
- Основание из плана: `content/todo.md` — материалы для презентации и раздел анализа существующих решений
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`
- Ключевые решения: в список включены основные альтернативы, уже используемые в дипломе и презентационной логике: Alluxio, JuiceFS, Dragonfly, CubeFS, Rook/Ceph и NFS. Формулировки недостатков сознательно сокращены до 1–2 коротких характеристик, чтобы они помещались на слайд без перегрузки.
- Проверка объёма: `python3 scripts/report_stats.py alternatives.md` — `alternatives.md`: words=28 chars=226.
- Следующий рекомендуемый шаг: при необходимости можно сразу сделать вторую версию этого же списка в табличном виде под конкретный шаблон презентации

## 2026-06-24 14:51 — Добавление речи спикера к слайду с альтернативами

- Статус: выполнено
- Сгенерировано: в конец `alternatives.md` добавлен готовый текст речи спикера для устного сопровождения слайда с альтернативными решениями
- Файлы: `alternatives.md`
- Основание из плана: `content/todo.md` — материалы для презентации и пояснения к слайдам
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `alternatives.md`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`
- Ключевые решения: речь построена как краткое последовательное объяснение, почему каждое из известных решений не закрывает задачу полностью и почему потребовалась специализированная архитектура. Англоязычные названия и ключевые термины в тексте помечены курсивом в Markdown, чтобы файл оставался удобным для чтения и копирования.
- Проверка объёма: `python3 scripts/report_stats.py alternatives.md` — `alternatives.md`: words=131 chars=1028.
- Следующий рекомендуемый шаг: при необходимости можно следующим проходом сделать ещё более короткую устную версию на 20–30 секунд или, наоборот, расширенную версию на 1 минуту

## 2026-06-24 14:58 — Расширение спича по альтернативам с обоснованием

- Статус: выполнено
- Сгенерировано: блок `Речь спикера` в `alternatives.md` расширен до более подробной версии с явным обоснованием критериев сравнения и причин, по которым существующие решения не подходят для задачи ускорения холодного старта больших моделей
- Файлы: `alternatives.md`
- Основание из плана: `content/todo.md` — материалы для презентации и пояснения к архитектурным решениям
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `alternatives.md`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`
- Ключевые решения: спич перестроен от простого перечисления минусов к аргументации через критерии задачи: локальность данных, межузловой обмен, прозрачный файловый интерфейс и операционная сложность. Для `Alluxio`, `JuiceFS`, `Dragonfly`, `CubeFS`, `Rook/Ceph` и `NFS` добавлены причинно-следственные пояснения, почему именно их архитектурные свойства ограничивают применимость в сценарии `serverless ML inference`.
- Проверка объёма: `python3 scripts/report_stats.py alternatives.md` — `alternatives.md`: words=428 chars=3197.
- Следующий рекомендуемый шаг: при необходимости можно сделать ещё одну сжатую версию этого же текста под тайминг 30–40 секунд или разбить спич на паузы под поочерёдное появление пунктов на слайде

## 2026-06-24 17:54 — Подготовка полной речи на защиту по презентации

- Статус: выполнено
- Сгенерировано: создан файл `speak.md` с полной речью спикера для защиты диплома, синхронизированной со структурой `diploma-latex-template/mablinov/pptx.pptx` и рассчитанной на выступление продолжительностью 12–15 минут
- Файлы: `speak.md`
- Основание из плана: `content/todo.md` — материалы для презентации, защита результатов и итоговое представление архитектуры
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/pptx.pptx`, `diploma-latex-template/mablinov/contents/2-02-existing-solutions.tex`, `diploma-latex-template/mablinov/contents/2-05-evaluation.tex`
- Ключевые решения: речь построена в порядке слайдов презентации: актуальность, цель и задачи, исходная архитектура, анализ альтернатив, требования, стек, предложенная архитектура, нагрузочное тестирование, результаты, выводы и дальнейшее развитие. Текст был отдельно сокращён после первичной черновой версии, чтобы при спокойном темпе укладываться примерно в 13–14 минут без спешки.
- Проверка объёма: `python3 scripts/report_stats.py speak.md` — `speak.md`: words=1653 chars=12306. Дополнительная оценка по темпу чтения показала ориентир `12.9` минуты при `130` словах в минуту и `14.0` минут при `120` словах в минуту.
- Следующий рекомендуемый шаг: при необходимости можно подготовить отдельный файл с ответами на вероятные вопросы комиссии, например про выбор `Redis`, сравнение с `NFS`, достоверность метрик и пределы применимости предложенной архитектуры

## 2026-06-24 17:59 — Подготовка быстрой версии речи на 10 минут

- Статус: выполнено
- Сгенерировано: создан файл `speakFast.md` с сокращённой версией речи на защиту, рассчитанной примерно на 10 минут выступления и сохраняющей всю основную логику презентации
- Файлы: `speakFast.md`
- Основание из плана: `content/todo.md` — материалы для презентации, защита результатов и подготовка к выступлению в разных таймингах
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `speak.md`
- Ключевые решения: из полной речи удалены второстепенные пояснения и длинные переходы, при этом сохранены все обязательные блоки: актуальность, цель и задачи, исходная архитектура, анализ альтернатив, требования, целевая архитектура, стенд, результаты и выводы. Текст ориентирован на быстрый, но всё ещё уверенный темп защиты без потери связности.
- Проверка объёма: `python3 scripts/report_stats.py speakFast.md` — `speakFast.md`: words=1278 chars=9515. Дополнительная оценка по темпу чтения показала ориентир `10.0` минут при `130` словах в минуту и `10.8` минут при `120` словах в минуту.
- Следующий рекомендуемый шаг: при необходимости можно подготовить ещё более короткую аварийную версию на 6–7 минут для случаев жёсткого ограничения регламента

## 2026-06-24 18:03 — Центрирование структурных заголовков в main.pdf

- Статус: выполнено
- Сгенерировано: в `main.tex` восстановлено центрирование для макроса `\structure`, благодаря чему заголовки `РЕФЕРАТ`, `СОДЕРЖАНИЕ`, `ТЕРМИНЫ И ОПРЕДЕЛЕНИЯ`, `ПЕРЕЧЕНЬ СОКРАЩЕНИЙ И ОБОЗНАЧЕНИЙ` и `ВВЕДЕНИЕ` выводятся по центру в `main.pdf`
- Файлы: `diploma-latex-template/mablinov/main.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/structure-check/p2-002.png`, `tmp/pdfs/structure-check/p4-004.png`, `tmp/pdfs/structure-check/p9-009.png`, `tmp/pdfs/structure-check/p11-011.png`, `tmp/pdfs/structure-check/p13-013.png`
- Основание из плана: `content/todo.md` — финальная доводка оформления основного текста диплома
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/diploma/styles/02-construction.sty`, `diploma-latex-template/diploma/styles/12-abstract.sty`, `diploma-latex-template/diploma/styles/13-contents.sty`, `diploma-latex-template/diploma/styles/14-terms-and-definitions.sty`, `diploma-latex-template/diploma/styles/15-list-of-abbreviations.sty`, `diploma-latex-template/mablinov/main.tex`
- Ключевые решения: правка внесена только в переопределение `\titleformat{\structure}` внутри `main.tex`; обычные `\section` оставлены без изменений, поэтому центрирование затронуло только структурные элементы, а не все разделы основной части. Это позволило вернуть поведение, согласованное с базовым стилем шаблона, не ломая остальную верстку.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/main.tex` — `main.tex`: words=159 chars=1373. `./run-new.sh` завершился успешно; визуальная проверка страниц 2, 4, 9, 11 и 13 через `pdftoppm` подтвердила центрирование соответствующих заголовков.
- Следующий рекомендуемый шаг: при необходимости можно аналогично согласовать выравнивание других структурных заголовков, например `ЗАКЛЮЧЕНИЕ` и `СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ`, если нужен полностью единый стиль по всему документу

## 2026-06-24 18:07 — Добавление номеров к подпунктам введения

- Статус: выполнено
- Сгенерировано: в `1-introduction.tex` заголовкам `Актуальность темы`, `Проблема и противоречие`, `Цель работы` и `Задачи работы` добавлены явные номера `1`, `2`, `3`, `4`
- Файлы: `diploma-latex-template/mablinov/contents/1-introduction.tex`, `diploma-latex-template/mablinov/main.pdf`, `tmp/pdfs/intro-num-check/intro-013.png`, `tmp/pdfs/intro-num-check/intro-014.png`
- Основание из плана: `content/todo.md` — финальная доводка структуры введения и оформления основного текста
- Использованные материалы: `prompt.md`, `content/todo.md`, `progress.md`, `diploma-latex-template/mablinov/contents/1-introduction.tex`
- Ключевые решения: номера добавлены непосредственно в текст заголовков через существующие `\subsection*`, а не через включение автоматической нумерации `\subsection`. Это позволило избежать нежелательной нумерации вида `0.1` во введении, поскольку `ВВЕДЕНИЕ` оформлено как структурный элемент `\structure`, а не как обычный `\section`.
- Проверка объёма: `python3 scripts/report_stats.py diploma-latex-template/mablinov/contents/1-introduction.tex` — `1-introduction.tex`: words=1268 chars=10664. `./run-new.sh` завершился успешно; визуальная проверка страниц 13 и 14 через `pdftoppm` подтвердила появление заголовков `1 Актуальность темы` и `2 Проблема и противоречие`, а исходник содержит также `3 Цель работы` и `4 Задачи работы`.
- Следующий рекомендуемый шаг: при необходимости можно тем же способом пронумеровать и оставшиеся подпункты введения, например `Объект и предмет исследования`, `Научная новизна и практическая значимость`, `Структура работы`, если нужен полностью единый формат всего введения
