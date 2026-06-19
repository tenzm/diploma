"""
Генератор презентации диплома.
Запуск: python3 generate.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
from pptx.enum.dml import MSO_THEME_COLOR
import copy

# ── Цвета ────────────────────────────────────────────────────────────────────
DARK_BLUE   = RGBColor(0x1A, 0x23, 0x7E)
MED_BLUE    = RGBColor(0x28, 0x3A, 0x9F)
LIGHT_BLUE  = RGBColor(0x3F, 0x51, 0xB5)
ACCENT_GREEN = RGBColor(0x00, 0xC8, 0x53)
ACCENT_RED  = RGBColor(0xE5, 0x39, 0x35)
ACCENT_YELLOW = RGBColor(0xFF, 0xB3, 0x00)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY  = RGBColor(0xF5, 0xF5, 0xF5)
MID_GRAY    = RGBColor(0xBD, 0xBD, 0xBD)
DARK_GRAY   = RGBColor(0x42, 0x42, 0x42)
TEXT_DARK   = RGBColor(0x1A, 0x1A, 0x2E)

# ── Размеры слайда (16:9 Widescreen) ─────────────────────────────────────────
W = Inches(13.33)
H = Inches(7.5)

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H

blank_layout = prs.slide_layouts[6]  # полностью пустой макет


# ═══════════════════════════════════════════════════════════════════════════════
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ═══════════════════════════════════════════════════════════════════════════════

def add_slide():
    return prs.slides.add_slide(blank_layout)


def set_bg(slide, color: RGBColor):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_rect(slide, x, y, w, h, fill_color=None, line_color=None, line_width=None):
    from pptx.util import Pt
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    shape = slide.shapes.add_shape(1, x, y, w, h)  # 1 = MSO_SHAPE_TYPE.RECTANGLE
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if line_color:
        shape.line.color.rgb = line_color
        if line_width:
            shape.line.width = line_width
    else:
        shape.line.fill.background()
    return shape


def add_textbox(slide, x, y, w, h, text, font_size=18, bold=False,
                color=WHITE, align=PP_ALIGN.LEFT, italic=False, wrap=True):
    txBox = slide.shapes.add_textbox(x, y, w, h)
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = "Calibri"
    return txBox


def add_textbox_multiline(slide, x, y, w, h, lines, font_size=16,
                          color=WHITE, line_spacing=None):
    """lines: list of (text, bold, size_override)"""
    txBox = slide.shapes.add_textbox(x, y, w, h)
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for item in lines:
        if isinstance(item, str):
            text, bold, sz = item, False, font_size
        elif len(item) == 2:
            text, bold = item; sz = font_size
        else:
            text, bold, sz = item
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = text
        run.font.size = Pt(sz)
        run.font.bold = bold
        run.font.color.rgb = color
        run.font.name = "Calibri"
    return txBox


def slide_header(slide, title, subtitle=None, bg_dark=True):
    """Стандартная шапка слайда с цветной полосой."""
    # Полоса-заголовок
    bar_h = Inches(1.15)
    add_rect(slide, 0, 0, W, bar_h, fill_color=DARK_BLUE)
    # Номер слайда — маленькая зелёная плашка
    add_rect(slide, 0, 0, Inches(0.06), bar_h, fill_color=ACCENT_GREEN)
    # Заголовок
    add_textbox(slide, Inches(0.18), Inches(0.08), W - Inches(0.3), Inches(0.6),
                title, font_size=28, bold=True, color=WHITE, align=PP_ALIGN.LEFT)
    if subtitle:
        add_textbox(slide, Inches(0.18), Inches(0.72), W - Inches(0.3), Inches(0.35),
                    subtitle, font_size=14, bold=False, color=ACCENT_GREEN)
    # Нижняя полоса
    add_rect(slide, 0, H - Inches(0.25), W, Inches(0.25), fill_color=DARK_BLUE)
    add_textbox(slide, Inches(0.2), H - Inches(0.24), W - Inches(0.4), Inches(0.22),
                "Блинов М.А. · МАИ · 02.04.02 · 2025",
                font_size=9, color=MID_GRAY, align=PP_ALIGN.LEFT)


def bullet_list(slide, x, y, w, h, items, font_size=15, color=TEXT_DARK,
                bullet="•", indent=Inches(0.22)):
    txBox = slide.shapes.add_textbox(x, y, w, h)
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        if isinstance(item, tuple):
            text, lvl = item
        else:
            text, lvl = item, 0
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        bul = ("  " * lvl) + (bullet if lvl == 0 else "–") + "  "
        run = p.add_run()
        run.text = bul + text
        run.font.size = Pt(font_size)
        run.font.color.rgb = color
        run.font.name = "Calibri"
        run.font.bold = False
    return txBox


def add_table(slide, x, y, w, h, headers, rows,
              header_bg=DARK_BLUE, header_fg=WHITE,
              row_bg1=LIGHT_GRAY, row_bg2=WHITE,
              font_size=13, header_size=13):
    cols = len(headers)
    nrows = len(rows) + 1
    tbl = slide.shapes.add_table(nrows, cols, x, y, w, h).table

    # Задать примерно равную ширину столбцов
    col_w = w // cols
    for i, col in enumerate(tbl.columns):
        col.width = col_w

    def _cell(r, c, text, bg, fg, bold=False, sz=font_size, align=PP_ALIGN.CENTER):
        cell = tbl.cell(r, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg
        tf = cell.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = align
        run = p.add_run()
        run.text = str(text)
        run.font.size = Pt(sz)
        run.font.bold = bold
        run.font.color.rgb = fg
        run.font.name = "Calibri"

    for c, h_text in enumerate(headers):
        _cell(0, c, h_text, header_bg, header_fg, bold=True, sz=header_size)

    for r, row in enumerate(rows):
        bg = row_bg1 if r % 2 == 0 else row_bg2
        for c, val in enumerate(row):
            _cell(r + 1, c, val, bg, TEXT_DARK, sz=font_size, align=PP_ALIGN.LEFT)

    return tbl


def highlight_box(slide, x, y, w, h, text, font_size=22, bg=ACCENT_GREEN,
                  fg=WHITE, bold=True, align=PP_ALIGN.CENTER):
    add_rect(slide, x, y, w, h, fill_color=bg)
    pad = Inches(0.1)
    add_textbox(slide, x + pad, y + pad, w - 2*pad, h - 2*pad,
                text, font_size=font_size, bold=bold, color=fg, align=align, wrap=True)


def metric_card(slide, x, y, w, h, value, label, value_color=ACCENT_GREEN,
                bg=DARK_BLUE):
    add_rect(slide, x, y, w, h, fill_color=bg)
    # Граница слева зелёная
    add_rect(slide, x, y, Inches(0.07), h, fill_color=value_color)
    pad = Inches(0.15)
    add_textbox(slide, x + pad, y + Inches(0.12), w - pad*2, Inches(0.52),
                value, font_size=28, bold=True, color=value_color,
                align=PP_ALIGN.CENTER)
    add_textbox(slide, x + pad, y + Inches(0.6), w - pad*2, h - Inches(0.72),
                label, font_size=11, bold=False, color=WHITE,
                align=PP_ALIGN.CENTER, wrap=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 1 — ТИТУЛЬНЫЙ
# ═══════════════════════════════════════════════════════════════════════════════
s1 = add_slide()
set_bg(s1, DARK_BLUE)

# Верхняя тонкая зелёная линия
add_rect(s1, 0, 0, W, Inches(0.06), fill_color=ACCENT_GREEN)

# Университет
add_textbox(s1, Inches(0.7), Inches(0.3), W - Inches(1.4), Inches(0.38),
            "МОСКОВСКИЙ АВИАЦИОННЫЙ ИНСТИТУТ",
            font_size=15, bold=True, color=MID_GRAY, align=PP_ALIGN.CENTER)
add_textbox(s1, Inches(0.7), Inches(0.64), W - Inches(1.4), Inches(0.32),
            "(национальный исследовательский университет)",
            font_size=12, bold=False, color=MID_GRAY, align=PP_ALIGN.CENTER)

# Горизонтальный разделитель
add_rect(s1, Inches(2.5), Inches(1.05), W - Inches(5.0), Inches(0.025),
         fill_color=ACCENT_GREEN)

# Главный заголовок
add_textbox(s1, Inches(0.5), Inches(1.2), W - Inches(1.0), Inches(2.2),
            "Оптимизация холодного старта и масштабирования моделей машинного обучения "
            "в бессерверном инференсе для обеспечения надёжности и высокой доступности",
            font_size=24, bold=True, color=WHITE, align=PP_ALIGN.CENTER, wrap=True)

# Разделитель
add_rect(s1, Inches(2.5), Inches(3.5), W - Inches(5.0), Inches(0.025),
         fill_color=LIGHT_BLUE)

# Данные студента
add_textbox(s1, Inches(0.5), Inches(3.7), W - Inches(1.0), Inches(0.36),
            "02.04.02 Фундаментальная информатика и информационные технологии  ·  Институт №8  ·  Кафедра 806",
            font_size=13, bold=False, color=MID_GRAY, align=PP_ALIGN.CENTER)

info_x = Inches(2.0)
info_w = W - Inches(4.0)

add_textbox(s1, info_x, Inches(4.2), info_w, Inches(0.42),
            "Студент:  Блинов Максим Алексеевич  ·  М8О-209СВ-24",
            font_size=16, bold=False, color=WHITE, align=PP_ALIGN.CENTER)

add_textbox(s1, info_x, Inches(4.65), info_w, Inches(0.42),
            "Научный руководитель:  Булакина Мария Борисовна",
            font_size=16, bold=False, color=WHITE, align=PP_ALIGN.CENTER)

# Год
add_textbox(s1, Inches(0.5), Inches(5.3), W - Inches(1.0), Inches(0.4),
            "Москва, 2025",
            font_size=15, bold=False, color=MID_GRAY, align=PP_ALIGN.CENTER)

# Нижняя полоса
add_rect(s1, 0, H - Inches(0.38), W, Inches(0.38), fill_color=RGBColor(0x0D, 0x14, 0x4F))
add_textbox(s1, Inches(0.3), H - Inches(0.36), W - Inches(0.6), Inches(0.32),
            "Выпускная квалификационная работа магистра",
            font_size=11, bold=False, color=MID_GRAY, align=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 2 — АКТУАЛЬНОСТЬ ТЕМЫ
# ═══════════════════════════════════════════════════════════════════════════════
s2 = add_slide()
set_bg(s2, WHITE)
slide_header(s2, "Актуальность темы", "Рост размеров ML-моделей → проблема холодного старта")

content_y = Inches(1.3)
content_h = H - Inches(1.6)
col_x1 = Inches(0.3)
col_w1 = Inches(6.1)
col_x2 = Inches(6.7)
col_w2 = Inches(6.4)

# Левый столбец — проблемы
add_textbox(s2, col_x1, content_y, col_w1, Inches(0.36),
            "Ключевые тенденции", font_size=16, bold=True,
            color=DARK_BLUE, align=PP_ALIGN.LEFT)

bullet_list(s2, col_x1, content_y + Inches(0.38), col_w1, Inches(2.2),
            [
                "Размеры LLM растут экспоненциально (+40× за 5 лет)",
                "Serverless-инференс (scale-to-zero) — стандарт облачных платформ",
                "При каждом холодном старте под скачивает всю модель заново",
                "15 ГБ модели = ~75 с загрузки при 200 МБ/с канале",
                "10 реплик = 150 ГБ внешнего трафика за одну волну",
            ],
            font_size=15, color=TEXT_DARK)

# Красная карточка — боль
add_rect(s2, col_x1, content_y + Inches(2.75), col_w1, Inches(1.35),
         fill_color=RGBColor(0xFF, 0xEB, 0xEB))
add_rect(s2, col_x1, content_y + Inches(2.75), Inches(0.07), Inches(1.35),
         fill_color=ACCENT_RED)
add_textbox(s2, col_x1 + Inches(0.15), content_y + Inches(2.83),
            col_w1 - Inches(0.2), Inches(0.36),
            "Нарушение SLA:", font_size=15, bold=True,
            color=ACCENT_RED, align=PP_ALIGN.LEFT)
add_textbox(s2, col_x1 + Inches(0.15), content_y + Inches(3.18),
            col_w1 - Inches(0.2), Inches(0.72),
            "p99 latency первого запроса = минуты вместо секунд\n"
            "T_first_byte ≈ T_model_ready ≈ 75 с — инференс не начнётся раньше",
            font_size=13, color=TEXT_DARK, wrap=True)

# Правый столбец — таблица
add_textbox(s2, col_x2, content_y, col_w2, Inches(0.36),
            "Рост размеров моделей", font_size=16, bold=True,
            color=DARK_BLUE, align=PP_ALIGN.LEFT)

add_table(s2, col_x2, content_y + Inches(0.4), col_w2, Inches(3.65),
          ["Модель", "Год", "Параметры", "Размер"],
          [
              ["GPT-2",        "2019", "1.5 млрд",  "~3 ГБ"],
              ["GPT-3",        "2020", "175 млрд",  "~350 ГБ"],
              ["LLaMA 2 7B",   "2023", "7 млрд",    "~13 ГБ"],
              ["LLaMA 3 8B",   "2024", "8 млрд",    "~15 ГБ"],
              ["LLaMA 3 70B",  "2024", "70 млрд",   "~140 ГБ"],
              ["Falcon 180B",  "2023", "180 млрд",  "~360 ГБ"],
          ],
          font_size=13, header_size=13)

add_textbox(s2, col_x2, content_y + Inches(4.12), col_w2, Inches(0.28),
            "↑ +40× рост за 5 лет при использовании fp16",
            font_size=11, bold=False, color=RGBColor(0x80,0x80,0x80), italic=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 3 — ЦЕЛЬ И ЗАДАЧИ
# ═══════════════════════════════════════════════════════════════════════════════
s3 = add_slide()
set_bg(s3, WHITE)
slide_header(s3, "Цель и задачи работы")

# Цель
add_rect(s3, Inches(0.3), Inches(1.3), W - Inches(0.6), Inches(0.96),
         fill_color=RGBColor(0xE8, 0xEA, 0xF6))
add_rect(s3, Inches(0.3), Inches(1.3), Inches(0.07), Inches(0.96),
         fill_color=DARK_BLUE)
add_textbox(s3, Inches(0.5), Inches(1.36), W - Inches(0.8), Inches(0.3),
            "Цель:", font_size=14, bold=True, color=DARK_BLUE)
add_textbox(s3, Inches(0.5), Inches(1.66), W - Inches(0.8), Inches(0.52),
            "Разработка архитектуры распределённого кэширования ML-моделей для serverless-инференса "
            "в Kubernetes, сокращающей задержку холодного старта и снижающей нагрузку на внешние репозитории.",
            font_size=13, color=TEXT_DARK, wrap=True)

# Задачи в двух колонках
tasks_y = Inches(2.45)
tasks_l = [
    "Анализ причин холодного старта и масштаба проблемы",
    "Исследование существующих решений (Alluxio, JuiceFS, Dragonfly, CubeFS, Ceph)",
    "Разработка NFS-этапа с координацией через файловые блокировки и Kubernetes Lease",
    "Проектирование P2P/FUSE-архитектуры с трёхуровневой иерархией кэша",
    "Реализация storage-agent как DaemonSet на каждой worker-ноде",
]
tasks_r = [
    "Реализация storage-mounter — FUSE-клиента с lazy loading",
    "Выбор механизма обнаружения узлов: Redis heartbeat vs Gossip vs mDNS",
    "Проектирование Redis-реестра метаданных чанков с TTL",
    "Анализ надёжности и сценариев отказов",
    "Формирование методики оценки эффективности",
]

col_mid = W / 2
for i, task in enumerate(tasks_l):
    ty = tasks_y + Inches(i * 0.95)
    add_rect(s3, Inches(0.3), ty, Inches(0.3), Inches(0.34),
             fill_color=DARK_BLUE)
    add_textbox(s3, Inches(0.34), ty + Inches(0.01), Inches(0.22), Inches(0.30),
                str(i+1), font_size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_textbox(s3, Inches(0.72), ty, col_mid - Inches(0.85), Inches(0.82),
                task, font_size=13, color=TEXT_DARK, wrap=True)

for i, task in enumerate(tasks_r):
    ty = tasks_y + Inches(i * 0.95)
    add_rect(s3, col_mid + Inches(0.1), ty, Inches(0.3), Inches(0.34),
             fill_color=LIGHT_BLUE)
    add_textbox(s3, col_mid + Inches(0.14), ty + Inches(0.01), Inches(0.22), Inches(0.30),
                str(i+6), font_size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_textbox(s3, col_mid + Inches(0.52), ty, col_mid - Inches(0.75), Inches(0.82),
                task, font_size=13, color=TEXT_DARK, wrap=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 4 — ИСХОДНАЯ АРХИТЕКТУРА
# ═══════════════════════════════════════════════════════════════════════════════
s4 = add_slide()
set_bg(s4, WHITE)
slide_header(s4, "Исходная архитектура", "storage-initializer + emptyDir — текущая практика")

# Блок-схема архитектуры (текстовая)
arch_x = Inches(0.3)
arch_y = Inches(1.3)
arch_w = Inches(7.3)
arch_h = Inches(5.9)
add_rect(s4, arch_x, arch_y, arch_w, arch_h,
         fill_color=RGBColor(0xF8, 0xF9, 0xFF),
         line_color=RGBColor(0xC5, 0xCA, 0xE9), line_width=Pt(1))

add_textbox(s4, arch_x + Inches(0.15), arch_y + Inches(0.1), arch_w - Inches(0.3), Inches(0.3),
            "Жизненный цикл пода при холодном старте",
            font_size=13, bold=True, color=DARK_BLUE)

# Шаги
steps = [
    ("1", "Scheduler помещает Pod на worker-ноду",       LIGHT_BLUE),
    ("2", "storage-initializer стартует, подключается к HuggingFace Hub", LIGHT_BLUE),
    ("3", "Скачивание весов модели в emptyDir  (~75 с для 15 ГБ)", ACCENT_RED),
    ("4", "runtime-container монтирует emptyDir и загружает модель в GPU", LIGHT_BLUE),
    ("5", "Pod готов к инференсу  (T_model_ready ≈ 75–180 с)", ACCENT_RED),
]
for i, (num, text, col) in enumerate(steps):
    sy = arch_y + Inches(0.55 + i * 0.97)
    add_rect(s4, arch_x + Inches(0.25), sy, Inches(0.36), Inches(0.36), fill_color=col)
    add_textbox(s4, arch_x + Inches(0.28), sy + Inches(0.01), Inches(0.3), Inches(0.3),
                num, font_size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_textbox(s4, arch_x + Inches(0.72), sy, arch_w - Inches(0.9), Inches(0.55),
                text, font_size=14, color=TEXT_DARK, wrap=True)
    if i < 4:
        add_textbox(s4, arch_x + Inches(0.35), sy + Inches(0.37), Inches(0.18), Inches(0.3),
                    "↓", font_size=13, color=MID_GRAY)

# Правый столбец — проблемы
prob_x = Inches(7.85)
prob_w = W - prob_x - Inches(0.3)
prob_y = Inches(1.3)

add_textbox(s4, prob_x, prob_y, prob_w, Inches(0.36),
            "Проблемы подхода", font_size=16, bold=True, color=DARK_BLUE)

problems = [
    ("❌  Нет переиспользования", "Каждый Pod скачивает модель\nзаново из интернета"),
    ("❌  Огромный трафик", "N реплик = N × размер модели\n10 × 15 ГБ = 150 ГБ"),
    ("❌  Нет lazy loading", "T_first_byte = T_model_ready\nИнференс ждёт полной загрузки"),
    ("❌  Зависимость от HF Hub", "Недоступность репозитория\n→ полная остановка"),
    ("❌  SLA невыполним", "p99 > 75 с при scale-to-zero"),
]
for i, (title, desc) in enumerate(problems):
    py = prob_y + Inches(0.45 + i * 1.1)
    add_rect(s4, prob_x, py, prob_w, Inches(1.0),
             fill_color=RGBColor(0xFF, 0xF0, 0xF0))
    add_rect(s4, prob_x, py, Inches(0.06), Inches(1.0), fill_color=ACCENT_RED)
    add_textbox(s4, prob_x + Inches(0.12), py + Inches(0.06),
                prob_w - Inches(0.15), Inches(0.3),
                title, font_size=13, bold=True, color=ACCENT_RED)
    add_textbox(s4, prob_x + Inches(0.12), py + Inches(0.38),
                prob_w - Inches(0.15), Inches(0.52),
                desc, font_size=12, color=TEXT_DARK, wrap=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 5 — ТРЕБОВАНИЯ К АРХИТЕКТУРЕ
# ═══════════════════════════════════════════════════════════════════════════════
s5 = add_slide()
set_bg(s5, WHITE)
slide_header(s5, "Требования к архитектуре")

col_x1 = Inches(0.3)
col_w1 = Inches(6.1)
col_x2 = Inches(6.73)
col_w2 = Inches(6.3)
ry = Inches(1.32)

add_rect(s5, col_x1, ry, col_w1, Inches(0.36), fill_color=DARK_BLUE)
add_textbox(s5, col_x1 + Inches(0.1), ry + Inches(0.04), col_w1 - Inches(0.2), Inches(0.3),
            "Функциональные", font_size=14, bold=True, color=WHITE)

func_reqs = [
    "Переиспользование весов между запусками (кэш на ноде)",
    "P2P-передача чанков между нодами без внешнего источника",
    "Стандартный POSIX-интерфейс для ML-runtime (без изменений кода)",
    "Автоматический fallback на HuggingFace Hub при отсутствии кэша",
    "Совместимость с Kubernetes (DaemonSet, CSI, PVC)",
    "Атомарная запись чанков (tmp-файл + os.Rename) для консистентности",
]
for i, req in enumerate(func_reqs):
    fy = ry + Inches(0.44 + i * 0.77)
    add_rect(s5, col_x1, fy, col_w1, Inches(0.68),
             fill_color=LIGHT_GRAY if i % 2 == 0 else WHITE,
             line_color=RGBColor(0xE0,0xE0,0xE0), line_width=Pt(0.5))
    add_textbox(s5, col_x1 + Inches(0.08), fy + Inches(0.06),
                col_w1 - Inches(0.15), Inches(0.56),
                "✓  " + req, font_size=13, color=TEXT_DARK, wrap=True)

add_rect(s5, col_x2, ry, col_w2, Inches(0.36), fill_color=LIGHT_BLUE)
add_textbox(s5, col_x2 + Inches(0.1), ry + Inches(0.04), col_w2 - Inches(0.2), Inches(0.3),
            "Нефункциональные (с целевыми значениями)", font_size=14, bold=True, color=WHITE)

nonfunc = [
    ("T_model_ready, local cache hit",      "≤ 3 с",     "для 15 ГБ модели"),
    ("T_first_byte, lazy FUSE loading",     "< 1 с",     "принципиально ≠ baseline"),
    ("Внешний трафик при N=10 репликах",   "= 1× модель","не N×"),
    ("Отказ одной worker-ноды",            "graceful",   "без полной остановки"),
    ("Overhead FUSE, последов. чтение",    "≤ 0.5%",    "CPU при 16-МБ чанках"),
    ("Redis lookup latency",               "p99 < 5 мс", "p50 < 1 мс"),
]
for i, (metric, value, note) in enumerate(nonfunc):
    ny = ry + Inches(0.44 + i * 0.77)
    add_rect(s5, col_x2, ny, col_w2, Inches(0.68),
             fill_color=LIGHT_GRAY if i % 2 == 0 else WHITE,
             line_color=RGBColor(0xE0,0xE0,0xE0), line_width=Pt(0.5))
    add_textbox(s5, col_x2 + Inches(0.08), ny + Inches(0.06),
                Inches(3.1), Inches(0.56),
                metric, font_size=12, color=TEXT_DARK, wrap=True)
    add_textbox(s5, col_x2 + Inches(3.2), ny + Inches(0.06),
                Inches(1.6), Inches(0.3),
                value, font_size=14, bold=True, color=ACCENT_GREEN, wrap=False)
    add_textbox(s5, col_x2 + Inches(3.2), ny + Inches(0.36),
                Inches(2.9), Inches(0.26),
                note, font_size=10, color=DARK_GRAY, italic=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 6 — СТЕК ТЕХНОЛОГИЙ
# ═══════════════════════════════════════════════════════════════════════════════
s6 = add_slide()
set_bg(s6, WHITE)
slide_header(s6, "Стек технологий")

techs = [
    ("Kubernetes",     "Оркестрация: DaemonSet для storage-agent,\nPVC и CSI-интеграция",            DARK_BLUE),
    ("Go",             "Реализация storage-agent и storage-mounter;\nbazefuse (go-fuse) библиотека", LIGHT_BLUE),
    ("Redis",          "Реестр метаданных чанков: TTL-записи,\nheartbeat агентов, Sentinel/Cluster",  RGBColor(0xCC, 0x00, 0x00)),
    ("FUSE (Linux)",   "Виртуальная ФС для прозрачного доступа\nML-runtime к чанкам без изменений",  RGBColor(0x33, 0x69, 0xE8)),
    ("Docker",         "Контейнеризация компонентов;\nbase-образ для agent и mounter",               RGBColor(0x00, 0x91, 0xE2)),
    ("HuggingFace Hub","Внешний репозиторий весов моделей;\nfallback-источник при отсутствии кэша",  RGBColor(0xFF, 0x97, 0x00)),
    ("NFS",            "Промежуточный этап: общий том с\nflock + Kubernetes Lease Leader Election",   RGBColor(0x43, 0xA0, 0x47)),
    ("Prometheus",     "Мониторинг: hit rate, latency по уровням,\nвнешний трафик, Redis метрики",    RGBColor(0xE6, 0x52, 0x2C)),
]

cols_n = 4
card_w = (W - Inches(0.5)) / cols_n - Inches(0.12)
card_h = Inches(2.4)
start_x = Inches(0.28)
row_y = [Inches(1.32), Inches(3.9)]

for i, (name, desc, color) in enumerate(techs):
    col = i % cols_n
    row = i // cols_n
    cx = start_x + col * (card_w + Inches(0.13))
    cy = row_y[row]

    add_rect(s6, cx, cy, card_w, card_h,
             fill_color=WHITE,
             line_color=RGBColor(0xE0, 0xE0, 0xE0), line_width=Pt(1))
    # Цветная полоса сверху
    add_rect(s6, cx, cy, card_w, Inches(0.1), fill_color=color)
    # Название
    add_textbox(s6, cx + Inches(0.1), cy + Inches(0.16),
                card_w - Inches(0.2), Inches(0.46),
                name, font_size=15, bold=True, color=color)
    # Описание
    add_textbox(s6, cx + Inches(0.1), cy + Inches(0.7),
                card_w - Inches(0.2), Inches(1.55),
                desc, font_size=12, color=DARK_GRAY, wrap=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 7 — ПРЕДЛОЖЕННАЯ АРХИТЕКТУРА
# ═══════════════════════════════════════════════════════════════════════════════
s7 = add_slide()
set_bg(s7, WHITE)
slide_header(s7, "Предложенная архитектура", "storage-agent + storage-mounter + Redis Cluster")

# Левая часть — описание компонентов
lx = Inches(0.3)
lw = Inches(5.8)
ly = Inches(1.32)

components = [
    ("storage-agent  (DaemonSet)",
     "Запускается на каждой ноде · управляет локальным chunk-кэшем на NVMe · "
     "отвечает на запросы mounter через UDS · отдаёт чанки соседям по TCP",
     DARK_BLUE),
    ("storage-mounter  (FUSE-клиент)",
     "Монтирует виртуальную ФС в Pod · ML-runtime видит обычные файлы · "
     "lazy loading: первый байт < 1 с до полной загрузки · трансляция read() → chunk-запросы",
     LIGHT_BLUE),
    ("Redis Cluster  (Control Plane)",
     "Хранит: какие чанки, на каких нодах, с каким TTL · агенты публикуют heartbeat "
     "каждые 10 с · TTL = 30 с → автоматическая очистка при отказе ноды",
     RGBColor(0xCC, 0x00, 0x00)),
]
for i, (name, desc, color) in enumerate(components):
    cy = ly + Inches(i * 1.7)
    add_rect(s7, lx, cy, lw, Inches(1.55), fill_color=WHITE,
             line_color=color, line_width=Pt(1.5))
    add_rect(s7, lx, cy, Inches(0.08), Inches(1.55), fill_color=color)
    add_textbox(s7, lx + Inches(0.16), cy + Inches(0.1),
                lw - Inches(0.22), Inches(0.36),
                name, font_size=14, bold=True, color=color)
    add_textbox(s7, lx + Inches(0.16), cy + Inches(0.46),
                lw - Inches(0.22), Inches(0.98),
                desc, font_size=12, color=TEXT_DARK, wrap=True)

# Правая часть — алгоритм чтения
rx = Inches(6.35)
rw = W - rx - Inches(0.3)
ry_top = Inches(1.32)

add_textbox(s7, rx, ry_top, rw, Inches(0.36),
            "Алгоритм чтения чанка", font_size=15, bold=True, color=DARK_BLUE)

algo_steps = [
    ("1",  "Локальный кэш (NVMe)",    "2.3 мс",   ACCENT_GREEN,   "✓ hit → вернуть данные"),
    ("↓",  "miss",                     "",          MID_GRAY,       ""),
    ("2",  "Соседняя нода (P2P/TCP)",  "13.3 мс",  ACCENT_YELLOW,  "✓ hit → вернуть + закэшировать"),
    ("↓",  "miss",                     "",          MID_GRAY,       ""),
    ("3",  "HuggingFace Hub (fallback)","≥ 130 мс", ACCENT_RED,    "скачать → закэшировать"),
]
step_y = ry_top + Inches(0.42)
for item in algo_steps:
    num, label, timing, color, note = item
    if num == "↓":
        add_textbox(s7, rx + Inches(0.3), step_y, rw, Inches(0.3),
                    "↓  " + label, font_size=11, color=MID_GRAY, italic=True)
        step_y += Inches(0.28)
    else:
        add_rect(s7, rx, step_y, rw, Inches(0.82),
                 fill_color=RGBColor(0xF5, 0xF5, 0xFF) if color != ACCENT_RED
                 else RGBColor(0xFF, 0xF0, 0xF0))
        add_rect(s7, rx, step_y, Inches(0.07), Inches(0.82), fill_color=color)
        add_textbox(s7, rx + Inches(0.14), step_y + Inches(0.06),
                    Inches(0.22), Inches(0.28),
                    num, font_size=13, bold=True, color=color)
        add_textbox(s7, rx + Inches(0.38), step_y + Inches(0.06),
                    rw - Inches(2.0), Inches(0.28),
                    label, font_size=13, bold=True, color=TEXT_DARK)
        add_textbox(s7, rx + rw - Inches(1.7), step_y + Inches(0.06),
                    Inches(1.62), Inches(0.28),
                    timing, font_size=13, bold=True, color=color, align=PP_ALIGN.RIGHT)
        if note:
            add_textbox(s7, rx + Inches(0.38), step_y + Inches(0.4),
                        rw - Inches(0.45), Inches(0.28),
                        note, font_size=11, color=DARK_GRAY, italic=True)
        step_y += Inches(0.9)

# UDS vs TCP
add_textbox(s7, rx, step_y + Inches(0.1), rw, Inches(0.3),
            "Транспорт: UDS (та же нода) · TCP (соседние ноды)",
            font_size=11, color=DARK_GRAY, italic=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 8 — НАГРУЗОЧНОЕ ТЕСТИРОВАНИЕ: СТЕНД
# ═══════════════════════════════════════════════════════════════════════════════
s8 = add_slide()
set_bg(s8, WHITE)
slide_header(s8, "Нагрузочное тестирование", "Конфигурация стенда и сценарии")

# Левый блок — конфигурация
lx = Inches(0.3)
lw = Inches(5.8)
add_rect(s8, lx, Inches(1.32), lw, Inches(0.36), fill_color=DARK_BLUE)
add_textbox(s8, lx + Inches(0.1), Inches(1.36), lw - Inches(0.2), Inches(0.3),
            "Тестовый стенд", font_size=14, bold=True, color=WHITE)

bench_items = [
    ("Ноды",         "6 × Intel Xeon Silver  16c/32t · 64 ГБ RAM"),
    ("Диск",         "Samsung 980 Pro NVMe 2 ТБ  (seq. read 7 000 МБ/с)"),
    ("Сеть",         "10 Гбит/с Ethernet · RTT между нодами ≤ 0.5 мс"),
    ("Redis",        "1 master + 2 replica · отдельная нода"),
    ("Llama 3 8B",   "15 ГБ · 960 чанков × 16 МБ"),
    ("Mistral 7B",   "14 ГБ · 896 чанков × 16 МБ"),
    ("Llama 3 70B",  "140 ГБ · 8 960 чанков × 16 МБ"),
]
for i, (key, val) in enumerate(bench_items):
    by = Inches(1.78 + i * 0.66)
    bg = LIGHT_GRAY if i % 2 == 0 else WHITE
    add_rect(s8, lx, by, lw, Inches(0.6), fill_color=bg,
             line_color=RGBColor(0xE0,0xE0,0xE0), line_width=Pt(0.5))
    add_textbox(s8, lx + Inches(0.1), by + Inches(0.08),
                Inches(1.3), Inches(0.42),
                key, font_size=12, bold=True, color=DARK_BLUE)
    add_textbox(s8, lx + Inches(1.45), by + Inches(0.08),
                lw - Inches(1.55), Inches(0.42),
                val, font_size=12, color=TEXT_DARK, wrap=True)

# Правый блок — сценарии
rx = Inches(6.35)
rw = W - rx - Inches(0.3)
add_rect(s8, rx, Inches(1.32), rw, Inches(0.36), fill_color=LIGHT_BLUE)
add_textbox(s8, rx + Inches(0.1), Inches(1.36), rw - Inches(0.2), Inches(0.3),
            "Сценарии тестирования", font_size=14, bold=True, color=WHITE)

scenarios = [
    ("Cold cluster",        "Кэш пуст, Redis пуст\n→ первый запуск в кластере",         ACCENT_RED),
    ("Warm (same node)",    "Модель уже есть на той же ноде\n→ local cache hit",         ACCENT_GREEN),
    ("Warm (peer node)",    "Модель есть на соседней ноде\n→ P2P peer cache hit",        ACCENT_YELLOW),
    ("Burst ×10",           "10 подов стартуют одновременно\n→ измерение трафика и p99", LIGHT_BLUE),
]
for i, (name, desc, color) in enumerate(scenarios):
    sy = Inches(1.78 + i * 1.37)
    add_rect(s8, rx, sy, rw, Inches(1.25),
             fill_color=WHITE, line_color=color, line_width=Pt(1.5))
    add_rect(s8, rx, sy, Inches(0.07), Inches(1.25), fill_color=color)
    add_textbox(s8, rx + Inches(0.16), sy + Inches(0.1),
                rw - Inches(0.22), Inches(0.34),
                name, font_size=14, bold=True, color=color)
    add_textbox(s8, rx + Inches(0.16), sy + Inches(0.48),
                rw - Inches(0.22), Inches(0.66),
                desc, font_size=13, color=TEXT_DARK, wrap=True)

# Метрики
add_textbox(s8, lx, Inches(6.46), W - Inches(0.6), Inches(0.28),
            "Метрики: T_model_ready (p50, p99)  ·  T_first_byte  ·  внешний трафик V_ext  ·  Redis latency  ·  CPU overhead FUSE",
            font_size=11, color=DARK_GRAY, italic=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 9 — РЕЗУЛЬТАТЫ
# ═══════════════════════════════════════════════════════════════════════════════
s9 = add_slide()
set_bg(s9, WHITE)
slide_header(s9, "Результаты тестирования", "Модель Llama 3 8B (15 ГБ) · 6 worker-нод · NVMe 7 ГБ/с · 10 Гбит/с")

# Таблица сравнения
add_table(s9, Inches(0.3), Inches(1.32), W - Inches(0.6), Inches(3.3),
          ["Показатель", "emptyDir (baseline)", "NFS", "P2P / FUSE"],
          [
              ["T_model_ready, cold cluster",          "~75 с",   "~75 с",  "~75 с"],
              ["T_model_ready, warm (same node)",       "~75 с",   "~12 с",  "~2 с  ✓"],
              ["T_model_ready, warm (peer node)",       "~75 с",   "~12 с",  "~12 с ✓"],
              ["T_first_byte",                          "~75 с",   "~75 с",  "< 1 с ✓"],
              ["Внешний трафик, N = 10 реплик",         "150 ГБ",  "15 ГБ",  "15 ГБ ✓"],
              ["SPOF",                                  "нет",     "NFS-сервер", "Redis (HA → нет)"],
              ["Деградация при отказе",                 "нет",     "полная", "graceful"],
              ["Redis lookup p50 / p99",                "—",       "—",      "< 1 мс / < 5 мс"],
              ["CPU overhead FUSE",                     "—",       "—",      "< 0.5 %"],
          ],
          header_bg=DARK_BLUE, font_size=12, header_size=12)

# Карточки ключевых метрик
card_y = Inches(4.8)
card_h_val = Inches(1.42)
metrics = [
    ("×36",   "ускорение загрузки\nlocal cache vs HuggingFace",   ACCENT_GREEN),
    ("×6",    "ускорение загрузки\npeer cache vs HuggingFace",     ACCENT_GREEN),
    ("×10",   "снижение\nвнешнего трафика\n(N=10 реплик)",         ACCENT_GREEN),
    ("< 1 с", "T_first_byte\nlazy FUSE loading",                   LIGHT_BLUE),
    ("×30",   "снижение AMAT\nпосле прогрева\n(130 мс → 4.3 мс)", ACCENT_GREEN),
]
card_w_m = (W - Inches(0.5)) / len(metrics) - Inches(0.1)
for i, (val, lbl, color) in enumerate(metrics):
    cx = Inches(0.28) + i * (card_w_m + Inches(0.1))
    metric_card(s9, cx, card_y, card_w_m, card_h_val, val, lbl, value_color=color)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 10 — НАДЁЖНОСТЬ
# ═══════════════════════════════════════════════════════════════════════════════
s10 = add_slide()
set_bg(s10, WHITE)
slide_header(s10, "Анализ надёжности", "Graceful degradation vs. полная остановка при NFS")

scenarios_fault = [
    (
        "Отказ worker-ноды",
        "TTL-записи агента истекают через 30 с → Redis автоматически удаляет их.\n"
        "Затронуты только чанки без репликации на других нодах.\n"
        "При r=2: P(потери чанка) = 10⁻⁴  ·  при r=3: P = 10⁻⁶",
        "⚠  Деградация к fallback, не остановка",
        ACCENT_YELLOW,
    ),
    (
        "Недоступность Redis",
        "Агент теряет peer discovery — не видит соседей.\n"
        "Система деградирует: local cache → HuggingFace (без P2P).\n"
        "При HA-конфигурации (Sentinel 1+2) вероятность полного отказа ≈ 0.",
        "✓  Сервис продолжает работу при наличии локального кэша",
        ACCENT_GREEN,
    ),
    (
        "Недоступность HuggingFace Hub",
        "Чанки из local / peer cache — запрос обслуживается без HF Hub.\n"
        "Прогретый кластер полностью изолирован от внешнего источника.\n"
        "При полном отсутствии кэша — ошибка (аналогично baseline).",
        "✓  Прогретый кластер работает автономно",
        ACCENT_GREEN,
    ),
]

card_y2 = Inches(1.32)
card_h2 = Inches(1.88)
card_w2 = W - Inches(0.6)

for i, (title, desc, result, color) in enumerate(scenarios_fault):
    cy = card_y2 + Inches(i * 2.0)
    add_rect(s10, Inches(0.3), cy, card_w2, card_h2,
             fill_color=WHITE, line_color=color, line_width=Pt(1.5))
    add_rect(s10, Inches(0.3), cy, Inches(0.08), card_h2, fill_color=color)
    add_textbox(s10, Inches(0.48), cy + Inches(0.1),
                Inches(4.5), Inches(0.34),
                f"Сценарий {i+1}: {title}",
                font_size=14, bold=True, color=color)
    add_textbox(s10, Inches(0.48), cy + Inches(0.5),
                card_w2 - Inches(3.0), Inches(1.2),
                desc, font_size=12, color=TEXT_DARK, wrap=True)
    # Результат справа
    add_rect(s10, Inches(0.3) + card_w2 - Inches(2.85), cy + Inches(0.28),
             Inches(2.75), Inches(1.32),
             fill_color=RGBColor(0xE8,0xF5,0xE9) if color == ACCENT_GREEN
             else RGBColor(0xFF,0xF8,0xE1))
    add_textbox(s10, Inches(0.3) + card_w2 - Inches(2.78), cy + Inches(0.45),
                Inches(2.6), Inches(0.98),
                result, font_size=12, bold=True, color=color, wrap=True,
                align=PP_ALIGN.CENTER)

# Итог сравнения с NFS
add_rect(s10, Inches(0.3), Inches(7.05), card_w2, Inches(0.22),
         fill_color=RGBColor(0xE8,0xEA,0xF6))
add_textbox(s10, Inches(0.4), Inches(7.06), card_w2 - Inches(0.1), Inches(0.2),
            "NFS при любом отказе сервера → полная остановка  ·  P2P/FUSE → graceful degradation",
            font_size=11, bold=True, color=DARK_BLUE, italic=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 11 — ИТОГИ И ВКЛАД
# ═══════════════════════════════════════════════════════════════════════════════
s11 = add_slide()
set_bg(s11, WHITE)
slide_header(s11, "Итоги и практическая ценность")

# Выполненные задачи — чеклист
lx = Inches(0.3)
lw = Inches(7.5)
add_textbox(s11, lx, Inches(1.32), lw, Inches(0.32),
            "Выполненные задачи", font_size=15, bold=True, color=DARK_BLUE)

done = [
    "Проведён анализ причин и масштаба проблемы cold start в serverless ML inference",
    "Исследованы и сравнены 5 существующих решений (Alluxio, JuiceFS, Dragonfly, CubeFS, Ceph)",
    "Разработан NFS-этап с Leader Election через Kubernetes Lease",
    "Спроектирована P2P/FUSE-архитектура с трёхуровневой иерархией кэша",
    "Реализованы storage-agent (DaemonSet, HTTP API, singleflight) и storage-mounter (FUSE)",
    "Обоснован выбор Redis heartbeat vs Gossip vs mDNS",
    "Проведён теоретический анализ: AMAT, Закон Литтла, Амдал, Ципф",
    "Сформирована методика оценки эффективности с расчётными значениями",
]
for i, text in enumerate(done):
    dy = Inches(1.7 + i * 0.62)
    add_rect(s11, lx, dy, Inches(0.3), Inches(0.3),
             fill_color=ACCENT_GREEN)
    add_textbox(s11, lx + Inches(0.06), dy + Inches(0.01), Inches(0.18), Inches(0.26),
                "✓", font_size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_textbox(s11, lx + Inches(0.38), dy, lw - Inches(0.42), Inches(0.54),
                text, font_size=13, color=TEXT_DARK, wrap=True)

# Правый блок — практическая ценность
rx = Inches(8.05)
rw = W - rx - Inches(0.3)
add_textbox(s11, rx, Inches(1.32), rw, Inches(0.32),
            "Практическая ценность", font_size=15, bold=True, color=DARK_BLUE)

value_cards = [
    ("135 ГБ",  "экономия внешнего трафика\nпри 10 репликах Llama 3 8B",  ACCENT_GREEN),
    ("×36",     "ускорение загрузки модели\nв прогретом кластере",         ACCENT_GREEN),
    ("< 1 с",   "T_first_byte с lazy FUSE\n(было: 75 с)",                  LIGHT_BLUE),
    ("0 SPOF",  "устранение NFS как\nединой точки отказа",                 DARK_BLUE),
]
card_w_v = (rw - Inches(0.15)) / 2 - Inches(0.08)
card_h_v = Inches(1.55)
for i, (val, lbl, color) in enumerate(value_cards):
    row = i // 2
    col = i % 2
    vx = rx + col * (card_w_v + Inches(0.1))
    vy = Inches(1.7) + row * Inches(1.65)
    metric_card(s11, vx, vy, card_w_v, card_h_v, val, lbl, value_color=color)

# Нижняя подпись
add_rect(s11, rx, Inches(5.05), rw, Inches(2.0),
         fill_color=RGBColor(0xE8, 0xEA, 0xF6))
add_rect(s11, rx, Inches(5.05), Inches(0.07), Inches(2.0), fill_color=DARK_BLUE)
add_textbox(s11, rx + Inches(0.14), Inches(5.12), rw - Inches(0.2), Inches(1.82),
            "Предложенная система совместима с существующими "
            "Kubernetes-кластерами без изменения кода ML-runtime. "
            "Развёртывание ограничивается установкой DaemonSet "
            "и монтированием FUSE-тома в целевые поды.",
            font_size=13, color=TEXT_DARK, wrap=True)


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 12 — ДАЛЬНЕЙШЕЕ РАЗВИТИЕ
# ═══════════════════════════════════════════════════════════════════════════════
s12 = add_slide()
set_bg(s12, DARK_BLUE)

# Верхняя зелёная линия
add_rect(s12, 0, 0, W, Inches(0.06), fill_color=ACCENT_GREEN)

add_textbox(s12, Inches(0.5), Inches(0.25), W - Inches(1.0), Inches(0.5),
            "Направления дальнейшего развития",
            font_size=26, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

future = [
    ("01", "Полноценный P2P",         "Gossip-based peer discovery как альтернатива Redis\nдля сред без персистентного хранилища"),
    ("02", "mTLS между агентами",      "Аутентификация TCP-соединений для production;\nавторизация Redis через ACL"),
    ("03", "Cache warming",            "Предзагрузка популярных моделей по расписанию;\nZipf-прогнозирование горячих чанков"),
    ("04", "CSI-плагин",               "Нативная интеграция с Kubernetes PVC;\navoidance of manual FUSE mount"),
    ("05", "Доп. источники моделей",   "Поддержка Ollama и ModelScope\nпомимо HuggingFace Hub"),
    ("06", "GPU-кластер валидация",    "Экспериментальная проверка на реальном\nGPU-кластере с vLLM / LLaMA.cpp"),
]

card_w_f = (W - Inches(0.5)) / 3 - Inches(0.12)
card_h_f = Inches(2.1)
row_fy = [Inches(0.95), Inches(3.2)]

for i, (num, title, desc) in enumerate(future):
    col = i % 3
    row = i // 3
    fx = Inches(0.26) + col * (card_w_f + Inches(0.14))
    fy = row_fy[row]
    add_rect(s12, fx, fy, card_w_f, card_h_f,
             fill_color=MED_BLUE)
    add_rect(s12, fx, fy, card_w_f, Inches(0.07), fill_color=ACCENT_GREEN)
    add_textbox(s12, fx + Inches(0.12), fy + Inches(0.14),
                Inches(0.5), Inches(0.42),
                num, font_size=20, bold=True, color=ACCENT_GREEN)
    add_textbox(s12, fx + Inches(0.12), fy + Inches(0.55),
                card_w_f - Inches(0.18), Inches(0.36),
                title, font_size=14, bold=True, color=WHITE)
    add_textbox(s12, fx + Inches(0.12), fy + Inches(0.93),
                card_w_f - Inches(0.18), Inches(1.0),
                desc, font_size=11, color=MID_GRAY, wrap=True)

# Заключительная фраза
add_rect(s12, Inches(0.5), Inches(5.45), W - Inches(1.0), Inches(1.35),
         fill_color=RGBColor(0x0D, 0x14, 0x4F))
add_rect(s12, Inches(0.5), Inches(5.45), Inches(0.07), Inches(1.35),
         fill_color=ACCENT_GREEN)
add_textbox(s12, Inches(0.7), Inches(5.55), W - Inches(1.2), Inches(1.1),
            "Система позволяет сократить задержку холодного старта на порядок "
            "при отсутствии деградации надёжности — что критично для "
            "production serverless ML inference.",
            font_size=16, bold=False, color=WHITE, align=PP_ALIGN.CENTER, wrap=True)

# Нижняя подпись
add_textbox(s12, Inches(0.3), H - Inches(0.32), W - Inches(0.6), Inches(0.28),
            "Блинов М.А.  ·  МАИ  ·  02.04.02  ·  2025",
            font_size=10, color=MID_GRAY, align=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════════════
# СОХРАНЕНИЕ
# ═══════════════════════════════════════════════════════════════════════════════
out_path = "/Users/mablinov/Documents/Diploma/pptx/diploma_presentation.pptx"
prs.save(out_path)
print(f"Saved: {out_path}  ({prs.slides.__len__()} slides)")
