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
