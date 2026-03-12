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

.metric-row {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 8px;
}
.metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 3px solid var(--accent);
    border-radius: 4px;
    padding: 20px 24px;
    min-width: 120px;
    text-align: center;
    flex: 1;
}
.metric-card .mv {
    font-family: var(--display);
    font-size: 36px;
    font-weight: 800;
    color: var(--accent);
    line-height: 1;
}
.metric-card .ml {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
}

.extreme-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 22px 26px;
}
.extreme-card .ec-label {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.extreme-card .ec-name {
    font-family: var(--display);
    font-size: 20px;
    color: var(--text);
    margin-bottom: 4px;
}
.extreme-card .ec-brand {
    font-size: 13px;
    color: var(--muted);
    margin-bottom: 14px;
}
.extreme-card .ec-stats {
    font-family: var(--mono);
    font-size: 13px;
    color: #bbb;
    line-height: 1.8;
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

# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="label">Pagina 01</div>
    <h1>Date & Statistici</h1>
    <div class="sub">Încărcarea și explorarea unui dataset real de fast food</div>
</div>
""", unsafe_allow_html=True)

# ── Verificare date ───────────────────────────────────────────────
if "df" not in st.session_state:
    st.warning("Nu există date încărcate. Mergi la pagina **Home** și încarcă fișierul CSV.")
    st.stop()

df = st.session_state["df"]

# ── Pasul 1 — Previzualizare ──────────────────────────────────────
st.markdown('<div class="sec-header">Pasul 1 — Previzualizare date</div>', unsafe_allow_html=True)

st.markdown("Folosim `st.dataframe()` pentru a afișa un tabel interactiv. Coloanele pot fi sortate direct din interfață.")

with st.expander("Cod folosit"):
    st.code("""
# df vine din st.session_state, salvat în Home.py
df = st.session_state["df"]

numar_randuri = st.slider("Câte rânduri să afișăm?", 5, 50, 10, 5)
st.dataframe(df.head(numar_randuri))
""", language="python")

numar_randuri = st.slider("Câte rânduri să afișăm?", min_value=5, max_value=50, value=10, step=5)
st.dataframe(df.head(numar_randuri), use_container_width=True)

# ── Pasul 2 — st.metric ──────────────────────────────────────────
st.markdown('<div class="sec-header">Pasul 2 — Indicatori cheie cu st.metric()</div>', unsafe_allow_html=True)

st.markdown("`st.metric()` afișează o valoare importantă cu etichetă și, opțional, o variație (delta).")

with st.expander("Cod folosit"):
    st.code("""
col1, col2, col3 = st.columns(3)
col1.metric("Total produse", len(df))
col2.metric("Branduri", df['Brand'].nunique())
col3.metric("Calorii medii", f"{df['Calories'].mean():.0f} kcal")
""", language="python")

st.markdown(f"""
<div class="metric-row">
    <div class="metric-card"><div class="mv">{len(df)}</div><div class="ml">Produse</div></div>
    <div class="metric-card"><div class="mv">{df['Brand'].nunique()}</div><div class="ml">Branduri</div></div>
    <div class="metric-card"><div class="mv">{df['Calories'].mean():.0f}</div><div class="ml">Kcal medii</div></div>
    <div class="metric-card"><div class="mv">{df['Calories'].max():.0f}</div><div class="ml">Kcal max</div></div>
    <div class="metric-card"><div class="mv">{df['Category'].nunique()}</div><div class="ml">Categorii</div></div>
</div>
""", unsafe_allow_html=True)

# ── Pasul 3 — df.describe() ──────────────────────────────────────
st.markdown('<div class="sec-header">Pasul 3 — Statistici automate cu df.describe()</div>', unsafe_allow_html=True)

st.markdown("`.describe()` calculează automat pentru fiecare coloană numerică: număr valori, medie, abatere standard, minim, maxim și cuartile.")

with st.expander("Cod folosit"):
    st.code("st.dataframe(df.describe().round(2))", language="python")

st.dataframe(df.describe().round(2), use_container_width=True)

# ── Pasul 4 — Structura datelor ───────────────────────────────────
st.markdown('<div class="sec-header">Pasul 4 — Structura datelor</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Coloane și tipuri de date**")
    info_df = pd.DataFrame({
        "Coloană": df.columns,
        "Tip": df.dtypes.values.astype(str),
        "Valori lipsă": df.isnull().sum().values
    })
    st.dataframe(info_df, use_container_width=True, hide_index=True)

with col2:
    st.markdown("**Distribuție pe branduri**")
    brand_counts = df["Brand"].value_counts().reset_index()
    brand_counts.columns = ["Brand", "Nr. produse"]
    st.dataframe(brand_counts, use_container_width=True, hide_index=True)

# ── Pasul 5 — Produse extreme ─────────────────────────────────────
st.markdown('<div class="sec-header">Pasul 5 — Produse extreme</div>', unsafe_allow_html=True)

max_row = df.loc[df["Calories"].idxmax()]
min_row = df.loc[df["Calories"].idxmin()]

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="extreme-card" style="border-top: 3px solid #ff4040;">
        <div class="ec-label" style="color:#ff4040;">Cel mai caloric produs</div>
        <div class="ec-name">{max_row['Item']}</div>
        <div class="ec-brand">{max_row['Brand']} &nbsp;·&nbsp; {max_row['Category']}</div>
        <div class="ec-stats">
            {max_row['Calories']} kcal<br>
            {max_row['Total Fat (g)']} g grăsimi<br>
            {max_row['Protein (g)']} g proteină<br>
            {max_row['Sodium (mg)']} mg sodiu
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="extreme-card" style="border-top: 3px solid #3ecf8e;">
        <div class="ec-label" style="color:#3ecf8e;">Cel mai puțin caloric produs</div>
        <div class="ec-name">{min_row['Item']}</div>
        <div class="ec-brand">{min_row['Brand']} &nbsp;·&nbsp; {min_row['Category']}</div>
        <div class="ec-stats">
            {min_row['Calories']} kcal<br>
            {min_row['Total Fat (g)']} g grăsimi<br>
            {min_row['Protein (g)']} g proteină<br>
            {min_row['Sodium (mg)']} mg sodiu
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Rezumat ───────────────────────────────────────────────────────
st.markdown('<div class="sec-header">Ce am învățat</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>st.session_state</code> — partajarea datelor între pagini</li>
            <li><code>st.dataframe()</code> — tabel interactiv cu sortare</li>
            <li><code>st.metric()</code> — indicatori cheie vizuali</li>
            <li><code>st.stop()</code> — oprirea execuției condiționat</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="summary-box">
        <ul>
            <li><code>df.describe()</code> — statistici automate Pandas</li>
            <li><code>df.dtypes</code> — tipurile coloanelor</li>
            <li><code>df.isnull().sum()</code> — valori lipsă</li>
            <li><code>df.loc[df[col].idxmax()]</code> — rândul cu valoarea maximă</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Continuă cu pagina 2: Filtrare & Explorare")

st.markdown("---")
st.markdown('<p style="text-align:center;color:#444;font-size:12px;font-family:\'IBM Plex Mono\',monospace;">Fast Food Dashboard · Seminar 3 · Python & Streamlit</p>', unsafe_allow_html=True)
