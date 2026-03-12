import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
.page-header .sub { font-size: 15px; color: #999; margin-top: 8px; }

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
.concept-box p { color: #ccc !important; font-size: 14px; line-height: 1.7; margin: 0; }
.concept-box code {
    background: #2a2a2a; padding: 1px 6px; border-radius: 3px;
    font-family: var(--mono); font-size: 12px; color: var(--accent2);
}
.summary-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 22px 26px;
}
.summary-box ul { margin: 0; padding-left: 18px; color: #ccc; font-size: 14px; line-height: 2; }
.summary-box code {
    background: #2a2a2a; padding: 1px 6px; border-radius: 3px;
    font-family: var(--mono); font-size: 12px; color: var(--accent2);
}
</style>
""", unsafe_allow_html=True)

# ── Plotly dark template ──────────────────────────────────────────
PLOTLY_TEMPLATE = "plotly_dark"
BRAND_COLORS = {
    "McDonald's":  "#ff5c00",
    "KFC":         "#ffb347",
    "Burger King": "#e8c84a",
    "Subway":      "#3ecf8e",
    "Taco Bell":   "#4ac0e8",
    "Pizza Hut":   "#c084fc",
    "Wendy's":     "#f87171",
}
COLOR_SEQ = list(BRAND_COLORS.values())

def apply_dark(fig, title=None):
    """Aplică stilul întunecat consistent pe orice figură Plotly."""
    fig.update_layout(
        template=PLOTLY_TEMPLATE,
        paper_bgcolor="#1a1a1a",
        plot_bgcolor="#1a1a1a",
        font_family="IBM Plex Mono",
        font_color="#e8e8e8",
        title_text=title,
        title_font_size=14,
        title_font_color="#e8e8e8",
        margin=dict(l=40, r=40, t=50, b=40),
        legend=dict(bgcolor="#1a1a1a", bordercolor="#2e2e2e", borderwidth=1),
    )
    fig.update_xaxes(gridcolor="#2e2e2e", zerolinecolor="#2e2e2e")
    fig.update_yaxes(gridcolor="#2e2e2e", zerolinecolor="#2e2e2e")
    return fig

# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="label">Pagina 04</div>
    <h1>Vizualizări Plotly</h1>
    <div class="sub">Grafice interactive cu hover, zoom și animații — integrate cu st.plotly_chart()</div>
</div>
""", unsafe_allow_html=True)

if "df" not in st.session_state:
    st.warning("Nu există date încărcate. Mergi la pagina **Home** și încarcă fișierul CSV.")
    st.stop()

df = st.session_state["df"]

# ── Matplotlib vs Plotly ──────────────────────────────────────────
st.markdown('<div class="sec-header">Matplotlib vs Plotly — când folosim ce</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="concept-box">
        <div class="cb-title">Matplotlib</div>
        <p>
            Grafice <strong>statice</strong>, exportate ca imagine.<br><br>
            Control total asupra fiecărui pixel — ideal pentru rapoarte,
            publicații sau când ai nevoie de un aspect foarte specific.<br><br>
            Sintaxă mai verbosă, dar extrem de flexibilă.
        </p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="concept-box">
        <div class="cb-title">Plotly</div>
        <p>
            Grafice <strong>interactive</strong> — hover, zoom, pan, click.<br><br>
            Utilizatorul poate explora datele direct în grafic.
            Ideal pentru dashboarduri și aplicații web.<br><br>
            Sintaxă mai scurtă prin <code>plotly.express</code>,
            control avansat prin <code>plotly.graph_objects</code>.
        </p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Structura de bază a unui grafic Plotly în Streamlit"):
    st.code("""
import plotly.express as px

# plotly.express — sintaxă scurtă, ideal pentru grafice rapide
fig = px.bar(df, x="Brand", y="Calories", color="Brand", title="Calorii per brand")

# Personalizare layout
fig.update_layout(template="plotly_dark", paper_bgcolor="#1a1a1a")

# Afișare în Streamlit — use_container_width extinde graficul pe toată lățimea
st.plotly_chart(fig, use_container_width=True)
""", language="python")

# ── GRAFIC 1 — Bar chart interactiv cu px.bar ─────────────────────
st.markdown('<div class="sec-header">Graficul 1 — Bar chart interactiv: px.bar()</div>', unsafe_allow_html=True)

st.markdown("Cel mai simplu grafic Plotly. Hover pe bare pentru a vedea valorile exacte, click pe legendă pentru a ascunde/afișa branduri.")

with st.expander("Cod folosit"):
    st.code("""
calorii = (
    df.groupby("Brand")["Calories"]
    .mean().round(1).reset_index()
    .sort_values("Calories", ascending=False)
)

fig = px.bar(
    calorii,
    x="Brand", y="Calories",
    color="Brand",
    color_discrete_map=BRAND_COLORS,   # culori personalizate per brand
    text="Calories",                    # afișează valoarea pe bară
    title="Calorii medii per brand"
)

fig.update_traces(texttemplate="%{text:.0f} kcal", textposition="outside")
fig.update_layout(showlegend=False, template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)
""", language="python")

calorii_bar = (
    df.groupby("Brand")["Calories"]
    .mean().round(1).reset_index()
    .sort_values("Calories", ascending=False)
)

fig1 = px.bar(
    calorii_bar,
    x="Brand", y="Calories",
    color="Brand",
    color_discrete_map=BRAND_COLORS,
    text="Calories",
)
fig1.update_traces(texttemplate="%{text:.0f} kcal", textposition="outside")
fig1.update_layout(showlegend=False, uniformtext_minsize=9)
fig1 = apply_dark(fig1, "Calorii medii per brand")
st.plotly_chart(fig1, use_container_width=True)

# ── GRAFIC 2 — Scatter plot: calorii vs grăsimi ───────────────────
st.markdown('<div class="sec-header">Graficul 2 — Scatter plot: corelații între nutrienți</div>', unsafe_allow_html=True)

st.markdown("""
Un scatter plot arată relația dintre două variabile numerice.
Fiecare punct este un produs — hover pe el pentru a vedea toate detaliile.
""")

with st.expander("Cod folosit"):
    st.code("""
fig = px.scatter(
    df,
    x="Calories", y="Total Fat (g)",
    color="Brand",
    size="Protein (g)",        # mărimea punctului = proteina
    hover_name="Item",         # titlul tooltip-ului la hover
    hover_data=["Category", "Sodium (mg)", "Price (USD)"],
    color_discrete_map=BRAND_COLORS,
)

st.plotly_chart(fig, use_container_width=True)
""", language="python")

col1, col2 = st.columns([3, 1])

with col2:
    axa_x = st.selectbox("Axa X", ["Calories", "Total Fat (g)", "Carbohydrates (g)", "Sodium (mg)"], index=0)
    axa_y = st.selectbox("Axa Y", ["Total Fat (g)", "Calories", "Protein (g)", "Sugar (g)"], index=0)
    marime = st.selectbox("Mărimea punctului", ["Protein (g)", "Calories", "Sodium (mg)"], index=0)

with col1:
    fig2 = px.scatter(
        df,
        x=axa_x, y=axa_y,
        color="Brand",
        size=marime,
        size_max=22,
        hover_name="Item",
        hover_data=["Category", "Brand", "Price (USD)"],
        color_discrete_map=BRAND_COLORS,
    )
    fig2 = apply_dark(fig2, f"{axa_x} vs {axa_y}")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="tip">
    <strong>De ce scatter plot?</strong><br><br>
    Observi imediat că produsele cu mai multe calorii tind să aibă mai multe grăsimi —
    o corelație pozitivă clară. Punctele izolate departe de grupul principal sunt
    <strong>outlieri</strong> — produse neobișnuite care merită investigate.
    Hover pe ele pentru a le identifica!
</div>
""", unsafe_allow_html=True)

# ── GRAFIC 3 — Box plot: distribuție calorii per brand ────────────
st.markdown('<div class="sec-header">Graficul 3 — Box plot: distribuția valorilor</div>', unsafe_allow_html=True)

st.markdown("""
Un box plot arată simultan **mediana, cuartilele și outlierii** unei distribuții.
Este mult mai informativ decât o simplă medie — arată și cât de variate sunt produsele unui brand.
""")

with st.expander("Cod folosit"):
    st.code("""
fig = px.box(
    df,
    x="Brand", y="Calories",
    color="Brand",
    color_discrete_map=BRAND_COLORS,
    points="all",       # afișează și punctele individuale
    hover_name="Item",
    notched=True,       # 'crestătură' care indică intervalul de încredere al medianei
)

st.plotly_chart(fig, use_container_width=True)
""", language="python")

col_box = st.selectbox(
    "Coloana de analizat",
    ["Calories", "Total Fat (g)", "Protein (g)", "Sodium (mg)", "Sugar (g)", "Price (USD)"],
    key="box_col"
)

fig3 = px.box(
    df,
    x="Brand", y=col_box,
    color="Brand",
    color_discrete_map=BRAND_COLORS,
    points="all",
    hover_name="Item",
    notched=True,
)
fig3 = apply_dark(fig3, f"Distribuția — {col_box} per brand")
fig3.update_layout(showlegend=False)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<div class="tip">
    <strong>Cum citim un box plot?</strong><br><br>
    Linia din mijlocul cutiei = <strong>mediana</strong> (50% din valori sunt sub ea).<br>
    Marginile cutiei = <strong>cuartila 25%</strong> și <strong>75%</strong>.<br>
    Liniile exterioare (mustățile) = valorile minime și maxime fără outlieri.<br>
    Punctele izolate = <strong>outlieri</strong> — valori neobișnuit de mari sau mici.
</div>
""", unsafe_allow_html=True)

# ── GRAFIC 4 — Heatmap: corelații între nutrienți ─────────────────
st.markdown('<div class="sec-header">Graficul 4 — Heatmap: matricea corelațiilor</div>', unsafe_allow_html=True)

st.markdown("""
O matrice de corelații arată cât de puternic sunt legate două coloane numerice.
Valoarea **1.0** înseamnă corelație perfectă pozitivă, **-1.0** perfectă negativă, **0** fără relație.
""")

with st.expander("Cod folosit"):
    st.code("""
# Calculăm matricea de corelații cu Pandas
corr = df[coloane_numerice].corr().round(2)

fig = go.Figure(data=go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.index,
    colorscale="RdBu",   # roșu = corelație negativă, albastru = pozitivă
    zmid=0,              # centrat pe 0
    text=corr.values,
    texttemplate="%{text}",
    hoverongaps=False,
))

st.plotly_chart(fig, use_container_width=True)
""", language="python")

coloane_corr = ["Calories", "Total Fat (g)", "Carbohydrates (g)",
                "Protein (g)", "Sodium (mg)", "Sugar (g)", "Fiber (g)", "Price (USD)"]

corr = df[coloane_corr].corr().round(2)

fig4 = go.Figure(data=go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.index,
    colorscale="RdBu",
    zmid=0,
    text=corr.values,
    texttemplate="%{text}",
    textfont={"size": 11},
    hoverongaps=False,
))
fig4 = apply_dark(fig4, "Matricea corelațiilor dintre nutrienți")
fig4.update_layout(height=480)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
<div class="tip">
    <strong>Ce observăm?</strong><br><br>
    Caloriile corelează puternic cu grăsimile și carbohidrații — are sens, ambele contribuie la calorii.
    Fibrele au o corelație slabă sau negativă cu zahărul — produsele bogate în fibre
    tind să fie mai puțin dulci. Aceste tipare sunt exact ce ar trebui să caute
    un analist de date când explorează un dataset nou.
</div>
""", unsafe_allow_html=True)

# ── GRAFIC 5 — Sunburst: ierarhie brand → categorie ───────────────
st.markdown('<div class="sec-header">Graficul 5 — Sunburst: structura ierarhică a datelor</div>', unsafe_allow_html=True)

st.markdown("""
Un sunburst chart vizualizează date **ierarhice** — inelul interior reprezintă primul nivel
(brandul), inelul exterior al doilea nivel (categoria). Click pe un brand pentru a-l izola.
""")

with st.expander("Cod folosit"):
    st.code("""
fig = px.sunburst(
    df,
    path=["Brand", "Category"],   # ierarhia: brand → categorie
    values="Calories",            # mărimea feliei = suma caloriilor
    color="Brand",
    color_discrete_map=BRAND_COLORS,
)

st.plotly_chart(fig, use_container_width=True)
""", language="python")

col1, col2 = st.columns([1, 1])

with col1:
    metric_sun = st.selectbox(
        "Valoarea reprezentată",
        ["Calories", "Total Fat (g)", "Protein (g)", "Sodium (mg)"],
        key="sun_metric"
    )
    fig5 = px.sunburst(
        df,
        path=["Brand", "Category"],
        values=metric_sun,
        color="Brand",
        color_discrete_map=BRAND_COLORS,
    )
    fig5 = apply_dark(fig5, f"Structura datelor — {metric_sun}")
    fig5.update_layout(height=460)
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    st.markdown("""
    <div class="tip" style="margin-top: 16px;">
        <strong>Cum interacționezi cu el?</strong><br><br>
        <strong>Click</strong> pe un brand din inelul interior — graficul face zoom
        și arată doar categoriile acelui brand.<br><br>
        <strong>Click în centru</strong> — revii la vizualizarea completă.<br><br>
        <strong>Hover</strong> — afișează valoarea exactă și ierarhia completă
        a fiecărei felii.<br><br>
        Sunburst este ideal când vrei să arăți simultan <strong>proporțiile</strong>
        și <strong>structura ierarhică</strong> a datelor.
    </div>
    """, unsafe_allow_html=True)

# ── Rezumat ───────────────────────────────────────────────────────
st.markdown('<div class="sec-header">Ce am învățat</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>px.bar()</code> — bar chart rapid cu plotly.express</li>
            <li><code>px.scatter()</code> — scatter plot cu hover detaliat</li>
            <li><code>px.box()</code> — box plot cu outlieri vizibili</li>
            <li><code>go.Heatmap()</code> — heatmap cu graph_objects</li>
            <li><code>px.sunburst()</code> — date ierarhice interactive</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>color_discrete_map</code> — culori personalizate per categorie</li>
            <li><code>hover_name / hover_data</code> — conținutul tooltip-ului</li>
            <li><code>fig.update_layout()</code> — personalizare generală</li>
            <li><code>fig.update_traces()</code> — personalizare serii de date</li>
            <li><code>st.plotly_chart(fig, use_container_width=True)</code></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Continuă cu pagina 5: Quiz — testează-ți cunoștințele din seminar.")

st.markdown("---")
st.markdown('<p style="text-align:center;color:#444;font-size:12px;font-family:\'IBM Plex Mono\',monospace;">Fast Food Dashboard · Seminar 3 · Python & Streamlit</p>', unsafe_allow_html=True)
