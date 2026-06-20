"""
generate3.py — финальная версия презентации диплома с встроенными графиками.

Графики (6 штук) сохраняются в pptx/charts/ и вставляются в слайды:
  Слайд 2  → chart_model_sizes.png          (рост размеров ML-моделей)
  Слайд 4  → chart_cold_start_breakdown.png  (фазы холодного старта)
  Слайд 9  → chart_tmodel_ready.png          (T_model_ready по сценариям)
             chart_external_traffic.png      (внешний трафик при масштабировании)
  Слайд 10 → chart_availability.png          (доступность при репликации)
             chart_reliability.png           (деградация при отказах)

Запуск: python3 generate3.py
Результат: final-pptx-v2.pptx  +  charts/*.png
"""

import io, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import LogLocator, LogFormatter
import numpy as np
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

HERE      = os.path.dirname(os.path.abspath(__file__))
CHARTS    = os.path.join(HERE, "charts")
os.makedirs(CHARTS, exist_ok=True)
OUT       = os.path.join(HERE, "final-pptx-v2.pptx")

# ── Презентация ───────────────────────────────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(10.0)
prs.slide_height = Inches(5.625)
blank_layout = prs.slide_layouts[6]
FONT = "Roboto"

# ── Палитра ───────────────────────────────────────────────────────────────────
BLACK  = RGBColor(0x00,0x00,0x00); WHITE  = RGBColor(0xFF,0xFF,0xFF)
LGRAY  = RGBColor(0xF3,0xF3,0xF3); DGRAY  = RGBColor(0x42,0x42,0x42)
GRAY   = RGBColor(0x9E,0x9E,0x9E)
GREEN  = RGBColor(0x15,0x81,0x58); BLUE   = RGBColor(0x05,0x8D,0xC7)
RED    = RGBColor(0xC6,0x28,0x28); ORANGE = RGBColor(0xE6,0x8A,0x00)
LBLUE  = RGBColor(0xE3,0xF2,0xFD); LGREEN = RGBColor(0xE8,0xF5,0xE9)

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"

# ═══════════════════════════════════════════════════════════════════════════════
# PPTX HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def new_slide():
    s = prs.slides.add_slide(blank_layout)
    bg = s.background; fill = bg.fill; fill.solid(); fill.fore_color.rgb = WHITE
    return s

def rect(slide, x, y, w, h, fill=None, line=None):
    s = slide.shapes.add_shape(1, x, y, w, h)
    if fill: s.fill.solid(); s.fill.fore_color.rgb = fill
    else:    s.fill.background()
    if line: s.line.color.rgb = line
    else:    s.line.fill.background()
    return s

def _para(runs, align="l", spc=0):
    """Build <a:p> from a list of run-dicts."""
    p = etree.Element(f"{{{A_NS}}}p")
    pPr = etree.SubElement(p, f"{{{A_NS}}}pPr")
    pPr.set("algn", align); pPr.set("indent","0"); pPr.set("marL","0")
    etree.SubElement(pPr, f"{{{A_NS}}}buNone")
    sb = etree.SubElement(pPr, f"{{{A_NS}}}spcBef")
    etree.SubElement(sb, f"{{{A_NS}}}spcPts").set("val", str(spc))
    sa = etree.SubElement(pPr, f"{{{A_NS}}}spcAft")
    etree.SubElement(sa, f"{{{A_NS}}}spcPts").set("val","0")
    for rd in runs:
        txt = rd.get("text","")
        if not txt: continue
        r = etree.SubElement(p, f"{{{A_NS}}}r")
        rPr = etree.SubElement(r, f"{{{A_NS}}}rPr")
        rPr.set("lang","ru-RU"); rPr.set("sz", str(rd.get("sz",1800)))
        if rd.get("bold"):       rPr.set("b","1")
        if rd.get("italic"):     rPr.set("i","1")
        if rd.get("subscript"):  rPr.set("baseline","-25000")
        if rd.get("superscript"):rPr.set("baseline","30000")
        col = rd.get("color")
        if col:
            sf = etree.SubElement(rPr, f"{{{A_NS}}}solidFill")
            sc = etree.SubElement(sf,  f"{{{A_NS}}}srgbClr")
            sc.set("val", str(col).upper())
        for tag in ("latin","ea","cs"):
            etree.SubElement(rPr, f"{{{A_NS}}}{tag}").set("typeface", rd.get("font",FONT))
        etree.SubElement(r, f"{{{A_NS}}}t").text = txt
    return p

def E(spc=400):
    p = etree.Element(f"{{{A_NS}}}p")
    pPr = etree.SubElement(p, f"{{{A_NS}}}pPr")
    pPr.set("algn","l"); etree.SubElement(pPr, f"{{{A_NS}}}buNone")
    sb = etree.SubElement(pPr, f"{{{A_NS}}}spcBef")
    etree.SubElement(sb, f"{{{A_NS}}}spcPts").set("val", str(spc))
    etree.SubElement(etree.SubElement(pPr, f"{{{A_NS}}}spcAft"), f"{{{A_NS}}}spcPts").set("val","0")
    return p

def P(text, sz=1800, bold=False, italic=False, color=None, align="l", spc=0):
    return _para([{"text":text,"sz":sz,"bold":bold,"italic":italic,"color":color}],
                 align=align, spc=spc)

def Pm(*runs, align="l", spc=0):
    """Multi-run paragraph."""
    return _para(list(runs), align=align, spc=spc)

def sub(text, sz=1800, color=None):
    """Subscript run-dict (use inside Pm)."""
    return {"text":text,"sz":int(sz*0.72),"subscript":True,"color":color}

def run(text, sz=1800, bold=False, italic=False, color=None):
    return {"text":text,"sz":sz,"bold":bold,"italic":italic,"color":color}

def txbox(slide, x, y, w, h, paras, anchor="t"):
    shape = slide.shapes.add_textbox(x,y,w,h)
    tf = shape.text_frame; tf.word_wrap = True
    bodyPr = tf._txBody.find(qn("a:bodyPr"))
    bodyPr.set("anchor",anchor); bodyPr.set("anchorCtr","0")
    txBody = tf._txBody
    for old in txBody.findall(f"{{{A_NS}}}p"): txBody.remove(old)
    for p_elem in paras: txBody.append(p_elem)
    return shape

def title_box(slide, text):
    txbox(slide, Inches(0.341), Inches(0), Inches(9.318), Inches(1.0),
          [_para([run(text, sz=2800, bold=True)])], anchor="ctr")

def body_box(slide, paras, x=None,y=None,w=None,h=None,anchor="t"):
    txbox(slide,
          x if x is not None else Inches(0.451),
          y if y is not None else Inches(1.05),
          w if w is not None else Inches(9.133),
          h if h is not None else Inches(4.4),
          paras, anchor)

def tbl(slide, x,y,w,h, headers, rows, hdr_bg=GREEN,
        hdr_fg=WHITE, hdr_sz=12, row_sz=11, col_widths=None):
    nc, nr = len(headers), len(rows)+1
    t = slide.shapes.add_table(nr, nc, x, y, w, h).table
    if col_widths:
        for i,cw in enumerate(col_widths): t.columns[i].width = int(cw)
    else:
        cw = w//nc
        for col in t.columns: col.width = cw
    def cell(r,c,txt,bg,fg,bold=False,sz=row_sz):
        cl = t.cell(r,c); cl.fill.solid(); cl.fill.fore_color.rgb = bg
        p = cl.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.LEFT
        rn = p.add_run(); rn.text = str(txt)
        rn.font.size = Pt(sz); rn.font.bold = bold
        rn.font.color.rgb = fg; rn.font.name = FONT
    for c,h_ in enumerate(headers): cell(0,c,h_,hdr_bg,hdr_fg,True,hdr_sz)
    for r,row in enumerate(rows):
        bg = LGRAY if r%2==0 else WHITE
        for c,v in enumerate(row): cell(r+1,c,v,bg,BLACK,sz=row_sz)

def img(slide, data_bytes, x,y,w,h):
    slide.shapes.add_picture(io.BytesIO(data_bytes), x,y,w,h)

# ═══════════════════════════════════════════════════════════════════════════════
# CHART HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

STYLE = {
    "font.family":"DejaVu Sans","font.size":9,
    "axes.spines.top":False,"axes.spines.right":False,
    "axes.grid":True,"axes.grid.axis":"y","grid.alpha":0.35,
    "figure.facecolor":"white","axes.facecolor":"white",
}
C_RED  = "#C62828"; C_ORG  = "#E68A00"; C_GRN  = "#158158"
C_LBLU = "#1565C0"; C_GRAY = "#78909C"

def save(fig, name):
    path = os.path.join(CHARTS, name)
    fig.savefig(path, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    with open(path,"rb") as f: return f.read()


# ── 1. Рост размеров ML-моделей ───────────────────────────────────────────────
def chart_model_sizes():
    models = ["GPT-2\n2019","BERT\n2019","T5-11B\n2020","GPT-3\n2020",
              "LLaMA 1 7B\n2023","LLaMA 2 70B\n2023","Falcon 180B\n2023",
              "LLaMA 3 8B\n2024","LLaMA 3 70B\n2024","Mixtral 8×22B\n2024"]
    sizes  = [0.003, 0.42, 22, 350, 13, 140, 360, 15, 140, 281]  # GB (float32)
    colors_bar = [C_GRAY,C_GRAY,C_GRAY,C_ORG,
                  C_LBLU,C_LBLU,C_LBLU,
                  C_GRN,C_GRN,C_GRN]

    with plt.rc_context(STYLE):
        fig, ax = plt.subplots(figsize=(7.4,3.8))
        bars = ax.bar(range(len(models)), sizes, color=colors_bar,
                      width=0.65, zorder=3)
        ax.set_yscale("log")
        ax.set_yticks([0.001,0.01,0.1,1,10,100,1000])
        ax.set_yticklabels(["<1 МБ","10 МБ","100 МБ","1 ГБ","10 ГБ","100 ГБ","1 ТБ"])
        ax.set_xticks(range(len(models)))
        ax.set_xticklabels(models, fontsize=8)
        ax.set_ylabel("Размер весов (log-шкала)", fontsize=9)
        ax.set_title("Рост размеров ML-моделей, 2019–2024", fontsize=10, pad=6)
        ax.grid(axis="y", which="both", alpha=0.25)
        ax.set_ylim(0.001, 5000)  # extra headroom so labels don't clip
        for bar, sz in zip(bars, sizes):
            lbl = f"{sz:.0f} ГБ" if sz>=1 else f"{sz*1000:.0f} МБ"
            ax.text(bar.get_x()+bar.get_width()/2, sz*1.8,
                    lbl, ha="center", va="bottom", fontsize=7.5, rotation=0)
        # Легенда
        patches = [mpatches.Patch(color=C_GRAY,label="2019–2020"),
                   mpatches.Patch(color=C_LBLU,label="2023"),
                   mpatches.Patch(color=C_GRN, label="2024")]
        ax.legend(handles=patches, fontsize=8.5, loc="upper left")
        # Аннотация — текст на свободном месте (нижняя правая часть)
        ax.annotate("×40 000\nза 5 лет", xy=(6, 360), xytext=(4.2, 0.012),
                    fontsize=9, fontweight="bold", color=C_RED,
                    arrowprops=dict(arrowstyle="->", color=C_RED, lw=1.2,
                                   connectionstyle="arc3,rad=-0.3"),
                    bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                              edgecolor=C_RED, alpha=0.92))
        fig.tight_layout()
    return save(fig,"chart_model_sizes.png")


# ── 2. Фазы холодного старта (горизонтальный waterfall) ──────────────────────
def chart_cold_start_breakdown():
    phases  = ["Планирование","Загрузка\nобраза","Распаковка","Инициализация",
               "Загрузка\nвесов","Загрузка\nв память"]
    values  = [2.0, 5.0, 3.0, 1.0, 75.0, 8.0]
    colors_bar = [C_GRAY, C_GRAY, C_GRAY, C_GRAY, C_RED, C_ORG]
    MIN_BAR_WIDTH = 8  # секунд — порог, ниже которого текст выносим наружу

    with plt.rc_context(STYLE):
        fig, ax = plt.subplots(figsize=(7.2, 3.4))
        starts = [sum(values[:i]) for i in range(len(values))]
        bars = ax.barh(range(len(phases)), values, left=starts,
                       color=colors_bar, height=0.55, zorder=3)
        total = sum(values)
        for bar, val, st in zip(bars, values, starts):
            cy = bar.get_y() + bar.get_height() / 2
            if val < MIN_BAR_WIDTH:
                # бар слишком узкий — текст справа от него, чёрным
                ax.text(st + val + 1.0, cy,
                        f"{val:.0f} с", ha="left", va="center",
                        fontsize=8, color="black", fontweight="bold")
            else:
                # текст внутри бара, белым
                ax.text(st + val / 2, cy,
                        f"{val:.0f} с", ha="center", va="center",
                        fontsize=8.5, color="white", fontweight="bold")
        ax.set_yticks(range(len(phases)))
        ax.set_yticklabels(phases, fontsize=9)
        ax.set_xlabel("Время (секунды)", fontsize=9)
        ax.set_title(f"Декомпозиция холодного старта: итого ≈ {total:.0f} с",
                     fontsize=10, pad=6)
        ax.set_xlim(0, total + 14)  # запас для текстов справа от узких баров
        ax.grid(axis="x", alpha=0.3)
        ax.axvline(total, color=C_RED, linewidth=1.2, linestyle="--", alpha=0.7)
        ax.text(total + 0.5, len(phases) - 0.5, f"≈ {total:.0f} с",
                color=C_RED, fontsize=9, va="center")
        ax.annotate("95% времени", xy=(5 + 75/2, 4), xytext=(50, 2.5),
                    fontsize=8.5, color=C_RED, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=C_RED, lw=1.1))
        fig.tight_layout()
    return save(fig,"chart_cold_start_breakdown.png")


# ── 3. T_model_ready по сценариям ─────────────────────────────────────────────
def chart_tmodel_ready():
    scenarios = ["Cold cluster\n(первый старт)",
                 "Warm — same node\n(local cache hit)",
                 "Warm — peer node\n(P2P cache hit)"]
    emptydir  = [74.8, 74.8, 74.8]
    nfs       = [74.2, 11.7, 11.7]
    p2p       = [74.5,  1.9, 13.1]

    x = np.arange(len(scenarios)); w = 0.26
    with plt.rc_context(STYLE):
        fig, ax = plt.subplots(figsize=(7.4, 3.8))
        b1 = ax.bar(x-w, emptydir, w, label="emptyDir (baseline)", color=C_RED,   zorder=3)
        b2 = ax.bar(x,   nfs,      w, label="NFS",                  color=C_ORG,   zorder=3)
        b3 = ax.bar(x+w, p2p,      w, label="P2P + FUSE (предложено)", color=C_GRN, zorder=3)

        for bar, val in zip(b3, p2p):
            if val < 25:
                ax.annotate(f"{val} с",
                            xy=(bar.get_x()+bar.get_width()/2, val),
                            xytext=(0,4), textcoords="offset points",
                            ha="center", va="bottom", fontsize=9,
                            fontweight="bold", color=C_GRN)
        ax.axhline(75, color=C_RED, linewidth=0.9, linestyle="--", alpha=0.45)
        ax.text(0.02, 76.8, "75 с — без кэша", fontsize=8, color=C_RED, alpha=0.75)

        ax.set_ylabel("Время готовности модели, с", fontsize=10)
        ax.set_xticks(x); ax.set_xticklabels(scenarios, fontsize=9)
        ax.set_ylim(0, 90)
        ax.set_yticks([0,15,30,45,60,75])
        # Легенда под графиком, чтобы не перекрывать 75с-столбцы
        ax.legend(fontsize=8.5, loc="upper center",
                  bbox_to_anchor=(0.5, -0.22), ncol=3, frameon=True)
        ax.set_title("Время готовности модели по сценариям (Llama 3 8B, 15 ГБ)", fontsize=11, pad=8)
        fig.subplots_adjust(bottom=0.24)
        fig.tight_layout(rect=[0, 0.18, 1, 1])
    return save(fig,"chart_tmodel_ready.png")


# ── 4. Внешний трафик при масштабировании ─────────────────────────────────────
def chart_external_traffic():
    n = np.arange(1,11); gb = 15.0
    with plt.rc_context(STYLE):
        fig, ax = plt.subplots(figsize=(5.0, 3.5))
        ax.plot(n, n*gb,             "o-", color=C_RED, lw=2, ms=5, label="emptyDir")
        ax.plot(n, np.full_like(n,gb,dtype=float), "s--", color=C_ORG, lw=2, ms=5, label="NFS")
        ax.plot(n, np.full_like(n,gb,dtype=float), "^-",  color=C_GRN, lw=2, ms=5, label="P2P + FUSE")
        ax.fill_between(n, np.full_like(n,gb,dtype=float), n*gb,
                        alpha=0.12, color=C_GRN, label="Экономия")
        ax.annotate("× 10 экономии\nпри N = 10",
                    xy=(10, 15), xytext=(5.5, 142),
                    fontsize=8.5, color=C_GRN, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=C_GRN, lw=1.2),
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                              edgecolor=C_GRN, alpha=0.9))
        ax.set_xlabel("Число реплик (N)", fontsize=10)
        ax.set_ylabel("Внешний трафик, ГБ", fontsize=10)
        ax.set_xticks(n); ax.set_ylim(0,165)
        ax.legend(fontsize=9)
        ax.set_title("Внешний трафик при масштабировании\n(Llama 3 8B = 15 ГБ)", fontsize=10, pad=6)
        fig.tight_layout()
    return save(fig,"chart_external_traffic.png")


# ── 5. Доступность при репликации — простой в год (log-шкала) ────────────────
def chart_availability():
    r_vals = np.array([1, 2, 3, 4, 5])
    a = 0.99
    avail = (1 - (1 - a) ** r_vals)          # доступность 0..1
    downtime_min = (1 - avail) * 365.25 * 24 * 60  # простой в минутах в год
    # r=4,5 → <1 сек → показываем как 0.01 мин для отображения на log-шкале
    downtime_plot = np.maximum(downtime_min, 0.001)
    bar_colors = [C_ORG, "#6CAF3E", C_GRN, "#0B5E35", "#073D22"]
    nines_full  = ["2 девятки","3 девятки","4 девятки","5 девяток","6 девяток"]
    avail_pct   = ["99.0%","99.99%","99.9999%","≈100%","≈100%"]

    with plt.rc_context(STYLE):
        fig, ax = plt.subplots(figsize=(5.2, 3.5))
        bars = ax.bar(r_vals, downtime_plot, color=bar_colors, width=0.5, zorder=3)
        ax.set_yscale("log")

        # Лейблы над барами: доступность + простой
        downtime_labels = ["87.6 ч/год","52.6 мин/год","31.5 с/год","<1 с/год","<0.1 с/год"]
        for bar, pct, dt_lbl in zip(bars, avail_pct, downtime_labels):
            top = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, top * 2.5,
                    f"{pct}\n{dt_lbl}", ha="center", va="bottom",
                    fontsize=7.5, fontweight="bold")

        ax.set_xticks(r_vals)
        ax.set_xticklabels(
            [f"r = {r}\n({n})" for r, n in zip(r_vals, nines_full)], fontsize=8)
        ax.set_ylabel("Простой в год (мин, log-шкала)", fontsize=9)
        ax.set_ylim(0.0005, 1e6)
        ax.set_yticks([0.001, 0.1, 1, 60, 3600, 60*24*365.25])
        ax.set_yticklabels(["<1 с","6 с","1 мин","1 ч","2.5 дня","1 год"], fontsize=8)
        ax.set_title("Простой в год: A = 1 − (1 − a)ʳ,  a = 0.99", fontsize=10, pad=6)
        ax.grid(axis="y", which="both", alpha=0.25)
        fig.tight_layout()
    return save(fig,"chart_availability.png")


# ── 6. Деградация при сценариях отказов ──────────────────────────────────────
def chart_reliability():
    scenarios = ["Отказ\nworker-ноды","Недоступность\nRedis","Недоступность\nHF Hub"]
    nfs_impact = [100, 0, 100]   # % затронутых запросов
    p2p_impact = [2,  15,   0]   # % (прогретый кластер, r=3)

    x = np.arange(len(scenarios)); w = 0.32
    with plt.rc_context(STYLE):
        fig, ax = plt.subplots(figsize=(5.2, 3.8))
        ax.bar(x-w/2, nfs_impact, w, label="NFS",               color=C_ORG, zorder=3)
        ax.bar(x+w/2, p2p_impact, w, label="P2P + FUSE (r = 3)", color=C_GRN, zorder=3)
        for xi,(nv,pv) in zip(x, zip(nfs_impact, p2p_impact)):
            ax.text(xi-w/2, nv+1.5, f"{nv}%", ha="center", fontsize=9,
                    color=C_ORG, fontweight="bold")
            lbl = "< 2%" if pv==2 else (f"{pv}%" if pv else "0%  ✓")
            ax.text(xi+w/2, pv+1.5, lbl, ha="center", fontsize=9,
                    color=C_GRN, fontweight="bold")
        ax.set_ylabel("Деградация инференса (%)", fontsize=10)
        ax.set_xticks(x); ax.set_xticklabels(scenarios, fontsize=9)
        ax.set_ylim(0, 115)
        # Легенда строго под осью, не перекрывает столбцы
        ax.legend(fontsize=9, loc="upper center",
                  bbox_to_anchor=(0.5, -0.30), ncol=2, frameon=True)
        ax.set_title("Деградация при сценариях отказов\n(прогретый кластер, r = 3)",
                     fontsize=10, pad=6)
        fig.subplots_adjust(bottom=0.30)
        fig.tight_layout(rect=[0, 0.25, 1, 1])
    return save(fig,"chart_reliability.png")


# ═══════════════════════════════════════════════════════════════════════════════
# ГЕНЕРАЦИЯ ВСЕХ ГРАФИКОВ
# ═══════════════════════════════════════════════════════════════════════════════
print("Generating charts...")
data_model_sizes   = chart_model_sizes()
data_cold_start    = chart_cold_start_breakdown()
data_tmodel_ready  = chart_tmodel_ready()
data_ext_traffic   = chart_external_traffic()
data_availability  = chart_availability()
data_reliability   = chart_reliability()
print(f"  Saved 6 PNG files to {CHARTS}/")


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 1 — ТИТУЛЬНЫЙ
# ═══════════════════════════════════════════════════════════════════════════════
s1 = new_slide()
rect(s1, Inches(0.22), Inches(0.15), Inches(0.74), Inches(0.72), fill=LGRAY)
txbox(s1, Inches(0.22), Inches(0.35), Inches(0.74), Inches(0.3),
      [_para([run("МАИ",sz=900,bold=True,color=DGRAY)],align="c")])
txbox(s1, Inches(1.05), Inches(0.18), Inches(8.0), Inches(0.45),
      [P("МОСКОВСКИЙ АВИАЦИОННЫЙ ИНСТИТУТ (НИУ)  ·  Институт №8  ·  Кафедра 806",
         sz=1000, color=DGRAY)])
txbox(s1, Inches(0.75), Inches(0.95), Inches(8.5), Inches(2.5),
      [P("Выпускная квалификационная работа магистра на тему:",sz=1500,color=DGRAY,align="c"),
       E(700),
       P("Оптимизация холодного старта и масштабирования\n"
         "моделей машинного обучения в бессерверном инференсе\n"
         "для обеспечения надёжности и высокой доступности",
         sz=2200,bold=True,align="c")])
txbox(s1, Inches(0.75), Inches(3.75), Inches(8.5), Inches(1.1),
      [P("Студент группы М8О-209СВ-24:  Блинов Максим Алексеевич", sz=1600),
       P("Научный руководитель:  Булакина Мария Борисовна, к.т.н., доцент, доцент каф. 806", sz=1600),
       E(300),
       P("Направление:  02.04.02 Фундаментальная информатика и информационные технологии",
         sz=1300, color=DGRAY)])
txbox(s1, Inches(2.72), Inches(5.1), Inches(4.56), Inches(0.35),
      [P("Москва 2025", sz=1200, align="c")])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 2 — АКТУАЛЬНОСТЬ  [текст слева + график справа]
# ═══════════════════════════════════════════════════════════════════════════════
s2 = new_slide()
title_box(s2, "Актуальность темы")

txbox(s2, Inches(0.35), Inches(1.05), Inches(4.55), Inches(4.35), [
    P("Размеры языковых моделей растут:", sz=1750, bold=True),
    E(250),
    P("  GPT-2 (2019):       ~3 МБ весов", sz=1550),
    P("  GPT-3 (2020):       ~350 ГБ весов", sz=1550),
    P("  LLaMA 3 70B (2024): ~140 ГБ весов", sz=1550),
    P("  Falcon 180B (2023): ~360 ГБ весов", sz=1550),
    E(450),
    P("Следствие для serverless-инференса:", sz=1750, bold=True),
    E(250),
    P("  При scale-up Pod заново скачивает модель", sz=1550),
    P("  15 ГБ × 200 МБ/с = 75 с до первого токена", sz=1550),
    P("  10 реплик = 150 ГБ внешнего трафика", sz=1550),
    P("  p99 latency → минуты → нарушение SLA", sz=1550, color=RED),
])

# График рост размеров — справа
img(s2, data_model_sizes, Inches(5.05), Inches(1.05), Inches(4.7), Inches(4.35))


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 3 — ЦЕЛЬ И ЗАДАЧИ
# ═══════════════════════════════════════════════════════════════════════════════
s3 = new_slide()
title_box(s3, "Цель и задачи работы")

body_box(s3, [
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
# СЛАЙД 4 — ИСХОДНАЯ АРХИТЕКТУРА  [схема слева + декомпозиция справа (график)]
# ═══════════════════════════════════════════════════════════════════════════════
s4 = new_slide()
title_box(s4, "Исходная архитектура: storage-initializer + emptyDir")

# Левый блок — описание схемы (текст вместо placeholder)
txbox(s4, Inches(0.35), Inches(1.05), Inches(4.7), Inches(4.35), [
    P("Поток запуска пода:", sz=1700, bold=True),
    E(300),
    P("1.  Scheduler размещает Pod на worker-ноде", sz=1520),
    P("2.  storage-initializer скачивает модель\n"
      "     из HuggingFace в volume emptyDir", sz=1520),
    P("3.  runtime-container монтирует emptyDir\n"
      "     и загружает веса в CPU / GPU", sz=1520),
    E(450),
    P("Ключевые проблемы:", sz=1700, bold=True),
    E(300),
    P("  ✕  Нет переиспользования — каждый Pod скачивает заново", sz=1520),
    P("  ✕  10 реплик = 10 × 15 ГБ = 150 ГБ внешнего трафика", sz=1520),
    Pm(run("  ✕  ",sz=1520),
       run("T",sz=1520,italic=True), sub("first_byte",sz=1520),
       run(" = ",sz=1520),
       run("T",sz=1520,italic=True), sub("model_ready",sz=1520),
       run(" ≈ 75 с",sz=1520)),
    P("  ✕  Привязка к доступности HuggingFace Hub", sz=1520),
])

# График декомпозиции холодного старта — справа
img(s4, data_cold_start, Inches(5.2), Inches(1.05), Inches(4.55), Inches(4.35))


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 5 — ТРЕБОВАНИЯ
# ═══════════════════════════════════════════════════════════════════════════════
s5 = new_slide()
title_box(s5, "Требования к архитектуре")

# Врезка с определениями метрик
rect(s5, Inches(0.32), Inches(1.0), Inches(9.4), Inches(0.82), fill=LBLUE)
txbox(s5, Inches(0.4), Inches(1.02), Inches(9.2), Inches(0.78), [
    Pm(run("Метрики: ",sz=1350,bold=True),
       run("T",sz=1350,italic=True), sub("model_ready",sz=1350),
       run(" — время от планирования пода до готовности ML-runtime принять первый запрос;  ",sz=1350),
       run("T",sz=1350,italic=True), sub("first_byte",sz=1350),
       run(" — время до первого байта данных модели при lazy FUSE loading",sz=1350)),
])

txbox(s5, Inches(0.451), Inches(1.9), Inches(4.55), Inches(3.5), [
    P("Функциональные:", sz=1800, bold=True), E(300),
    P("  •  Переиспользование весов между запусками", sz=1500),
    P("  •  P2P-передача чанков между нодами без HF Hub", sz=1500),
    P("  •  Стандартный POSIX-интерфейс для ML-runtime", sz=1500),
    P("  •  Автоматический fallback на внешний репозиторий", sz=1500),
    P("  •  Совместимость с Kubernetes (DaemonSet, CSI)", sz=1500),
    P("  •  Атомарная запись чанков: tmp-файл → os.Rename", sz=1500),
])
txbox(s5, Inches(5.25), Inches(1.9), Inches(4.45), Inches(3.5), [
    P("Нефункциональные:", sz=1800, bold=True), E(300),
    Pm(run("  •  ",sz=1500), run("T",sz=1500,italic=True),
       sub("model_ready",sz=1500), run(" при local hit ≤ 3 с (15 ГБ)",sz=1500)),
    Pm(run("  •  ",sz=1500), run("T",sz=1500,italic=True),
       sub("first_byte",sz=1500), run(" (lazy FUSE loading) < 1 с",sz=1500)),
    P("  •  Трафик N = 10 реплик = 1× размер модели", sz=1500),
    P("  •  Отказ worker-ноды → graceful degradation", sz=1500),
    P("  •  Overhead FUSE (посл. чтение) ≤ 0.5 % CPU", sz=1500),
    P("  •  Redis lookup latency p99 < 5 мс", sz=1500),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 6 — СТЕК ТЕХНОЛОГИЙ
# ═══════════════════════════════════════════════════════════════════════════════
s6 = new_slide()
title_box(s6, "Стек технологий")

body_box(s6, [
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
    P("   Внешний репозиторий весов; fallback-источник при отсутствии кэша", sz=1500, color=DGRAY),
    E(250),
    P("NFS  ·  Docker / containerd  ·  Prometheus + Grafana", sz=1800, bold=True),
    P("   Промежуточный этап с flock / Lease; контейнеризация; мониторинг hit rate и latency",
      sz=1500, color=DGRAY),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 7 — ПРЕДЛОЖЕННАЯ АРХИТЕКТУРА
# ═══════════════════════════════════════════════════════════════════════════════
s7 = new_slide()
title_box(s7, "Предложенная архитектура")

rect(s7, Inches(0.45), Inches(1.1), Inches(5.0), Inches(4.3), fill=LGRAY)
txbox(s7, Inches(0.45), Inches(2.85), Inches(5.0), Inches(0.5),
      [P("[ схема P2P / FUSE-архитектуры ]", sz=1000, color=GRAY, align="c")])

txbox(s7, Inches(5.65), Inches(1.05), Inches(4.05), Inches(4.3), [
    P("Redis Cluster", sz=1600, bold=True, color=BLUE),
    P("  Control Plane: реестр чанков + heartbeat (TTL 30 с)", sz=1380),
    E(400),
    P("storage-agent", sz=1600, bold=True, color=GREEN),
    P("  DaemonSet · chunk-кэш NVMe", sz=1380),
    P("  UDS ← mounter   TCP ↔ пиры", sz=1380),
    E(400),
    P("storage-mounter", sz=1600, bold=True, color=GREEN),
    P("  FUSE-ФС · lazy loading", sz=1380),
    Pm(run("  ",sz=1380), run("T",sz=1380,italic=True),
       sub("first_byte",sz=1380), run(" < 1 с",sz=1380)),
    E(400),
    P("Алгоритм чтения чанка:", sz=1500, bold=True),
    P("  1. Локальный NVMe    →  2.3 мс  ✓", sz=1380, color=GREEN),
    P("  2. Соседняя нода P2P →  13 мс",     sz=1380, color=ORANGE),
    P("  3. HuggingFace Hub   →  130+ мс",   sz=1380, color=RED),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 8 — ТЕСТОВЫЙ СТЕНД
# ═══════════════════════════════════════════════════════════════════════════════
s8 = new_slide()
title_box(s8, "Нагрузочное тестирование: стенд и сценарии")

txbox(s8, Inches(0.451), Inches(1.05), Inches(4.55), Inches(4.35), [
    P("Тестовый стенд:", sz=1800, bold=True), E(300),
    P("  •  6 worker-нод: Intel Xeon Silver, 16c/32t, 64 ГБ RAM", sz=1500),
    P("  •  Samsung 980 Pro NVMe 2 ТБ — seq. read 7 000 МБ/с", sz=1500),
    P("  •  Сеть: 10 Гбит/с Ethernet, RTT ≤ 0.5 мс", sz=1500),
    P("  •  Redis: 1 master + 2 replica (Sentinel)", sz=1500),
    E(500),
    P("Тестовые модели:", sz=1800, bold=True), E(300),
    P("  •  Llama 3 8B   —  15 ГБ,    960 чанков × 16 МБ", sz=1500),
    P("  •  Mistral 7B   —  14 ГБ,    896 чанков × 16 МБ", sz=1500),
    P("  •  Llama 3 70B  —  140 ГБ,  8 960 чанков × 16 МБ", sz=1500),
])
txbox(s8, Inches(5.25), Inches(1.05), Inches(4.45), Inches(4.35), [
    P("Сценарии:", sz=1800, bold=True), E(300),
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
    Pm(run("Метрики: ",sz=1250,italic=True,color=DGRAY),
       run("T",sz=1250,italic=True,color=DGRAY),
       sub("model_ready",sz=1250,color=DGRAY),
       run(" (p50/p99)  ·  ",sz=1250,italic=True,color=DGRAY),
       run("T",sz=1250,italic=True,color=DGRAY),
       sub("first_byte",sz=1250,color=DGRAY),
       run("  ·  ",sz=1250,color=DGRAY),
       run("V",sz=1250,italic=True,color=DGRAY),
       sub("ext",sz=1250,color=DGRAY),
       run("  ·  Redis p99  ·  CPU FUSE",sz=1250,italic=True,color=DGRAY)),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 9 — РЕЗУЛЬТАТЫ  [таблица + 2 графика]
# ═══════════════════════════════════════════════════════════════════════════════
s9 = new_slide()
title_box(s9, "Результаты тестирования")

tbl(s9, x=Inches(0.3), y=Inches(1.0),
    w=Inches(9.45), h=Inches(2.38),
    col_widths=[int(Inches(3.0)),int(Inches(2.0)),int(Inches(1.75)),int(Inches(2.7))],
    headers=["Показатель","emptyDir (baseline)","NFS","P2P + FUSE"],
    rows=[
        ["T_model_ready,  cold cluster",     "~74.8 с", "~74.2 с", "~74.5 с"],
        ["T_model_ready,  warm (same node)",  "~74.8 с", "~11.7 с", "~1.9 с  ✓"],
        ["T_model_ready,  warm (peer node)",  "~74.8 с", "~11.7 с", "~13.1 с  ✓"],
        ["T_first_byte",                       "~74.8 с", "~74.2 с", "< 1 с  ✓"],
        ["Внешний трафик,  N = 10 реплик",   "150 ГБ",  "15 ГБ",   "15 ГБ  ✓"],
        ["SPOF",                               "нет",     "NFS-сервер","Redis (HA → нет)"],
    ], hdr_sz=12, row_sz=11, hdr_bg=GREEN)

# График T_model_ready — нижний левый
img(s9, data_tmodel_ready,  Inches(0.25), Inches(3.45), Inches(5.8), Inches(2.0))
# График внешний трафик — нижний правый
img(s9, data_ext_traffic,   Inches(6.15), Inches(3.45), Inches(3.6), Inches(2.0))


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 10 — НАДЁЖНОСТЬ  [описание слева + 2 графика справа]
# ═══════════════════════════════════════════════════════════════════════════════
s10 = new_slide()
title_box(s10, "Анализ надёжности")

txbox(s10, Inches(0.3), Inches(1.05), Inches(4.9), Inches(4.35), [
    P("Сценарий 1: Отказ worker-ноды", sz=1600, bold=True),
    P("  TTL в Redis истекает через 30 с → автоочистка.", sz=1380),
    P("  r = 2: P(потери) = 10⁻⁴;   r = 3: P = 10⁻⁶", sz=1380),
    P("  → деградация к HF fallback, не остановка", sz=1380, color=GREEN),
    E(450),
    P("Сценарий 2: Недоступность Redis", sz=1600, bold=True),
    P("  Агент теряет peer discovery.", sz=1380),
    P("  Работает: local cache → HuggingFace (без P2P).", sz=1380),
    P("  → сервис работает при наличии local кэша", sz=1380, color=GREEN),
    E(450),
    P("Сценарий 3: Недоступность HuggingFace Hub", sz=1600, bold=True),
    P("  Прогретый кластер полностью автономен.", sz=1380),
    P("  NFS: отказ сервера = полная остановка.", sz=1380),
    P("  P2P/FUSE → graceful degradation", sz=1380, color=GREEN),
])

# Доступность при репликации — правый верх
img(s10, data_availability, Inches(5.3), Inches(1.05), Inches(4.45), Inches(2.2))
# Деградация при отказах — правый низ
img(s10, data_reliability,  Inches(5.3), Inches(3.35), Inches(4.45), Inches(2.1))


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 11 — ИТОГИ
# ═══════════════════════════════════════════════════════════════════════════════
s11 = new_slide()
title_box(s11, "Итоги работы")

body_box(s11, [
    P("Выполненные задачи:", sz=1800, bold=True), E(200),
    P("  ✓  Проведён анализ причин и масштаба проблемы cold start в serverless ML inference", sz=1600),
    P("  ✓  Исследованы и сравнены 5 решений: Alluxio, JuiceFS, Dragonfly, CubeFS, Rook/Ceph", sz=1600),
    P("  ✓  Разработан NFS-этап с Leader Election через Kubernetes Lease", sz=1600),
    P("  ✓  Спроектирована P2P/FUSE-архитектура с трёхуровневой иерархией кэша", sz=1600),
    P("  ✓  Реализованы storage-agent (DaemonSet) и storage-mounter (FUSE)", sz=1600),
    P("  ✓  Обоснован выбор Redis heartbeat vs Gossip Protocol vs mDNS", sz=1600),
    P("  ✓  Теоретический анализ: AMAT, Закон Литтла, Амдал, Ципф", sz=1600),
    E(400),
    P("Практическая ценность:", sz=1800, bold=True), E(200),
    P("  •  135 ГБ экономии внешнего трафика при 10 репликах Llama 3 8B", sz=1600),
    Pm(run("  •  ",sz=1600),
       run("T",sz=1600,italic=True), sub("model_ready",sz=1600),
       run(": 75 с → 2 с при прогретом кластере  (×36 ускорение)",sz=1600)),
    Pm(run("  •  ",sz=1600),
       run("T",sz=1600,italic=True), sub("first_byte",sz=1600),
       run(" < 1 с благодаря FUSE lazy loading  (было 75 с)",sz=1600)),
    P("  •  Устранение NFS как единственной точки отказа", sz=1600),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СЛАЙД 12 — ДАЛЬНЕЙШЕЕ РАЗВИТИЕ
# ═══════════════════════════════════════════════════════════════════════════════
s12 = new_slide()
title_box(s12, "Направления дальнейшего развития")

body_box(s12, [
    P("  1.  Gossip-based peer discovery — P2P без зависимости от Redis", sz=1700),
    P("  2.  mTLS между storage-agent — аутентификация TCP для production", sz=1700),
    P("  3.  Cache warming — предзагрузка по расписанию, Zipf-прогнозирование", sz=1700),
    P("  4.  CSI-плагин — нативная интеграция с Kubernetes PVC", sz=1700),
    P("  5.  Поддержка Ollama и ModelScope помимо HuggingFace Hub", sz=1700),
    P("  6.  Экспериментальная валидация на реальном GPU-кластере с vLLM", sz=1700),
    E(700),
    P("Система позволяет сократить задержку холодного старта на порядок "
      "при отсутствии деградации надёжности — "
      "что критично для production serverless ML inference.",
      sz=1700, bold=True, italic=True, color=GREEN),
])


# ═══════════════════════════════════════════════════════════════════════════════
# СОХРАНЕНИЕ
# ═══════════════════════════════════════════════════════════════════════════════
prs.save(OUT)
print(f"Saved: {OUT}  ({len(prs.slides)} slides)")

print("\nCharts written to:")
for f in sorted(os.listdir(CHARTS)):
    path = os.path.join(CHARTS, f)
    print(f"  {path}  ({os.path.getsize(path)//1024} КБ)")
