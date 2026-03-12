import streamlit as st
import pandas as pd

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
    --success: #3ecf8e;
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

.result-stat {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 3px solid var(--accent);
    border-radius: 4px;
    padding: 16px 20px;
    text-align: center;
}
.result-stat .rv {
    font-family: var(--display);
    font-size: 32px;
    font-weight: 800;
    color: var(--accent);
    line-height: 1;
}
.result-stat .rl {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
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

.no-results {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 40px;
    text-align: center;
    color: var(--muted);
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="label">Pagina 02</div>
    <h1>Filtrare & Explorare</h1>
    <div class="sub">Filtrarea datelor cu Pandas și vizualizări rapide cu Streamlit</div>
</div>
""", unsafe_allow_html=True)

# ── Verificare date ───────────────────────────────────────────────
if "df" not in st.session_state:
    st.warning("Nu există date încărcate. Mergi la pagina **Home** și încarcă fișierul CSV.")
    st.stop()

df = st.session_state["df"]

# ── Pasul 1 — Filtrare cu sidebar ───────────────────────────────
st.markdown('<div class="sec-header">Pasul 1 — Filtrare cu sidebar</div>', unsafe_allow_html=True)

st.markdown("""
Sidebar-ul este ideal pentru filtre — rămâne vizibil indiferent de pagină și nu aglomerează conținutul principal.
Widget-urile de mai jos filtrează DataFrame-ul în timp real.
""")

with st.expander("Cod folosit"):
    st.code("""
# Filtre în sidebar
branduri_disponibile = df["Brand"].unique().tolist()
branduri_selectate = st.sidebar.multiselect(
    "Brand", branduri_disponibile, default=branduri_disponibile
)

cal_min, cal_max = int(df["Calories"].min()), int(df["Calories"].max())
interval_calorii = st.sidebar.slider(
    "Interval calorii", cal_min, cal_max, (cal_min, cal_max)
)

# Aplicăm filtrele pe DataFrame
df_filtrat = df[
    (df["Brand"].isin(branduri_selectate)) &
    (df["Calories"] >= interval_calorii[0]) &
    (df["Calories"] <= interval_calorii[1])
]
""", language="python")

# ── Filtre în sidebar ─────────────────────────────────────────────
st.sidebar.markdown("---")
st.sidebar.markdown("### Filtre")

# Filter 1 — Brand
branduri_disponibile = sorted(df["Brand"].unique().tolist())
branduri_selectate = st.sidebar.multiselect(
    "Brand",
    options=branduri_disponibile,
    default=branduri_disponibile
)

# Filter 2 — Categorie
categorii_disponibile = sorted(df["Category"].unique().tolist())
categorii_selectate = st.sidebar.multiselect(
    "Categorie",
    options=categorii_disponibile,
    default=categorii_disponibile
)

# Filter 3 — Interval calorii
cal_min = int(df["Calories"].min())
cal_max = int(df["Calories"].max())
interval_calorii = st.sidebar.slider(
    "Interval calorii (kcal)",
    min_value=cal_min,
    max_value=cal_max,
    value=(cal_min, cal_max)
)

# Filter 4 — Sortare
coloana_sortare = st.sidebar.selectbox(
    "Sortează după",
    options=["Calories", "Total Fat (g)", "Protein (g)", "Sodium (mg)", "Sugar (g)", "Price (USD)"],
)
ordine_desc = st.sidebar.toggle("Descrescător", value=True)

# ── Aplicăm filtrele ──────────────────────────────────────────────
df_filtrat = df[
    (df["Brand"].isin(branduri_selectate)) &
    (df["Category"].isin(categorii_selectate)) &
    (df["Calories"] >= interval_calorii[0]) &
    (df["Calories"] <= interval_calorii[1])
].sort_values(coloana_sortare, ascending=not ordine_desc).reset_index(drop=True)

# ── Statistici rezultat ───────────────────────────────────────────
st.markdown('<div class="sec-header">Rezultatele filtrării</div>', unsafe_allow_html=True)

if len(df_filtrat) == 0:
    st.markdown('<div class="no-results">Niciun produs nu corespunde filtrelor selectate. Ajustează filtrele din sidebar.</div>', unsafe_allow_html=True)
    st.stop()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="result-stat"><div class="rv">{len(df_filtrat)}</div><div class="rl">Produse găsite</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="result-stat"><div class="rv">{df_filtrat["Calories"].mean():.0f}</div><div class="rl">Kcal medii</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="result-stat"><div class="rv">{df_filtrat["Total Fat (g)"].mean():.1f}g</div><div class="rl">Grăsimi medii</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="result-stat"><div class="rv">{df_filtrat["Protein (g)"].mean():.1f}g</div><div class="rl">Proteină medie</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.dataframe(df_filtrat, use_container_width=True, hide_index=True)

# ── Pasul 2 — st.bar_chart ──────────────────────────────────────
st.markdown('<div class="sec-header">Pasul 2 — Grafic cu bare: st.bar_chart()</div>', unsafe_allow_html=True)

st.markdown("""
`st.bar_chart()` este cel mai rapid mod de a vizualiza date categoriale în Streamlit.
Primește un DataFrame cu indexul pe axa X și valorile pe axa Y.
""")

with st.expander("Cod folosit"):
    st.code("""
# Calculăm media caloriilor per brand
calorii_per_brand = (
    df_filtrat.groupby("Brand")["Calories"]
    .mean()
    .round(0)
    .sort_values(ascending=False)
)

st.bar_chart(calorii_per_brand)
""", language="python")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("**Calorii medii per brand**")
    calorii_per_brand = (
        df_filtrat.groupby("Brand")["Calories"]
        .mean()
        .round(0)
        .sort_values(ascending=False)
    )
    st.bar_chart(calorii_per_brand, color="#ff5c00")

with col2:
    st.markdown("""
    <div class="tip">
        <strong>Cum funcționează?</strong><br><br>
        <code>groupby("Brand")</code> — grupează rândurile după brand<br><br>
        <code>["Calories"].mean()</code> — calculează media caloriilor per grup<br><br>
        <code>.sort_values()</code> — sortează rezultatul<br><br>
        Rezultatul este o <strong>Serie Pandas</strong> cu brandul ca index — exact formatul pe care îl așteaptă <code>st.bar_chart()</code>.
    </div>
    """, unsafe_allow_html=True)

# ── Pasul 3 — st.bar_chart grupat pe categorie ──────────────────
st.markdown('<div class="sec-header">Pasul 3 — Comparație pe categorii</div>', unsafe_allow_html=True)

st.markdown("Putem alege dinamic ce nutrient să vizualizăm, lăsând utilizatorul să decidă.")

with st.expander("Cod folosit"):
    st.code("""
nutrient = st.selectbox(
    "Alege nutrientul",
    ["Calories", "Total Fat (g)", "Protein (g)", "Sodium (mg)", "Sugar (g)"]
)

per_categorie = (
    df_filtrat.groupby("Category")[nutrient]
    .mean()
    .round(1)
    .sort_values(ascending=False)
)

st.bar_chart(per_categorie)
""", language="python")

nutrient = st.selectbox(
    "Alege nutrientul de vizualizat",
    ["Calories", "Total Fat (g)", "Protein (g)", "Sodium (mg)", "Sugar (g)", "Fiber (g)"]
)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"**{nutrient} — medie per categorie**")
    per_categorie = (
        df_filtrat.groupby("Category")[nutrient]
        .mean()
        .round(1)
        .sort_values(ascending=False)
    )
    st.bar_chart(per_categorie, color="#ffb347")

with col2:
    top3 = per_categorie.head(3)
    st.markdown("**Top 3 categorii:**")
    for i, (cat, val) in enumerate(top3.items()):
        rank_color = ["#ff5c00", "#ffb347", "#888"][i]
        st.markdown(f"""
        <div style="background:#1a1a1a; border:1px solid #2e2e2e; border-left:3px solid {rank_color};
                    border-radius:4px; padding:12px 16px; margin-bottom:10px;">
            <div style="font-family:'IBM Plex Mono',monospace; font-size:10px;
                        color:{rank_color}; letter-spacing:2px; text-transform:uppercase;">
                #{i+1}
            </div>
            <div style="font-family:'Syne',sans-serif; font-size:16px;
                        font-weight:700; color:#e8e8e8; margin:4px 0 2px 0;">
                {cat}
            </div>
            <div style="font-family:'IBM Plex Mono',monospace; font-size:13px; color:#aaa;">
                {val:.1f}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Pasul 4 — st.line_chart ──────────────────────────────────────
st.markdown('<div class="sec-header">Pasul 4 — Grafic liniar: st.line_chart()</div>', unsafe_allow_html=True)

st.markdown("""
`st.line_chart()` funcționează similar cu `st.bar_chart()`, dar este mai potrivit pentru a
arăta **distribuția** sau **evoluția** unor valori. Aici îl folosim pentru a compara
profilul nutrițional mediu al fiecărui brand selectat.
""")

with st.expander("Cod folosit"):
    st.code("""
# Creăm un tabel pivot: branduri pe coloane, nutrienți pe rânduri
nutrienti = ["Calories", "Total Fat (g)", "Protein (g)", "Sodium (mg)"]

pivot = (
    df_filtrat.groupby("Brand")[nutrienti]
    .mean()
    .round(1)
    .T   # transpunem: nutrienții devin indexul (axa X)
)

st.line_chart(pivot)
""", language="python")

nutrienti_line = ["Calories", "Total Fat (g)", "Protein (g)", "Sodium (mg)", "Sugar (g)"]

pivot = (
    df_filtrat.groupby("Brand")[nutrienti_line]
    .mean()
    .round(1)
    .T
)

st.markdown("**Profil nutrițional mediu per brand**")
st.line_chart(pivot)

st.markdown("""
<div class="tip">
    <strong>Atentie la scala datelor!</strong><br><br>
    Sodiul este măsurat în <strong>mg</strong>, iar grăsimile în <strong>grame</strong> —
    valorile lor absolute sunt foarte diferite, ceea ce poate distorsiona graficul.
    Pe pagina 4 (Plotly) vom vedea cum normalizăm datele pentru comparații corecte.
</div>
""", unsafe_allow_html=True)

# ── Pasul 5 — Căutare după nume produs ────────────────────────
st.markdown('<div class="sec-header">Pasul 5 — Căutare după nume</div>', unsafe_allow_html=True)

st.markdown("Folosim `str.contains()` din Pandas pentru a filtra după un text introdus de utilizator.")

with st.expander("Cod folosit"):
    st.code("""
termen = st.text_input("Caută un produs")

if termen:
    rezultate = df[
        df["Item"].str.contains(termen, case=False, na=False)
    ]
    st.dataframe(rezultate)
""", language="python")

termen = st.text_input("Caută un produs (ex: Chicken, Burger, Fries...)")

if termen:
    rezultate = df[df["Item"].str.contains(termen, case=False, na=False)]
    if len(rezultate) == 0:
        st.markdown(f'<div class="no-results">Niciun produs găsit pentru "<strong>{termen}</strong>".</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"**{len(rezultate)} produse găsite pentru \"{termen}\":**")
        st.dataframe(
            rezultate[["Brand", "Item", "Category", "Calories", "Total Fat (g)", "Protein (g)", "Price (USD)"]],
            use_container_width=True,
            hide_index=True
        )
else:
    st.markdown('<div class="no-results" style="padding:20px;">Introdu un termen de căutare mai sus.</div>', unsafe_allow_html=True)

# ── Rezumat ───────────────────────────────────────────────────────
st.markdown('<div class="sec-header">Ce am învățat</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>st.sidebar.multiselect()</code> — filtre multiple în sidebar</li>
            <li><code>st.sidebar.slider()</code> — interval numeric interactiv</li>
            <li><code>st.sidebar.toggle()</code> — comutator on/off</li>
            <li><code>df[conditie1 & conditie2]</code> — filtrare combinată Pandas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>df.groupby().mean()</code> — agregare pe grupuri</li>
            <li><code>st.bar_chart()</code> — grafic cu bare rapid</li>
            <li><code>st.line_chart()</code> — grafic liniar rapid</li>
            <li><code>str.contains()</code> — căutare text în coloană</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Continuă cu pagina 3: Vizualizări Matplotlib")

st.markdown("---")
st.markdown('<p style="text-align:center;color:#444;font-size:12px;font-family:\'IBM Plex Mono\',monospace;">Fast Food Dashboard · Seminar 3 · Python & Streamlit</p>', unsafe_allow_html=True)
