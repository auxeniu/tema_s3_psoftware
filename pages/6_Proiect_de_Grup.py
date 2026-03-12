import streamlit as st

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

.step-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 24px 28px;
    margin-bottom: 14px;
    display: flex;
    gap: 20px;
    align-items: flex-start;
}
.step-num {
    font-family: var(--display);
    font-size: 42px;
    font-weight: 800;
    color: #2e2e2e;
    line-height: 1;
    min-width: 48px;
}
.step-body .step-title {
    font-family: var(--display);
    font-size: 18px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 6px;
}
.step-body .step-time {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.step-body p {
    font-size: 14px;
    color: #bbb !important;
    line-height: 1.7;
    margin: 0;
}
.step-body code {
    background: #2a2a2a;
    padding: 1px 6px;
    border-radius: 3px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent2);
}

.dataset-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 22px 26px;
    height: 100%;
    transition: border-color 0.2s;
}
.dataset-card:hover { border-color: var(--accent); }
.dataset-tag {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.dataset-title {
    font-family: var(--display);
    font-size: 18px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 8px;
}
.dataset-desc {
    font-size: 13.5px;
    color: #999;
    line-height: 1.6;
    margin-bottom: 14px;
}
.dataset-cols {
    font-family: var(--mono);
    font-size: 11px;
    color: #666;
    line-height: 1.8;
}
.dataset-cols span {
    color: var(--accent2);
}

.req-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 4px;
}
.req-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 16px 20px;
    font-size: 14px;
    color: #ccc;
    line-height: 1.6;
}
.req-item .req-label {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--success);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.req-item code {
    background: #2a2a2a;
    padding: 1px 5px;
    border-radius: 3px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent2);
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

.deploy-step {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 20px 24px;
    margin-bottom: 12px;
}
.deploy-step .ds-num {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.deploy-step .ds-title {
    font-family: var(--display);
    font-size: 16px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 8px;
}
.deploy-step p {
    font-size: 14px;
    color: #bbb !important;
    line-height: 1.7;
    margin: 0;
}
.deploy-step code {
    background: #2a2a2a;
    padding: 1px 6px;
    border-radius: 3px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent2);
}

.present-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 3px solid var(--accent);
    border-radius: 4px;
    padding: 24px 28px;
}
.present-card .pc-title {
    font-family: var(--display);
    font-size: 18px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 14px;
}
.present-card ul {
    margin: 0;
    padding-left: 18px;
    color: #bbb;
    font-size: 14px;
    line-height: 2.1;
}
.present-card code {
    background: #2a2a2a;
    padding: 1px 5px;
    border-radius: 3px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent2);
}

.timer-banner {
    background: #1a1109;
    border: 1px solid #3d2a00;
    border-left: 4px solid var(--accent2);
    border-radius: 4px;
    padding: 18px 24px;
    font-size: 15px;
    color: #f5d49a;
    line-height: 1.7;
    margin-bottom: 8px;
}
.timer-banner strong { color: var(--accent2); }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="label">Pagina 06</div>
    <h1>Proiect de Grup</h1>
    <div class="sub">30 de minute · 2-4 studenți · deploy live pe Streamlit Community Cloud</div>
</div>
""", unsafe_allow_html=True)

# ── Contextul misiunii ────────────────────────────────────────────
st.markdown('<div class="sec-header">Misiunea</div>', unsafe_allow_html=True)

st.markdown("""
<div class="timer-banner">
    <strong>Scenariul:</strong> Ești angajat(ă) la o firmă de analiză de date.
    Clientul ți-a trimis un dataset și vrea un dashboard funcțional, publicat online,
    în 30 de minute. LLM-urile sunt permise — exact ca în lumea reală.
    La final, prezinți live, 2 minute, în fața clasei.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="background:#1a1a1a;border:1px solid #2e2e2e;border-top:3px solid #ff5c00;
                border-radius:4px;padding:18px;text-align:center;">
        <div style="font-family:'Syne',sans-serif;font-size:32px;font-weight:800;color:#ff5c00;">30</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:#888;
                    text-transform:uppercase;letter-spacing:1.5px;margin-top:4px;">minute</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="background:#1a1a1a;border:1px solid #2e2e2e;border-top:3px solid #ffb347;
                border-radius:4px;padding:18px;text-align:center;">
        <div style="font-family:'Syne',sans-serif;font-size:32px;font-weight:800;color:#ffb347;">2-4</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:#888;
                    text-transform:uppercase;letter-spacing:1.5px;margin-top:4px;">studenți / grup</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div style="background:#1a1a1a;border:1px solid #2e2e2e;border-top:3px solid #3ecf8e;
                border-radius:4px;padding:18px;text-align:center;">
        <div style="font-family:'Syne',sans-serif;font-size:32px;font-weight:800;color:#3ecf8e;">2'</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:#888;
                    text-transform:uppercase;letter-spacing:1.5px;margin-top:4px;">prezentare live</div>
    </div>
    """, unsafe_allow_html=True)

# ── Pașii proiectului ─────────────────────────────────────────────
st.markdown('<div class="sec-header">Pașii proiectului</div>', unsafe_allow_html=True)

st.markdown("""
<div class="step-card">
    <div class="step-num">01</div>
    <div class="step-body">
        <div class="step-title">Formați grupul și alegeți dataset-ul</div>
        <div class="step-time">0 — 5 minute</div>
        <p>Grupuri de 2-4 studenți. Decideți cine scrie codul, cine testează, cine pregătește prezentarea.
        Alegeți un dataset din lista de mai jos sau găsiți unul pe
        <a href="https://www.kaggle.com/datasets" target="_blank" style="color:#ff5c00;">kaggle.com/datasets</a>.
        Criteriu esențial: fișierul să fie <code>.csv</code>, să aibă coloane numerice și cel puțin 100 de rânduri.</p>
    </div>
</div>

<div class="step-card">
    <div class="step-num">02</div>
    <div class="step-body">
        <div class="step-title">Explorați dataset-ul</div>
        <div class="step-time">5 — 10 minute</div>
        <p>Deschideți fișierul CSV și înțelegeți ce coloane are, ce tipuri de date, ce întrebări interesante
        puteți răspunde cu el. Gândiți-vă la <strong>3 întrebări</strong> pe care dashboard-ul vostru să le răspundă.
        De exemplu: <em>„Care gen de filme are cel mai mare rating mediu?"</em> sau
        <em>„Ce exercițiu arde cele mai multe calorii?"</em></p>
    </div>
</div>

<div class="step-card">
    <div class="step-num">03</div>
    <div class="step-body">
        <div class="step-title">Construiți dashboard-ul</div>
        <div class="step-time">10 — 25 minute</div>
        <p>Folosiți template-ul de mai jos ca punct de start. LLM-urile sunt permise —
        dar fiecare linie de cod trebuie să fie înțeleasă de cel puțin un membru al grupului,
        pentru că veți fi întrebați la prezentare. Dashboard-ul trebuie să respecte cerințele minime
        din secțiunea de mai jos.</p>
    </div>
</div>

<div class="step-card">
    <div class="step-num">04</div>
    <div class="step-body">
        <div class="step-title">Deploy pe Streamlit Community Cloud</div>
        <div class="step-time">25 — 30 minute</div>
        <p>Publicați aplicația urmând ghidul de deploy de mai jos. La final veți avea un link public
        pe care îl trimiteți profesorului și îl prezentați clasei.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Cerințe minime ────────────────────────────────────────────────
st.markdown('<div class="sec-header">Cerințe minime</div>', unsafe_allow_html=True)

st.markdown("""
<div class="req-grid">
    <div class="req-item">
        <div class="req-label">Date</div>
        Cel puțin un <code>st.file_uploader()</code> sau dataset hardcodat.
        Date afișate cu <code>st.dataframe()</code> și statistici cu <code>st.metric()</code>.
    </div>
    <div class="req-item">
        <div class="req-label">Filtrare</div>
        Cel puțin un filtru interactiv în sidebar —
        <code>multiselect</code>, <code>slider</code> sau <code>selectbox</code>.
        DataFrame-ul afișat să se actualizeze în funcție de filtre.
    </div>
    <div class="req-item">
        <div class="req-label">Vizualizare</div>
        Cel puțin 2 grafice — unul Matplotlib sau Streamlit built-in,
        unul Plotly interactiv. Graficele să fie relevante pentru dataset, nu aleatorii.
    </div>
    <div class="req-item">
        <div class="req-label">Prezentare</div>
        Dashboard-ul publicat pe Streamlit Cloud cu link funcțional.
        Prezentare live de 2 minute: ce face aplicația, ce dataset ați ales, ce ați descoperit în date.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Dataset-uri sugerate ──────────────────────────────────────────
st.markdown('<div class="sec-header">Dataset-uri sugerate</div>', unsafe_allow_html=True)

st.markdown("Puteți folosi unul din dataset-urile de mai jos sau orice dataset `.csv` de pe [kaggle.com/datasets](https://www.kaggle.com/datasets).")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="dataset-card">
        <div class="dataset-tag">Opțiunea A</div>
        <div class="dataset-title">Fitness & Exerciții</div>
        <div class="dataset-desc">
            Un dataset cu exerciții fizice, grupuri musculare, calorii arse per minut
            și nivel de dificultate. Ideal pentru filtrare după tip de exercițiu
            și comparații calorice.
        </div>
        <div class="dataset-cols">
            Coloane: <span>Exercise, Calories_per_Hour, Difficulty,</span><br>
            <span>MuscleGroup, Equipment, Duration</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="dataset-card">
        <div class="dataset-tag">Opțiunea C</div>
        <div class="dataset-title">Cryptocurrency Prețuri Istorice</div>
        <div class="dataset-desc">
            Prețuri zilnice istorice pentru Bitcoin, Ethereum și alte criptomonede.
            Ideal pentru grafice liniare, comparații între monede și analiza volatilității.
        </div>
        <div class="dataset-cols">
            Coloane: <span>Date, Symbol, Open, High, Low,</span><br>
            <span>Close, Volume, Market_Cap</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="dataset-card">
        <div class="dataset-tag">Opțiunea B</div>
        <div class="dataset-title">Filme & Rating-uri IMDb</div>
        <div class="dataset-desc">
            Un dataset cu filme, genuri, ani de lansare, rating-uri IMDb,
            număr de voturi și venituri la box office.
            Ideal pentru comparații între genuri și evoluția rating-urilor în timp.
        </div>
        <div class="dataset-cols">
            Coloane: <span>Title, Year, Genre, Rating, Votes,</span><br>
            <span>Director, Runtime, Revenue</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="dataset-card">
        <div class="dataset-tag">Opțiunea D</div>
        <div class="dataset-title">Jocuri Video Steam</div>
        <div class="dataset-desc">
            Jocuri de pe platforma Steam cu prețuri, review-uri pozitive/negative,
            genuri și număr de jucători. Ideal pentru scatter plots preț vs rating
            și filtrare după gen sau studio.
        </div>
        <div class="dataset-cols">
            Coloane: <span>Name, Genre, Price, Positive_Reviews,</span><br>
            <span>Negative_Reviews, Developer, Release_Date</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="tip">
    <strong>Sau alegeți propriul dataset de pe Kaggle.</strong><br><br>
    Mergeți pe <a href="https://www.kaggle.com/datasets" target="_blank" style="color:#ff5c00;">kaggle.com/datasets</a>,
    căutați un subiect care vă interesează și descărcați un fișier <code>.csv</code>.
    Verificați înainte că are cel puțin <strong>100 de rânduri</strong>,
    <strong>coloane numerice</strong> pe care să le vizualizați
    și <strong>cel puțin o coloană categorică</strong> pentru filtrare.
</div>
""", unsafe_allow_html=True)

# ── Template starter ──────────────────────────────────────────────
st.markdown('<div class="sec-header">Template starter</div>', unsafe_allow_html=True)

st.markdown("Copiați codul de mai jos într-un fișier nou `dashboard.py` și modificați-l pentru dataset-ul vostru.")

st.code("""
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("Numele dashboardului vostru")  # TODO: schimbați titlul

# ── Încărcare date ────────────────────────────────────────────────
fisier = st.file_uploader("Încarcă fișierul CSV", type=["csv"])

if fisier is None:
    st.info("Încarcă un fișier CSV pentru a continua.")
    st.stop()

df = pd.read_csv(fisier)

# ── Statistici generale ───────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total înregistrări", len(df))
col2.metric("Coloane", len(df.columns))
col3.metric("...", "...")  # TODO: adăugați o metrică relevantă

st.dataframe(df.head(10), use_container_width=True)

# ── Filtre în sidebar ─────────────────────────────────────────────
st.sidebar.header("Filtre")

# TODO: înlocuiți 'coloana_categorica' cu numele coloanei voastre
optiuni = df["coloana_categorica"].unique().tolist()
selectie = st.sidebar.multiselect("Filtru", optiuni, default=optiuni)
df_filtrat = df[df["coloana_categorica"].isin(selectie)]

# ── Grafic 1 — Plotly ─────────────────────────────────────────────
st.subheader("Grafic 1")

# TODO: înlocuiți x și y cu coloanele voastre
fig = px.bar(
    df_filtrat.groupby("coloana_categorica")["coloana_numerica"].mean().reset_index(),
    x="coloana_categorica",
    y="coloana_numerica",
    color="coloana_categorica",
    title="Titlul graficului"  # TODO
)
st.plotly_chart(fig, use_container_width=True)

# ── Grafic 2 — Matplotlib ─────────────────────────────────────────
st.subheader("Grafic 2")

fig2, ax = plt.subplots(figsize=(9, 4))
ax.hist(df_filtrat["coloana_numerica"].dropna(), bins=20, color="#ff5c00", edgecolor="white")
ax.set_title("Distribuția valorilor")  # TODO
ax.set_xlabel("Valoare")
ax.set_ylabel("Frecvență")
st.pyplot(fig2)
plt.close(fig2)
""", language="python")

# ── Deploy pe Streamlit Cloud ─────────────────────────────────────
st.markdown('<div class="sec-header">Deploy pe Streamlit Community Cloud</div>', unsafe_allow_html=True)

st.markdown("Urmați acești 5 pași pentru a publica aplicația online, gratuit, în mai puțin de 5 minute.")

st.markdown("""
<div class="deploy-step">
    <div class="ds-num">Pasul 1</div>
    <div class="ds-title">Creați un repository pe GitHub</div>
    <p>Mergeți pe <a href="https://github.com" target="_blank" style="color:#ff5c00;">github.com</a>,
    creați un cont dacă nu aveți și creați un repository nou — public, cu orice nume.
    Încărcați în el două fișiere: <code>dashboard.py</code> și fișierul vostru <code>.csv</code>.</p>
</div>

<div class="deploy-step">
    <div class="ds-num">Pasul 2</div>
    <div class="ds-title">Adăugați fișierul requirements.txt</div>
    <p>Streamlit Cloud trebuie să știe ce librării să instaleze. Creați un fișier
    <code>requirements.txt</code> în repository cu conținutul de mai jos și încărcați-l pe GitHub.</p>
</div>
""", unsafe_allow_html=True)

st.code("""streamlit
pandas
plotly
matplotlib
""", language="text")

st.markdown("""
<div class="deploy-step">
    <div class="ds-num">Pasul 3</div>
    <div class="ds-title">Conectați-vă la Streamlit Community Cloud</div>
    <p>Mergeți pe <a href="https://share.streamlit.io" target="_blank" style="color:#ff5c00;">share.streamlit.io</a>
    și autentificați-vă cu contul de GitHub. Este gratuit și nu necesită card de credit.</p>
</div>

<div class="deploy-step">
    <div class="ds-num">Pasul 4</div>
    <div class="ds-title">Creați o nouă aplicație</div>
    <p>Apăsați <strong>New app</strong>, selectați repository-ul creat la pasul 1,
    alegeți branch-ul <code>main</code> și scrieți <code>dashboard.py</code> ca fișier principal.
    Apăsați <strong>Deploy</strong>.</p>
</div>

<div class="deploy-step">
    <div class="ds-num">Pasul 5</div>
    <div class="ds-title">Copiați link-ul și prezentați</div>
    <p>După 1-2 minute, aplicația este live la o adresă de forma
    <code>https://your-app-name.streamlit.app</code>.
    Copiați link-ul, trimiteți-l profesorului și pregătiți-vă prezentarea de 2 minute.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tip">
    <strong>Dacă deploy-ul durează prea mult</strong> — nu vă panicați.
    Prezentați mai întâi local cu <code>streamlit run dashboard.py</code>
    și publicați după seminar. Link-ul rămâne valabil permanent.
</div>
""", unsafe_allow_html=True)

# ── Prezentarea ───────────────────────────────────────────────────
st.markdown('<div class="sec-header">Prezentarea — 2 minute</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="present-card">
        <div class="pc-title">Ce prezentați</div>
        <ul>
            <li>Ce dataset ați ales și de ce</li>
            <li>Ce întrebări răspunde dashboard-ul</li>
            <li>Demo live — rulați aplicația și arătați filtrele și graficele</li>
            <li>Un lucru interesant descoperit în date</li>
            <li>Un lucru pe care l-ați fi făcut diferit cu mai mult timp</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="present-card">
        <div class="pc-title">Ce nu trebuie să faceți</div>
        <ul>
            <li>Nu citiți codul linie cu linie</li>
            <li>Nu prezentați slide-uri — doar aplicația live</li>
            <li>Nu vă scuzați că nu e perfect — arătați ce funcționează</li>
            <li>Nu vorbește doar un singur membru — fiecare spune cel puțin un lucru</li>
            <li>Nu depășiți 2 minute — exersați înainte</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding: 10px 0;">
    <div style="font-family:'Syne',sans-serif; font-size:22px; font-weight:800; color:#ff5c00;">
        Succes!
    </div>
    <div style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#444; margin-top:6px;">
        Fast Food Dashboard · Seminar 3 · Python & Streamlit
    </div>
</div>
""", unsafe_allow_html=True)
