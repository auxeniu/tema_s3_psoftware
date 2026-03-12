import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=IBM+Plex+Mono:wght@400;500&family=DM+Sans:wght@400;500;600&display=swap');

:root {
    --bg:      #0f0f0f;
    --surface: #1a1a1a;
    --border:  #2e2e2e;
    --accent:  #ff5c00;
    --accent2: #ffb347;
    --text:    #e8e8e8;
    --muted:   #888;
    --mono:    'IBM Plex Mono', monospace;
    --display: 'Syne', sans-serif;
    --body:    'DM Sans', sans-serif;
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: var(--body) !important;
}
h1, h2, h3 { font-family: var(--display) !important; color: var(--text) !important; }
[data-testid="stSidebar"] { background-color: #141414 !important; border-right: 1px solid var(--border); }
[data-testid="stSidebar"] * { color: var(--text) !important; }
[data-testid="stMarkdownContainer"] p { color: var(--text) !important; }

.page-header {
    border-left: 4px solid var(--accent);
    padding: 28px 36px;
    background: var(--surface);
    border-radius: 4px;
    margin-bottom: 36px;
}
.page-header .label {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.page-header h1 {
    font-family: var(--display) !important;
    font-size: 44px !important;
    font-weight: 800;
    margin: 0 !important;
    color: var(--text) !important;
    line-height: 1.1;
}
.page-header .sub {
    font-size: 15px;
    color: #999;
    margin-top: 8px;
}

.sec-header {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    margin: 40px 0 16px 0;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
}

.tip {
    background: #161616;
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent2);
    border-radius: 4px;
    padding: 16px 20px;
    font-size: 14px;
    color: #ccc;
    line-height: 1.7;
}
.tip strong { color: var(--accent2); }
.tip code {
    background: #2a2a2a;
    padding: 1px 6px;
    border-radius: 3px;
    font-family: var(--mono);
    font-size: 12px;
    color: #e0e0e0;
}

.concept-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 22px 26px;
    margin-bottom: 8px;
}
.concept-box .cb-title {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.concept-box p {
    color: #ccc !important;
    font-size: 14px;
    line-height: 1.7;
    margin: 0;
}
.concept-box code {
    background: #2a2a2a;
    padding: 1px 6px;
    border-radius: 3px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent2);
}

.summary-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 22px 26px;
}
.summary-box ul {
    margin: 0;
    padding-left: 18px;
    color: #ccc;
    font-size: 14px;
    line-height: 2;
}
.summary-box code {
    background: #2a2a2a;
    padding: 1px 6px;
    border-radius: 3px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent2);
}
</style>
""", unsafe_allow_html=True)

# ── Matplotlib dark theme global ──────────────────────────────────
plt.rcParams.update({
    "figure.facecolor":  "#1a1a1a",
    "axes.facecolor":    "#1a1a1a",
    "axes.edgecolor":    "#2e2e2e",
    "axes.labelcolor":   "#e8e8e8",
    "axes.titlecolor":   "#e8e8e8",
    "xtick.color":       "#888",
    "ytick.color":       "#888",
    "text.color":        "#e8e8e8",
    "grid.color":        "#2e2e2e",
    "grid.linestyle":    "--",
    "grid.alpha":        0.6,
    "figure.dpi":        130,
    "font.family":       "monospace",
})

BRAND_COLORS = {
    "McDonald's":  "#ff5c00",
    "KFC":         "#ffb347",
    "Burger King": "#e8c84a",
    "Subway":      "#3ecf8e",
    "Taco Bell":   "#4ac0e8",
    "Pizza Hut":   "#c084fc",
    "Wendy's":     "#f87171",
}

# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="label">Pagina 03</div>
    <h1>Vizualizări Matplotlib</h1>
    <div class="sub">Grafice statice personalizate integrate în Streamlit cu st.pyplot()</div>
</div>
""", unsafe_allow_html=True)

# ── Verificare date ───────────────────────────────────────────────
if "df" not in st.session_state:
    st.warning("Nu există date încărcate. Mergi la pagina **Home** și încarcă fișierul CSV.")
    st.stop()

df = st.session_state["df"]

# ── Introducere Matplotlib ────────────────────────────────────────
st.markdown('<div class="sec-header">Ce este Matplotlib și cum îl integrăm în Streamlit</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="concept-box">
        <div class="cb-title">Matplotlib vs st.bar_chart</div>
        <p>
            <code>st.bar_chart()</code> este rapid, dar limitat — nu poți controla culorile,
            fonturile, etichetele sau aspectul general.<br><br>
            <strong>Matplotlib</strong> oferă control complet asupra fiecărui element al graficului:
            culori, titluri, axe, legende, adnotări, dimensiuni.
        </p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="concept-box">
        <div class="cb-title">Cum funcționează st.pyplot()</div>
        <p>
            Matplotlib creează graficul în memorie. <code>st.pyplot(fig)</code>
            îl preia și îl afișează ca imagine în aplicație.<br><br>
            Întotdeauna creezi o figură cu <code>fig, ax = plt.subplots()</code>,
            desenezi pe <code>ax</code>, apoi trimiți <code>fig</code> către Streamlit.
        </p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Structura de bază a unui grafic Matplotlib în Streamlit"):
    st.code("""
import matplotlib.pyplot as plt

# 1. Creăm figura și axa
fig, ax = plt.subplots(figsize=(10, 5))

# 2. Desenăm pe axă
ax.bar(categorii, valori, color="#ff5c00")

# 3. Personalizăm
ax.set_title("Titlul graficului", fontsize=14, fontweight="bold")
ax.set_xlabel("Axa X")
ax.set_ylabel("Axa Y")
ax.grid(axis="y", alpha=0.3)

# 4. Trimitem figura către Streamlit
st.pyplot(fig)

# 5. Închidem figura pentru a elibera memoria
plt.close(fig)
""", language="python")

# ── GRAFIC 1 — Bar chart orizontal: calorii medii per brand ───────
st.markdown('<div class="sec-header">Graficul 1 — Bar chart orizontal</div>', unsafe_allow_html=True)

st.markdown("Un bar chart orizontal este mai lizibil când etichetele de pe axa Y sunt nume lungi, cum ar fi numele brandurilor.")

with st.expander("Cod folosit"):
    st.code("""
calorii = (
    df.groupby("Brand")["Calories"]
    .mean()
    .round(0)
    .sort_values()   # ascendent — cel mai mic jos
)

fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.barh(
    calorii.index,
    calorii.values,
    color=[BRAND_COLORS.get(b, "#888") for b in calorii.index],
    height=0.6,
    edgecolor="none"
)

# Adăugăm valoarea la capătul fiecărei bare
for bar, val in zip(bars, calorii.values):
    ax.text(
        val + 5, bar.get_y() + bar.get_height() / 2,
        f"{val:.0f} kcal",
        va="center", fontsize=9, color="#aaa"
    )

ax.set_title("Calorii medii per brand", fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Calorii (kcal)")
ax.grid(axis="x", alpha=0.3)
ax.spines[["top", "right", "left"]].set_visible(False)

st.pyplot(fig)
plt.close(fig)
""", language="python")

calorii = (
    df.groupby("Brand")["Calories"]
    .mean()
    .round(0)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.barh(
    calorii.index,
    calorii.values,
    color=[BRAND_COLORS.get(b, "#888") for b in calorii.index],
    height=0.6,
    edgecolor="none"
)
for bar, val in zip(bars, calorii.values):
    ax.text(
        val + 5, bar.get_y() + bar.get_height() / 2,
        f"{val:.0f} kcal",
        va="center", fontsize=9, color="#aaa"
    )
ax.set_title("Calorii medii per brand", fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Calorii (kcal)")
ax.grid(axis="x", alpha=0.3)
ax.spines[["top", "right", "left"]].set_visible(False)
st.pyplot(fig)
plt.close(fig)

# ── GRAFIC 2 — Pie chart: distribuție categorii ───────────────────
st.markdown('<div class="sec-header">Graficul 2 — Pie chart: distribuția categoriilor</div>', unsafe_allow_html=True)

st.markdown("Un pie chart arată proporțiile dintr-un întreg. Îl folosim pentru a vedea cât din dataset reprezintă fiecare categorie de produs.")

with st.expander("Cod folosit"):
    st.code("""
distributie = df["Category"].value_counts()

fig, ax = plt.subplots(figsize=(7, 7))

wedges, texts, autotexts = ax.pie(
    distributie.values,
    labels=distributie.index,
    autopct="%1.1f%%",        # afișează procentul pe fiecare felie
    startangle=140,           # unghiul de start al primei felii
    pctdistance=0.82,         # distanța procentului față de centru
    wedgeprops=dict(width=0.6, edgecolor="#0f0f0f", linewidth=2)  # donut
)

# Stilizare texte
for text in texts:
    text.set_fontsize(10)
    text.set_color("#e8e8e8")
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color("#e8e8e8")

ax.set_title("Distribuția produselor pe categorii", fontsize=13, fontweight="bold", pad=20)

st.pyplot(fig)
plt.close(fig)
""", language="python")

col1, col2 = st.columns([1, 1])

with col1:
    distributie = df["Category"].value_counts()
    pie_colors = [
        "#ff5c00", "#ffb347", "#3ecf8e", "#4ac0e8",
        "#c084fc", "#f87171", "#e8c84a", "#60a5fa",
        "#34d399", "#fb923c", "#a78bfa", "#f472b6"
    ][:len(distributie)]

    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        distributie.values,
        labels=distributie.index,
        autopct="%1.1f%%",
        startangle=140,
        pctdistance=0.82,
        colors=pie_colors,
        wedgeprops=dict(width=0.6, edgecolor="#0f0f0f", linewidth=2)
    )
    for text in texts:
        text.set_fontsize(9)
        text.set_color("#e8e8e8")
    for autotext in autotexts:
        autotext.set_fontsize(8)
        autotext.set_color("#e8e8e8")
    ax.set_title("Distribuția pe categorii", fontsize=12, fontweight="bold", pad=16)
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.markdown("""
    <div class="tip" style="margin-top: 16px;">
        <strong>Donut chart vs Pie chart</strong><br><br>
        Prin setarea parametrului <code>width</code> în <code>wedgeprops</code>,
        transformăm un pie chart clasic într-un <strong>donut chart</strong> —
        mai modern și mai lizibil când avem multe categorii.<br><br>
        <strong>Când să folosim pie chart?</strong><br>
        Doar când avem <strong>maxim 5-6 categorii</strong> și vrem să arătăm
        proporții dintr-un întreg. Pentru mai multe categorii, un bar chart
        este întotdeauna mai clar.
    </div>
    """, unsafe_allow_html=True)

# ── GRAFIC 3 — Histogram interactiv ───────────────────────────────
st.markdown('<div class="sec-header">Graficul 3 — Histogramă interactivă</div>', unsafe_allow_html=True)

st.markdown("""
O histogramă arată **distribuția** valorilor dintr-o coloană numerică —
câte produse au între 0-100 kcal, câte între 100-200 kcal, și așa mai departe.
Utilizatorul poate alege ce coloană să vizualizeze și câte intervale (bins) să folosească.
""")

with st.expander("Cod folosit"):
    st.code("""
col_hist = st.selectbox("Coloana de vizualizat", coloane_numerice)
bins = st.slider("Număr de intervale (bins)", 5, 40, 15)

fig, ax = plt.subplots(figsize=(9, 4))

ax.hist(df[col_hist].dropna(), bins=bins, color="#ff5c00",
        edgecolor="#0f0f0f", linewidth=0.8, alpha=0.9)

# Linie verticală pentru medie
medie = df[col_hist].mean()
ax.axvline(medie, color="#ffb347", linewidth=1.5,
           linestyle="--", label=f"Medie: {medie:.1f}")

ax.set_title(f"Distribuția valorilor — {col_hist}", fontsize=13, fontweight="bold")
ax.set_xlabel(col_hist)
ax.set_ylabel("Număr produse")
ax.legend()
ax.grid(axis="y", alpha=0.3)

st.pyplot(fig)
plt.close(fig)
""", language="python")

coloane_numerice = ["Calories", "Total Fat (g)", "Carbohydrates (g)",
                    "Protein (g)", "Sodium (mg)", "Sugar (g)", "Fiber (g)", "Price (USD)"]

col1, col2 = st.columns([3, 1])
with col2:
    col_hist = st.selectbox("Coloana de vizualizat", coloane_numerice)
    bins = st.slider("Număr de intervale (bins)", min_value=5, max_value=40, value=15)
    arata_medie = st.toggle("Afișează media", value=True)
    arata_mediana = st.toggle("Afișează mediana", value=False)

with col1:
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.hist(df[col_hist].dropna(), bins=bins, color="#ff5c00",
            edgecolor="#0f0f0f", linewidth=0.8, alpha=0.9)

    legend_handles = []
    if arata_medie:
        medie = df[col_hist].mean()
        ax.axvline(medie, color="#ffb347", linewidth=1.8, linestyle="--")
        legend_handles.append(mpatches.Patch(color="#ffb347", label=f"Medie: {medie:.1f}"))
    if arata_mediana:
        mediana = df[col_hist].median()
        ax.axvline(mediana, color="#3ecf8e", linewidth=1.8, linestyle="--")
        legend_handles.append(mpatches.Patch(color="#3ecf8e", label=f"Mediană: {mediana:.1f}"))
    if legend_handles:
        ax.legend(handles=legend_handles, fontsize=9)

    ax.set_title(f"Distribuția — {col_hist}", fontsize=12, fontweight="bold", pad=12)
    ax.set_xlabel(col_hist)
    ax.set_ylabel("Număr produse")
    ax.grid(axis="y", alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
    st.pyplot(fig)
    plt.close(fig)

# ── GRAFIC 4 — Grouped bar chart: comparație nutrienți per brand ──
st.markdown('<div class="sec-header">Graficul 4 — Grouped bar chart</div>', unsafe_allow_html=True)

st.markdown("""
Un grouped bar chart permite compararea mai multor valori pentru aceleași categorii simultan.
Folosim `numpy` pentru a calcula pozițiile barelor pe axa X.
""")

with st.expander("Cod folosit"):
    st.code("""
import numpy as np

nutrienti = ["Calories", "Total Fat (g)", "Protein (g)"]
branduri = df["Brand"].unique()

# Calculăm media per brand și nutrient
medii = df.groupby("Brand")[nutrienti].mean().round(1)

x = np.arange(len(branduri))   # pozițiile grupurilor
width = 0.25                    # lățimea unei bare
offsets = [-width, 0, width]    # decalajele pentru fiecare nutrient

fig, ax = plt.subplots(figsize=(11, 5))
for i, nutrient in enumerate(nutrienti):
    ax.bar(x + offsets[i], medii[nutrient], width=width-0.02,
           label=nutrient, edgecolor="none")

ax.set_xticks(x)
ax.set_xticklabels(branduri, rotation=20, ha="right")
ax.legend()
ax.set_title("Comparație nutrienți per brand")
st.pyplot(fig)
plt.close(fig)
""", language="python")

nutrienti_grup = ["Calories", "Total Fat (g)", "Protein (g)", "Carbohydrates (g)"]
nutrienti_selectati = st.multiselect(
    "Alege nutrienții de comparat",
    options=nutrienti_grup,
    default=["Calories", "Total Fat (g)", "Protein (g)"]
)

if len(nutrienti_selectati) == 0:
    st.warning("Selectează cel puțin un nutrient.")
else:
    medii = df.groupby("Brand")[nutrienti_selectati].mean().round(1)
    branduri = medii.index.tolist()
    x = np.arange(len(branduri))
    n = len(nutrienti_selectati)
    width = 0.7 / n
    offsets = np.linspace(-(n - 1) * width / 2, (n - 1) * width / 2, n)
    graf_colors = ["#ff5c00", "#ffb347", "#3ecf8e", "#4ac0e8"]

    fig, ax = plt.subplots(figsize=(11, 5))
    for i, nutrient in enumerate(nutrienti_selectati):
        ax.bar(
            x + offsets[i], medii[nutrient],
            width=width - 0.02,
            label=nutrient,
            color=graf_colors[i % len(graf_colors)],
            edgecolor="none",
            alpha=0.9
        )

    ax.set_xticks(x)
    ax.set_xticklabels(branduri, rotation=20, ha="right", fontsize=9)
    ax.legend(fontsize=9, framealpha=0.2)
    ax.set_title("Comparație nutrienți per brand", fontsize=12, fontweight="bold", pad=12)
    ax.set_ylabel("Valoare medie")
    ax.grid(axis="y", alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("""
    <div class="tip">
        <strong>Atentie la scala comună!</strong><br><br>
        Caloriile (sute) și grăsimile (zeci de grame) au scale foarte diferite —
        pe un grafic comun, valorile mici par neglijabile. Pe pagina 4 vom vedea
        cum rezolvăm asta cu Plotly și axe secundare sau date normalizate.
    </div>
    """, unsafe_allow_html=True)

# ── Rezumat ───────────────────────────────────────────────────────
st.markdown('<div class="sec-header">Ce am învățat</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>fig, ax = plt.subplots()</code> — creare figură și axă</li>
            <li><code>ax.barh()</code> — bar chart orizontal</li>
            <li><code>ax.pie()</code> — pie / donut chart</li>
            <li><code>ax.hist()</code> — histogramă</li>
            <li><code>ax.axvline()</code> — linie verticală (medie/mediană)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>ax.set_title() / set_xlabel()</code> — etichete și titlu</li>
            <li><code>ax.spines[].set_visible(False)</code> — ascunde borduri</li>
            <li><code>ax.grid()</code> — grilă de fundal</li>
            <li><code>np.arange() + offset</code> — poziționare grouped bar</li>
            <li><code>st.pyplot(fig)</code> — afișare în Streamlit</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Continuă cu pagina 4: Vizualizări Plotly — grafice interactive cu hover și zoom.")

st.markdown("---")
st.markdown('<p style="text-align:center;color:#444;font-size:12px;font-family:\'IBM Plex Mono\',monospace;">Fast Food Dashboard · Seminar 3 · Python & Streamlit</p>', unsafe_allow_html=True)
