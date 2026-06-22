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
