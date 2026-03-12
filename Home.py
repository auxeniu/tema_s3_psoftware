import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Fast Food Dashboard",
    page_icon="🍔",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=IBM+Plex+Mono:wght@400;500&family=DM+Sans:wght@400;500;600&display=swap');

:root {
    --bg:       #0f0f0f;
    --surface:  #1a1a1a;
    --border:   #2e2e2e;
    --accent:   #ff5c00;
    --accent2:  #ffb347;
    --text:     #e8e8e8;
    --muted:    #888;
    --success:  #3ecf8e;
    --mono:     'IBM Plex Mono', monospace;
    --display:  'Syne', sans-serif;
    --body:     'DM Sans', sans-serif;
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: var(--body) !important;
}

h1, h2, h3, h4 {
    font-family: var(--display) !important;
    color: var(--text) !important;
    letter-spacing: -0.5px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #141414 !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Streamlit default elements */
[data-testid="stMarkdownContainer"] p { color: var(--text) !important; }
.stAlert p { color: #0f0f0f !important; }

/* Hero */
.hero {
    border-top: 4px solid var(--accent);
    background: var(--surface);
    padding: 48px 52px;
    border-radius: 4px;
    margin-bottom: 40px;
}
.hero-label {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.hero-title {
    font-family: var(--display);
    font-size: 64px;
    font-weight: 800;
    color: var(--text);
    line-height: 1;
    margin: 0 0 16px 0;
}
.hero-sub {
    font-size: 17px;
    color: #aaa;
    max-width: 600px;
    line-height: 1.6;
}

/* Section headers */
.sec-header {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    margin: 44px 0 20px 0;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
}

/* Page cards */
.page-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 4px;
}
.page-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 22px 26px;
    transition: border-color 0.2s;
}
.page-card:hover { border-color: var(--accent); }
.page-num {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 2px;
    margin-bottom: 6px;
}
.page-name {
    font-family: var(--display);
    font-size: 17px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 8px;
}
.page-desc {
    font-size: 13.5px;
    color: #999;
    line-height: 1.55;
}

/* Structure box */
.struct-box {
    background: #111;
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 4px;
    padding: 22px 26px;
    font-family: var(--mono);
    font-size: 13px;
    color: #ccc;
    line-height: 1.9;
}
.struct-box .hl { color: var(--accent); font-weight: 500; }
.struct-box .dim { color: #555; }

/* Tip box */
.tip {
    background: #1a1a1a;
    border: 1px solid #2e2e2e;
    border-left: 3px solid var(--accent2);
    border-radius: 4px;
    padding: 18px 22px;
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

/* Upload area */
.upload-prompt {
    border: 1.5px dashed #3a3a3a;
    border-radius: 6px;
    padding: 32px;
    text-align: center;
    color: #666;
    font-size: 15px;
    margin: 16px 0;
}
.upload-prompt strong { color: var(--accent); }

/* Success banner */
.ok-banner {
    background: #0f2a1e;
    border: 1px solid #1e5c3a;
    border-left: 4px solid var(--success);
    border-radius: 4px;
    padding: 18px 24px;
    color: #a8eecb;
    font-size: 15px;
    line-height: 1.6;
}
.ok-banner strong { color: var(--success); }

/* Stat pills */
.stat-row {
    display: flex;
    gap: 14px;
    margin-top: 16px;
    flex-wrap: wrap;
}
.stat-pill {
    background: #1f1f1f;
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 12px 20px;
    text-align: center;
    min-width: 110px;
}
.stat-pill .sv {
    font-family: var(--display);
    font-size: 26px;
    color: var(--accent);
    line-height: 1;
}
.stat-pill .sl {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────
st.sidebar.markdown("### 🍔 Fast Food Dashboard")
st.sidebar.markdown("**Seminar 3 — Python & Streamlit**")
st.sidebar.markdown("---")

# ── Hero ─────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-label">Seminar 3 &nbsp;/&nbsp; Python &amp; Streamlit</div>
    <div class="hero-title">Fast Food<br>Dashboard</div>
    <div class="hero-sub">
        Un dashboard complet de date — de la încărcarea unui CSV până la vizualizări
        interactive și deployment live. Pandas, Matplotlib, Plotly, Streamlit.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Structura proiectului ─────────────────────────────────────────
st.markdown('<div class="sec-header">Structura proiectului</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    <div class="struct-box">
        fastfood_dashboard/<br>
        <span class="dim">│</span><br>
        <span class="dim">├──</span> <span class="hl">Home.py</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="dim">← pagina principală (ești aici)</span><br>
        <span class="dim">├──</span> fastfood_dataset.csv &nbsp;&nbsp;<span class="dim">← datele</span><br>
        <span class="dim">└──</span> pages/<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="dim">├──</span> 1_Date_si_Statistici.py<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="dim">├──</span> 2_Filtrare_si_Explorare.py<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="dim">├──</span> 3_Vizualizari_Matplotlib.py<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="dim">├──</span> 4_Vizualizari_Plotly.py<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="dim">├──</span> 5_Quiz.py<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="dim">└──</span> 6_Proiect_de_Grup.py
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tip">
        <strong>Reguli multipage Streamlit</strong><br><br>
        <code>st.set_page_config()</code> — doar în <code>Home.py</code><br><br>
        Fișierele din <code>pages/</code> sunt detectate automat de Streamlit<br><br>
        Prefixul numeric (<code>1_</code>, <code>2_</code>...) controlează ordinea din sidebar<br><br>
        <code>st.session_state</code> este partajat între toate paginile<br><br>
        Se rulează cu: <code>python -m streamlit run Home.py</code>
    </div>
    """, unsafe_allow_html=True)

# ── Paginile seminarului ──────────────────────────────────────────
st.markdown('<div class="sec-header">Ce vom învăța</div>', unsafe_allow_html=True)

st.markdown("""
<div class="page-grid">
    <div class="page-card">
        <div class="page-num">PAGINA 01</div>
        <div class="page-name">Date & Statistici</div>
        <div class="page-desc">Încărcarea unui CSV cu <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">st.file_uploader()</code>, previzualizare cu <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">st.dataframe()</code>, statistici cu <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">st.metric()</code> și <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">df.describe()</code>.</div>
    </div>
    <div class="page-card">
        <div class="page-num">PAGINA 02</div>
        <div class="page-name">Filtrare & Explorare</div>
        <div class="page-desc">Filtrarea datelor cu Pandas, sidebar cu widget-uri interactive, grafice rapide cu <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">st.bar_chart()</code> și <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">st.line_chart()</code>.</div>
    </div>
    <div class="page-card">
        <div class="page-num">PAGINA 03</div>
        <div class="page-name">Vizualizări Matplotlib</div>
        <div class="page-desc">Grafice statice personalizate: bar chart, pie chart, histogram. Integrare în Streamlit cu <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">st.pyplot()</code>.</div>
    </div>
    <div class="page-card">
        <div class="page-num">PAGINA 04</div>
        <div class="page-name">Vizualizări Plotly</div>
        <div class="page-desc">Grafice interactive cu hover, zoom și filtrare. Comparații între branduri cu <code style="background:#2a2a2a;padding:1px 5px;border-radius:3px;font-size:12px;">st.plotly_chart()</code>.</div>
    </div>
    <div class="page-card">
        <div class="page-num">PAGINA 05</div>
        <div class="page-name">Quiz</div>
        <div class="page-desc">Întrebări interactive despre conceptele din seminar, cu feedback imediat și scor final.</div>
    </div>
    <div class="page-card">
        <div class="page-num">PAGINA 06</div>
        <div class="page-name">Proiect de Grup + Deploy</div>
        <div class="page-desc">Construiește propriul dashboard și publică-l live pe Streamlit Community Cloud — gratuit, în câțiva pași.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Încărcare date ────────────────────────────────────────────────
st.markdown('<div class="sec-header">Încarcă dataset-ul</div>', unsafe_allow_html=True)

st.markdown("""
Încarcă fișierul **fastfood_dataset.csv** o singură dată, aici.
Datele sunt salvate în `st.session_state` și rămân disponibile în toate paginile aplicației.
""")

with st.expander("De ce session_state?"):
    st.code("""
# Nu uitati!!!
# Streamlit reexecută întregul script la fiecare interacțiune.
# Fără session_state, DataFrame-ul s-ar pierde la fiecare click.

# În Home.py — salvăm datele:
st.session_state["df"] = pd.read_csv(fisier)

# În orice pagină din pages/ — le recuperăm:
if "df" not in st.session_state:
    st.warning("Te rog încarcă datele din pagina Home.")
    st.stop()

df = st.session_state["df"]
""", language="python")

if "df" not in st.session_state:
    st.markdown('<div class="upload-prompt">Încarcă fișierul <strong>fastfood_dataset.csv</strong> pentru a activa toate paginile</div>', unsafe_allow_html=True)
    fisier = st.file_uploader("Alege fișierul CSV", type=["csv"], label_visibility="collapsed")
    if fisier is not None:
        df = pd.read_csv(fisier,encoding="latin1")
        st.session_state["df"] = df
        st.rerun()
else:
    df = st.session_state["df"]
    st.markdown(f"""
    <div class="ok-banner">
        <strong>Date încărcate.</strong> Dataset-ul conține
        <strong>{len(df)} produse</strong> de la
        <strong>{df['Brand'].nunique()} branduri</strong> în
        <strong>{df['Category'].nunique()} categorii</strong>.
        Poți naviga liber între toate paginile.
    </div>
    <div class="stat-row">
        <div class="stat-pill"><div class="sv">{len(df)}</div><div class="sl">Produse</div></div>
        <div class="stat-pill"><div class="sv">{df['Brand'].nunique()}</div><div class="sl">Branduri</div></div>
        <div class="stat-pill"><div class="sv">{df['Category'].nunique()}</div><div class="sl">Categorii</div></div>
        <div class="stat-pill"><div class="sv">{df['Calories'].mean():.0f}</div><div class="sl">Kcal medii</div></div>
        <div class="stat-pill"><div class="sv">{df['Calories'].max():.0f}</div><div class="sl">Kcal max</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(df.head(5), use_container_width=True)

    if st.button("Încarcă un alt fișier"):
        del st.session_state["df"]
        st.rerun()

# ── Footer ────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<p style="text-align:center; color:#444; font-size:13px; font-family:\'IBM Plex Mono\', monospace;">Fast Food Dashboard · Seminar 3 · Python & Streamlit</p>', unsafe_allow_html=True)