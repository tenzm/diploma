"""
Генератор presentation2.pptx в стиле vkr.pptx.
Создаётся с нуля (без vkr.pptx как базы) — чистый zip, только 12 слайдов.

Параметры стиля взяты из vkr.pptx:
  - Размер: 10 × 5.62 дюйма
  - Белый фон
  - Шрифт: Roboto
  - Заголовок: 28pt Bold, left=0.341in top=0 h=1.115in
  - Контент: 18pt, left=0.451in top=1.115in
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn, nsmap
from lxml import etree

OUT = "/Users/mablinov/Documents/Diploma/pptx/presentation2.pptx"

# ── Новая презентация с нуля ──────────────────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(10.0)
prs.slide_height = Inches(5.625)   # 5.62 in из vkr.pptx

blank_layout = prs.slide_layouts[6]  # blank

# ── Цвета ────────────────────────────────────────────────────────────────────
BLACK = RGBColor(0x00, 0x00, 0x00)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GRAY  = RGBColor(0x9E, 0x9E, 0x9E)
LGRAY = RGBColor(0xF3, 0xF3, 0xF3)
DGRAY = RGBColor(0x42, 0x42, 0x42)
GREEN = RGBColor(0x15, 0x81, 0x58)   # dk2 из темы vkr
BLUE  = RGBColor(0x05, 0x8D, 0xC7)   # accent1 из темы vkr

W = prs.slide_width
H = prs.slide_height
FONT = "Roboto"


# ═══════════════════════════════════════════════════════════════════════════════
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ═══════════════════════════════════════════════════════════════════════════════

def new_slide():
    return prs.slides.add_slide(blank_layout)


def _set_bg_white(slide):
    """Явно задаём белый фон."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = WHITE


def _para_xml(text, sz_hundredths, bold=False, italic=False,
              color_rgb=None, align="l", font=FONT, space_before=0):
    """Возвращает <a:p> XML-элемент."""
    A = "http://schemas.openxmlformats.org/drawingml/2006/main"
    p = etree.Element(f"{{{A}}}p")

    pPr = etree.SubElement(p, f"{{{A}}}pPr")
    pPr.set("algn", align)
    pPr.set("indent", "0")
    pPr.set("marL", "0")
    buNone = etree.SubElement(pPr, f"{{{A}}}buNone")
    spcBef = etree.SubElement(pPr, f"{{{A}}}spcBef")
    spcPts = etree.SubElement(spcBef, f"{{{A}}}spcPts")
    spcPts.set("val", str(space_before))
    spcAft = etree.SubElement(pPr, f"{{{A}}}spcAft")
    spcPts2 = etree.SubElement(spcAft, f"{{{A}}}spcPts")
    spcPts2.set("val", "0")

    if not text:
        end = etree.SubElement(p, f"{{{A}}}endParaRPr")
        end.set("sz", str(sz_hundredths))
        lat = etree.SubElement(end, f"{{{A}}}latin"); lat.set("typeface", font)
        ea  = etree.SubElement(end, f"{{{A}}}ea");  ea.set("typeface", font)
        cs  = etree.SubElement(end, f"{{{A}}}cs");  cs.set("typeface", font)
        return p

    r = etree.SubElement(p, f"{{{A}}}r")
    rPr = etree.SubElement(r, f"{{{A}}}rPr")
    rPr.set("lang", "ru")
    rPr.set("sz", str(sz_hundredths))
    if bold:   rPr.set("b", "1")
    if italic: rPr.set("i", "1")
    if color_rgb:
        sf = etree.SubElement(rPr, f"{{{A}}}solidFill")
        sc = etree.SubElement(sf,  f"{{{A}}}srgbClr")
        sc.set("val", str(color_rgb).upper())
    lat = etree.SubElement(rPr, f"{{{A}}}latin"); lat.set("typeface", font)
    ea  = etree.SubElement(rPr, f"{{{A}}}ea");  ea.set("typeface", font)
    cs  = etree.SubElement(rPr, f"{{{A}}}cs");  cs.set("typeface", font)
    t = etree.SubElement(r, f"{{{A}}}t")
    t.text = text
    return p


def txbox(slide, x, y, w, h, paras, anchor="t"):
    """
    paras: list of dicts с ключами text/sz/bold/italic/color/align/space_before
    """
    shape = slide.shapes.add_textbox(x, y, w, h)
    tf = shape.text_frame
    tf.word_wrap = True

    bodyPr = tf._txBody.find(qn("a:bodyPr"))
    bodyPr.set("anchor", anchor)
    bodyPr.set("anchorCtr", "0")

    # Очищаем существующие параграфы
    txBody = tf._txBody
    A = "http://schemas.openxmlformats.org/drawingml/2006/main"
    for old_p in txBody.findall(f"{{{A}}}p"):
        txBody.remove(old_p)

    for pd in paras:
        p_elem = _para_xml(
            text         = pd.get("text", ""),
            sz_hundredths= pd.get("sz", 1800),
            bold         = pd.get("bold", False),
            italic       = pd.get("italic", False),
            color_rgb    = pd.get("color", None),
            align        = pd.get("align", "l"),
            font         = pd.get("font", FONT),
            space_before = pd.get("spc", 0),
        )
        # вставляем перед endParaRPr если есть
        end_rpr = txBody.find(f"{{{A}}}endParaRPr")
        if end_rpr is not None:
            txBody.insert(list(txBody).index(end_rpr), p_elem)
        else:
            txBody.append(p_elem)

    return shape


def P(text, sz=1800, bold=False, italic=False, color=None,
      align="l", spc=0, font=FONT):
    return dict(text=text, sz=sz, bold=bold, italic=italic,
                color=color, align=align, spc=spc, font=font)


def E(sz=1800):
    return P("", sz=sz)


def title(slide, text):
    """Заголовок слайда: 28pt Bold Roboto, top=0, h=1.115in (по vkr.pptx)."""
    txbox(slide,
          x=Inches(0.341), y=Inches(0.0),
          w=Inches(9.318), h=Inches(1.115),
          paras=[P(text, sz=2800, bold=True)],
          anchor="ctr")


def body(slide, paras, x=None, y=None, w=None, h=None, anchor="t"):
    x = x if x is not None else Inches(0.451)
    y = y if y is not None else Inches(1.115)
    w = w if w is not None else Inches(9.133)
    h = h if h is not None else Inches(4.35)
    return txbox(slide, x, y, w, h, paras, anchor=anchor)


def rect(slide, x, y, w, h, fill=None, line=None):
    s = slide.shapes.add_shape(1, x, y, w, h)
    if fill:
        s.fill.solid(); s.fill.fore_color.rgb = fill
    else:
        s.fill.background()
    if line:
        s.line.color.rgb = line
    else:
        s.line.fill.background()
    return s


def table(slide, x, y, w, h, headers, rows,
          hdr_bg=GREEN, hdr_fg=WHITE, hdr_sz=1300,
          row_sz=1200):
    ncols = len(headers)
    nrows = len(rows) + 1
    tbl = slide.shapes.add_table(nrows, ncols, x, y, w, h).table
    cw = w // ncols
    for col in tbl.columns:
        col.width = cw

    def cell(r, c, txt, bg, fg, bold=False, sz=row_sz):
        cl = tbl.cell(r, c)
        cl.fill.solid(); cl.fill.fore_color.rgb = bg
        p = cl.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = str(txt)
        run.font.size = Pt(sz / 100)
        run.font.bold = bold
        run.font.color.rgb = fg
        run.font.name = FONT

    for c, h_ in enumerate(headers):
        cell(0, c, h_, hdr_bg, hdr_fg, bold=True, sz=hdr_sz)
    for r, row in enumerate(rows):
        bg = LGRAY if r % 2 == 0 else WHITE
        for c, v in enumerate(row):
            cell(r + 1, c, v, bg, BLACK, sz=row_sz)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 1 — ТИТУЛЬНЫЙ
# ═══════════════════════════════════════════════════════════════════════════════
s1 = new_slide(); _set_bg_white(s1)

# Логотип-заглушка
rect(s1, Inches(0.22), Inches(0.15), Inches(0.74), Inches(0.72), fill=LGRAY)
txbox(s1, Inches(0.22), Inches(0.35), Inches(0.74), Inches(0.3),
      [P("МАИ", sz=900, bold=True, color=DGRAY, align="c")])

# Верхняя строка
txbox(s1, Inches(1.05), Inches(0.18), Inches(8.0), Inches(0.45),
      [P("МОСКОВСКИЙ АВИАЦИОННЫЙ ИНСТИТУТ (НИУ)  ·  Институт №8  ·  Кафедра 806",
         sz=1000, color=DGRAY)])

# Главный заголовок
txbox(s1, Inches(0.75), Inches(0.95), Inches(8.5), Inches(2.5),
      [P("Выпускная квалификационная работа магистра на тему:",
         sz=1500, color=DGRAY, align="c"),
       E(700),
       P("Оптимизация холодного старта и масштабирования\n"
         "моделей машинного обучения в бессерверном инференсе\n"
         "для обеспечения надёжности и высокой доступности",
         sz=2200, bold=True, align="c")],
      anchor="t")

# Студент
txbox(s1, Inches(0.75), Inches(3.75), Inches(8.5), Inches(1.1),
      [P("Студент группы М8О-209СВ-24:  Блинов Максим Алексеевич", sz=1600),
       P("Научный руководитель:  Булакина Мария Борисовна", sz=1600),
       E(300),
       P("Направление:  02.04.02 Фундаментальная информатика и информационные технологии",
         sz=1300, color=DGRAY)])

txbox(s1, Inches(2.72), Inches(5.1), Inches(4.56), Inches(0.35),
      [P("Москва 2025", sz=1200, align="c")])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 2 — АКТУАЛЬНОСТЬ ТЕМЫ
# ═══════════════════════════════════════════════════════════════════════════════
s2 = new_slide(); _set_bg_white(s2)
title(s2, "Актуальность темы")

body(s2, [
    P("Размеры языковых моделей растут экспоненциально:", sz=1800, bold=True),
    E(300),
    P("  •  GPT-2 (2019):       1.5 млрд параметров  —  3 ГБ", sz=1700),
    P("  •  LLaMA 3 8B (2024):  8 млрд параметров   —  15 ГБ", sz=1700),
    P("  •  LLaMA 3 70B (2024): 70 млрд параметров  —  140 ГБ", sz=1700),
    P("  •  Falcon 180B (2023): 180 млрд параметров —  360 ГБ", sz=1700),
    E(500),
    P("Проблема холодного старта в serverless-инференсе:", sz=1800, bold=True),
    E(300),
    P("  •  При каждом scale-up Pod заново скачивает всю модель из интернета", sz=1700),
    P("  •  15 ГБ × 200 МБ/с = 75 секунд до первого токена", sz=1700),
    P("  •  10 одновременных реплик = 150 ГБ внешнего трафика", sz=1700),
    P("  •  p99 latency первого запроса — минуты вместо секунд → нарушение SLA", sz=1700),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 3 — ЦЕЛЬ И ЗАДАЧИ
# ═══════════════════════════════════════════════════════════════════════════════
s3 = new_slide(); _set_bg_white(s3)
title(s3, "Цель и задачи работы")

body(s3, [
    P("Цель:", sz=1800, bold=True),
    E(200),
    P("Разработка архитектуры распределённого кэширования ML-моделей для serverless-инференса "
      "в Kubernetes, сокращающей задержку холодного старта и снижающей нагрузку на внешние репозитории.",
      sz=1700, italic=True),
    E(600),
    P("Задачи:", sz=1800, bold=True),
    E(200),
    P("  1.  Анализ причин холодного старта и масштаба проблемы роста весов моделей", sz=1600),
    P("  2.  Исследование существующих решений: Alluxio, JuiceFS, Dragonfly, CubeFS, Rook/Ceph", sz=1600),
    P("  3.  Разработка NFS-этапа с координацией через flock и Kubernetes Lease", sz=1600),
    P("  4.  Проектирование P2P/FUSE-архитектуры с трёхуровневой иерархией кэша", sz=1600),
    P("  5.  Реализация storage-agent (DaemonSet) и storage-mounter (FUSE-клиент)", sz=1600),
    P("  6.  Выбор механизма обнаружения узлов: Redis heartbeat vs Gossip vs mDNS", sz=1600),
    P("  7.  Теоретический анализ: AMAT, Закон Литтла, Амдал, Ципф", sz=1600),
    P("  8.  Формирование методики оценки эффективности с расчётными значениями", sz=1600),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 4 — ИСХОДНАЯ АРХИТЕКТУРА
# ═══════════════════════════════════════════════════════════════════════════════
s4 = new_slide(); _set_bg_white(s4)
title(s4, "Исходная архитектура")

rect(s4, Inches(0.45), Inches(1.2), Inches(4.9), Inches(4.05), fill=LGRAY)
txbox(s4, Inches(0.45), Inches(2.85), Inches(4.9), Inches(0.5),
      [P("[ вставить изображение исходной архитектуры ]",
         sz=1100, color=GRAY, align="c")])

txbox(s4, Inches(5.55), Inches(1.15), Inches(4.15), Inches(4.15),
      [P("Схема: storage-initializer + emptyDir", sz=1700, bold=True),
       E(400),
       P("1.  Scheduler помещает Pod на worker-ноду", sz=1500),
       P("2.  storage-initializer скачивает модель из HuggingFace в emptyDir", sz=1500),
       P("3.  runtime-container монтирует emptyDir, загружает в GPU", sz=1500),
       E(600),
       P("Ключевые проблемы:", sz=1700, bold=True),
       E(400),
       P("  ✕  Нет переиспользования — каждый Pod скачивает заново", sz=1500),
       P("  ✕  10 реплик = 10 загрузок = 150 ГБ внешнего трафика", sz=1500),
       P("  ✕  T_first_byte = T_model_ready ≈ 75 с", sz=1500),
       P("  ✕  Зависимость от доступности HuggingFace Hub", sz=1500),
       ])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 5 — ТРЕБОВАНИЯ
# ═══════════════════════════════════════════════════════════════════════════════
s5 = new_slide(); _set_bg_white(s5)
title(s5, "Требования к архитектуре")

txbox(s5, Inches(0.451), Inches(1.15), Inches(4.55), Inches(4.2),
      [P("Функциональные:", sz=1800, bold=True),
       E(300),
       P("  •  Переиспользование весов между запусками", sz=1550),
       P("  •  P2P-передача чанков между нодами без HF Hub", sz=1550),
       P("  •  Стандартный POSIX-интерфейс для ML-runtime", sz=1550),
       P("  •  Автоматический fallback на внешний репозиторий", sz=1550),
       P("  •  Совместимость с Kubernetes (DaemonSet, CSI)", sz=1550),
       P("  •  Атомарная запись чанков (tmp → os.Rename)", sz=1550),
       ])

txbox(s5, Inches(5.25), Inches(1.15), Inches(4.45), Inches(4.2),
      [P("Нефункциональные:", sz=1800, bold=True),
       E(300),
       P("  •  T_model_ready при local hit ≤ 3 с (15 ГБ)", sz=1550),
       P("  •  T_first_byte (lazy FUSE loading) < 1 с", sz=1550),
       P("  •  Трафик N=10 реплик = 1× размер модели", sz=1550),
       P("  •  Отказ worker-ноды → graceful degradation", sz=1550),
       P("  •  Overhead FUSE (последов. чтение) ≤ 0.5% CPU", sz=1550),
       P("  •  Redis lookup latency p99 < 5 мс", sz=1550),
       ])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 6 — СТЕК ТЕХНОЛОГИЙ
# ═══════════════════════════════════════════════════════════════════════════════
s6 = new_slide(); _set_bg_white(s6)
title(s6, "Стек технологий")

body(s6, [
    P("Kubernetes", sz=1800, bold=True),
    P("   Оркестрация: DaemonSet для storage-agent; PVC, CSI-интеграция", sz=1500, color=DGRAY),
    E(250),
    P("Go", sz=1800, bold=True),
    P("   Реализация storage-agent и storage-mounter; библиотека go-fuse", sz=1500, color=DGRAY),
    E(250),
    P("Redis", sz=1800, bold=True),
    P("   Реестр метаданных чанков: TTL-записи, heartbeat агентов (Sentinel / Cluster)", sz=1500, color=DGRAY),
    E(250),
    P("FUSE (Linux)", sz=1800, bold=True),
    P("   Виртуальная ФС — ML-runtime видит обычные файлы без изменений кода", sz=1500, color=DGRAY),
    E(250),
    P("HuggingFace Hub", sz=1800, bold=True),
    P("   Внешний репозиторий весов моделей; fallback-источник при отсутствии кэша", sz=1500, color=DGRAY),
    E(250),
    P("NFS  ·  Docker  ·  Prometheus + Grafana", sz=1800, bold=True),
    P("   Промежуточный этап с flock / Lease; контейнеризация; мониторинг hit rate и latency",
      sz=1500, color=DGRAY),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 7 — ПРЕДЛОЖЕННАЯ АРХИТЕКТУРА
# ═══════════════════════════════════════════════════════════════════════════════
s7 = new_slide(); _set_bg_white(s7)
title(s7, "Предложенная архитектура")

rect(s7, Inches(0.45), Inches(1.2), Inches(5.5), Inches(4.05), fill=LGRAY)
txbox(s7, Inches(0.45), Inches(2.85), Inches(5.5), Inches(0.5),
      [P("[ вставить изображение P2P/FUSE-архитектуры ]",
         sz=1100, color=GRAY, align="c")])

txbox(s7, Inches(6.15), Inches(1.15), Inches(3.55), Inches(4.15),
      [P("storage-agent  (DaemonSet)", sz=1600, bold=True),
       P("  chunk-кэш на NVMe · UDS → mounter · TCP → пиры", sz=1400),
       E(400),
       P("storage-mounter  (FUSE)", sz=1600, bold=True),
       P("  виртуальная ФС · lazy loading · T_first_byte < 1 с", sz=1400),
       E(400),
       P("Redis Cluster", sz=1600, bold=True),
       P("  реестр чанков · heartbeat 10 с · TTL 30 с", sz=1400),
       E(500),
       P("Алгоритм чтения чанка:", sz=1600, bold=True),
       E(200),
       P("  1. Локальный NVMe         →  2.3 мс", sz=1400),
       P("  2. Соседняя нода (P2P)    →  13.3 мс", sz=1400),
       P("  3. HuggingFace (fallback)  →  130+ мс", sz=1400),
       ])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 8 — НАГРУЗОЧНЫЙ СТЕНД
# ═══════════════════════════════════════════════════════════════════════════════
s8 = new_slide(); _set_bg_white(s8)
title(s8, "Нагрузочное тестирование")

txbox(s8, Inches(0.451), Inches(1.15), Inches(4.55), Inches(4.2),
      [P("Тестовый стенд:", sz=1800, bold=True),
       E(300),
       P("  •  6 worker-нод: Intel Xeon Silver, 16c/32t, 64 ГБ RAM", sz=1500),
       P("  •  Samsung 980 Pro NVMe 2 ТБ — seq. read 7 000 МБ/с", sz=1500),
       P("  •  Сеть: 10 Гбит/с Ethernet, RTT ≤ 0.5 мс", sz=1500),
       P("  •  Redis: 1 master + 2 replica", sz=1500),
       E(500),
       P("Тестовые модели:", sz=1800, bold=True),
       E(300),
       P("  •  Llama 3 8B   —  15 ГБ,  960 чанков × 16 МБ", sz=1500),
       P("  •  Mistral 7B   —  14 ГБ,  896 чанков × 16 МБ", sz=1500),
       P("  •  Llama 3 70B  —  140 ГБ, 8 960 чанков × 16 МБ", sz=1500),
       ])

txbox(s8, Inches(5.25), Inches(1.15), Inches(4.45), Inches(4.2),
      [P("Сценарии:", sz=1800, bold=True),
       E(300),
       P("  1.  Cold cluster — кэш пуст, Redis пуст", sz=1500),
       P("       первый запуск в кластере", sz=1350, color=DGRAY),
       E(200),
       P("  2.  Warm (same node) — local cache hit", sz=1500),
       P("       модель уже есть на той же ноде", sz=1350, color=DGRAY),
       E(200),
       P("  3.  Warm (peer node) — P2P peer cache hit", sz=1500),
       P("       модель есть на соседней ноде", sz=1350, color=DGRAY),
       E(200),
       P("  4.  Burst ×10 — 10 подов одновременно", sz=1500),
       P("       суммарный трафик и p99 по репликам", sz=1350, color=DGRAY),
       E(500),
       P("Метрики: T_model_ready (p50/p99)  ·  T_first_byte  ·  V_ext  ·  Redis p99  ·  CPU FUSE",
         sz=1250, color=DGRAY, italic=True),
       ])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 9 — РЕЗУЛЬТАТЫ
# ═══════════════════════════════════════════════════════════════════════════════
s9 = new_slide(); _set_bg_white(s9)
title(s9, "Результаты тестирования")

table(s9,
      x=Inches(0.3), y=Inches(1.15),
      w=Inches(9.45), h=Inches(3.5),
      headers=["Показатель", "emptyDir (baseline)", "NFS", "P2P / FUSE"],
      rows=[
          ["T_model_ready,  cold cluster",       "~75 с",   "~75 с",        "~75 с"],
          ["T_model_ready,  warm (same node)",    "~75 с",   "~12 с",        "~2 с  ✓"],
          ["T_model_ready,  warm (peer node)",    "~75 с",   "~12 с",        "~12 с  ✓"],
          ["T_first_byte",                        "~75 с",   "~75 с",        "< 1 с  ✓"],
          ["Внешний трафик,  N = 10 реплик",      "150 ГБ",  "15 ГБ",        "15 ГБ  ✓"],
          ["SPOF",                                "нет",     "NFS-сервер",   "Redis (HA → нет)"],
          ["Деградация при отказе",               "нет",     "полная",       "graceful"],
          ["Redis lookup  p50 / p99",             "—",       "—",            "< 1 мс / < 5 мс"],
          ["CPU overhead FUSE",                   "—",       "—",            "< 0.5 %"],
      ],
      hdr_sz=1300, row_sz=1200, hdr_bg=GREEN)

txbox(s9, Inches(0.3), Inches(4.75), Inches(9.45), Inches(0.7),
      [P("×36 ускорение (local cache)   ·   ×6 ускорение (peer cache)   ·   "
         "×10 снижение трафика при N=10   ·   ×30 снижение AMAT (130 мс → 4.3 мс)",
         sz=1400, bold=True, color=GREEN, align="c")])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 10 — НАДЁЖНОСТЬ
# ═══════════════════════════════════════════════════════════════════════════════
s10 = new_slide(); _set_bg_white(s10)
title(s10, "Анализ надёжности")

body(s10, [
    P("Сценарий 1: Отказ worker-ноды", sz=1800, bold=True),
    P("  TTL-записи агента в Redis истекают через 30 с — автоматическая очистка метаданных.", sz=1500),
    P("  При r = 2 репликах: P(потери чанка) = 10⁻⁴;   при r = 3: P = 10⁻⁶", sz=1500),
    P("  Результат: деградация к HuggingFace fallback — сервис не останавливается", sz=1500, color=GREEN),
    E(500),
    P("Сценарий 2: Недоступность Redis", sz=1800, bold=True),
    P("  Агент теряет peer discovery, перестаёт видеть соседей.", sz=1500),
    P("  Система работает по схеме: local cache → HuggingFace (без P2P-уровня).", sz=1500),
    P("  Результат: сервис продолжает работу при наличии локального кэша", sz=1500, color=GREEN),
    E(500),
    P("Сценарий 3: Недоступность HuggingFace Hub", sz=1800, bold=True),
    P("  Чанки из local / peer cache обслуживаются полностью автономно.", sz=1500),
    P("  Прогретый кластер изолирован от внешнего источника.", sz=1500),
    P("  NFS при отказе сервера → полная остановка;  P2P/FUSE → graceful degradation", sz=1500, color=GREEN),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 11 — ИТОГИ
# ═══════════════════════════════════════════════════════════════════════════════
s11 = new_slide(); _set_bg_white(s11)
title(s11, "Итоги работы")

body(s11, [
    P("Выполненные задачи:", sz=1800, bold=True),
    E(200),
    P("  ✓  Проведён анализ причин и масштаба проблемы cold start в serverless ML inference", sz=1600),
    P("  ✓  Исследованы и сравнены 5 решений: Alluxio, JuiceFS, Dragonfly, CubeFS, Rook/Ceph", sz=1600),
    P("  ✓  Разработан NFS-этап с Leader Election через Kubernetes Lease", sz=1600),
    P("  ✓  Спроектирована P2P/FUSE-архитектура с трёхуровневой иерархией кэша", sz=1600),
    P("  ✓  Реализованы storage-agent (DaemonSet) и storage-mounter (FUSE)", sz=1600),
    P("  ✓  Обоснован выбор Redis heartbeat vs Gossip Protocol vs mDNS", sz=1600),
    P("  ✓  Теоретический анализ: AMAT, Закон Литтла, Амдал, Ципф", sz=1600),
    E(500),
    P("Практическая ценность:", sz=1800, bold=True),
    E(200),
    P("  •  135 ГБ экономии внешнего трафика при 10 репликах Llama 3 8B", sz=1600),
    P("  •  T_model_ready: 75 с → 2 с при прогретом кластере  (×36 ускорение)", sz=1600),
    P("  •  T_first_byte < 1 с благодаря FUSE lazy loading  (было 75 с)", sz=1600),
    P("  •  Устранение NFS как единственной точки отказа", sz=1600),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 12 — ДАЛЬНЕЙШЕЕ РАЗВИТИЕ
# ═══════════════════════════════════════════════════════════════════════════════
s12 = new_slide(); _set_bg_white(s12)
title(s12, "Направления дальнейшего развития")

body(s12, [
    P("  1.  Gossip-based peer discovery — P2P без зависимости от Redis", sz=1700),
    P("  2.  mTLS между storage-agent — аутентификация TCP для production", sz=1700),
    P("  3.  Cache warming — предзагрузка по расписанию, Zipf-прогнозирование", sz=1700),
    P("  4.  CSI-плагин — нативная интеграция с Kubernetes PVC", sz=1700),
    P("  5.  Поддержка Ollama и ModelScope помимо HuggingFace Hub", sz=1700),
    P("  6.  Экспериментальная валидация на реальном GPU-кластере с vLLM", sz=1700),
    E(800),
    P("Система позволяет сократить задержку холодного старта на порядок "
      "при отсутствии деградации надёжности — что критично для "
      "production serverless ML inference.",
      sz=1700, bold=True, italic=True, color=GREEN),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СОХРАНЕНИЕ
# ═══════════════════════════════════════════════════════════════════════════════
prs.save(OUT)
print(f"Saved: {OUT}  ({len(prs.slides)} slides)")
