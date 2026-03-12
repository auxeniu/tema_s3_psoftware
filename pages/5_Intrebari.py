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
    --error:   #f87171;
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

.q-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 24px 28px;
    margin-bottom: 20px;
}
.q-num {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.q-text {
    font-size: 16px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 6px;
    line-height: 1.5;
}
.q-hint {
    font-size: 13px;
    color: var(--muted);
    margin-bottom: 16px;
    font-family: var(--mono);
}

.correct {
    background: #0f2a1e;
    border: 1px solid #1e5c3a;
    border-left: 4px solid var(--success);
    border-radius: 4px;
    padding: 14px 18px;
    color: #a8eecb;
    font-size: 14px;
    margin-top: 8px;
}
.wrong {
    background: #2a0f0f;
    border: 1px solid #5c1e1e;
    border-left: 4px solid var(--error);
    border-radius: 4px;
    padding: 14px 18px;
    color: #fca5a5;
    font-size: 14px;
    margin-top: 8px;
}
.correct strong { color: var(--success); }
.wrong strong { color: var(--error); }

.score-card {
    border-radius: 4px;
    padding: 36px 40px;
    text-align: center;
    margin: 24px 0;
}
.score-card .sc-val {
    font-family: var(--display);
    font-size: 80px;
    font-weight: 800;
    line-height: 1;
}
.score-card .sc-sub {
    font-family: var(--mono);
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 10px;
}
.score-card .sc-msg {
    font-size: 16px;
    margin-top: 14px;
    color: #ccc;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="label">Pagina 05</div>
    <h1>Quiz</h1>
    <div class="sub">Testează-ți cunoștințele din seminarul de azi</div>
</div>
""", unsafe_allow_html=True)

# ── Întrebările quizului ──────────────────────────────────────────
INTREBARI = [
    {
        "sectiune": "Streamlit — Multipage & Session State",
        "intrebare": "Unde se plasează st.set_page_config() într-o aplicație multipage Streamlit?",
        "optiuni": [
            "În fiecare fișier din folderul pages/",
            "Doar în Home.py, o singură dată",
            "Nu este necesar în aplicațiile multipage",
            "În fișierul de configurare config.toml",
        ],
        "raspuns": "Doar în Home.py, o singură dată",
        "explicatie": "st.set_page_config() trebuie apelat o singură dată, ca primul element din Home.py. Dacă este pus în paginile din pages/, Streamlit va genera o eroare."
    },
    {
        "sectiune": "Streamlit — Multipage & Session State",
        "intrebare": "De ce folosim st.session_state pentru a stoca DataFrame-ul după încărcare?",
        "optiuni": [
            "Pentru că st.dataframe() necesită datele în session_state",
            "Pentru că Streamlit reexecută întregul script la fiecare interacțiune, iar variabilele locale se pierd",
            "Pentru a putea accesa datele din browser-ul utilizatorului",
            "Pentru a reduce consumul de memorie al aplicației",
        ],
        "raspuns": "Pentru că Streamlit reexecută întregul script la fiecare interacțiune, iar variabilele locale se pierd",
        "explicatie": "La fiecare click sau modificare a unui widget, Streamlit rulează scriptul de la zero. session_state păstrează valorile între aceste reexecutări."
    },
    {
        "sectiune": "Streamlit — Multipage & Session State",
        "intrebare": "Ce face st.stop() într-o pagină Streamlit?",
        "optiuni": [
            "Oprește serverul Streamlit",
            "Ascunde sidebar-ul aplicației",
            "Oprește execuția scriptului în acel punct — codul de după nu mai rulează",
            "Șterge toate datele din session_state",
        ],
        "raspuns": "Oprește execuția scriptului în acel punct — codul de după nu mai rulează",
        "explicatie": "st.stop() este util pentru a preveni erorile când datele necesare nu sunt disponibile. De exemplu, dacă df nu e în session_state, afișăm un warning și oprim execuția."
    },
    {
        "sectiune": "Pandas — Filtrare & Agregare",
        "intrebare": "Ce returnează df.groupby('Brand')['Calories'].mean()?",
        "optiuni": [
            "Un DataFrame cu toate coloanele, grupate după Brand",
            "O Serie Pandas cu media caloriilor pentru fiecare brand",
            "Numărul de produse din fiecare brand",
            "Un singur număr — media caloriilor din întregul dataset",
        ],
        "raspuns": "O Serie Pandas cu media caloriilor pentru fiecare brand",
        "explicatie": "groupby('Brand') creează grupuri, ['Calories'] selectează coloana, iar .mean() calculează media per grup. Rezultatul este o Serie cu brandul ca index."
    },
    {
        "sectiune": "Pandas — Filtrare & Agregare",
        "intrebare": "Care dintre următoarele filtrează corect produsele cu Calories > 500 ȘI Brand == 'KFC'?",
        "optiuni": [
            "df[df['Calories'] > 500 and df['Brand'] == 'KFC']",
            "df[df['Calories'] > 500 & df['Brand'] == 'KFC']",
            "df[(df['Calories'] > 500) & (df['Brand'] == 'KFC')]",
            "df.filter(Calories > 500, Brand == 'KFC')",
        ],
        "raspuns": "df[(df['Calories'] > 500) & (df['Brand'] == 'KFC')]",
        "explicatie": "În Pandas, condițiile multiple se combină cu & (și) sau | (sau), iar fiecare condiție trebuie înconjurată de paranteze. Operatorul 'and' din Python nu funcționează pe serii."
    },
    {
        "sectiune": "Pandas — Filtrare & Agregare",
        "intrebare": "Ce face df['Item'].str.contains('Chicken', case=False)?",
        "optiuni": [
            "Înlocuiește toate aparițiile cuvântului 'Chicken' cu un string gol",
            "Returnează o Serie booleană: True pentru rândurile unde Item conține 'Chicken' (indiferent de majuscule)",
            "Numără de câte ori apare 'Chicken' în coloana Item",
            "Filtrează DataFrame-ul și returnează doar rândurile cu 'Chicken'",
        ],
        "raspuns": "Returnează o Serie booleană: True pentru rândurile unde Item conține 'Chicken' (indiferent de majuscule)",
        "explicatie": "str.contains() returnează o mască booleană, nu un DataFrame filtrat. Pentru a filtra, folosim rezultatul ca index: df[df['Item'].str.contains('Chicken', case=False)]."
    },
    {
        "sectiune": "Matplotlib",
        "intrebare": "Care este ordinea corectă pentru a afișa un grafic Matplotlib în Streamlit?",
        "optiuni": [
            "plt.show() → st.pyplot()",
            "fig, ax = plt.subplots() → desenezi pe ax → st.pyplot(fig) → plt.close(fig)",
            "ax = plt.axes() → fig = plt.figure() → st.pyplot(ax)",
            "st.pyplot() → fig, ax = plt.subplots() → desenezi pe ax",
        ],
        "raspuns": "fig, ax = plt.subplots() → desenezi pe ax → st.pyplot(fig) → plt.close(fig)",
        "explicatie": "Întotdeauna creezi figura cu plt.subplots(), desenezi pe ax, trimiți fig la Streamlit cu st.pyplot(fig), apoi eliberezi memoria cu plt.close(fig). Nu folosi plt.show() în Streamlit."
    },
    {
        "sectiune": "Matplotlib",
        "intrebare": "Ce face ax.spines[['top', 'right']].set_visible(False)?",
        "optiuni": [
            "Elimină titlul și legenda graficului",
            "Ascunde bordurile de sus și din dreapta ale graficului, pentru un aspect mai curat",
            "Rotește graficul cu 90 de grade",
            "Setează culorile axelor la transparent",
        ],
        "raspuns": "Ascunde bordurile de sus și din dreapta ale graficului, pentru un aspect mai curat",
        "explicatie": "Spines sunt liniile care formează chenarul graficului. Ascunderea celor de sus și din dreapta este o tehnică de design comună care face graficul mai modern și mai ușor de citit."
    },
    {
        "sectiune": "Plotly",
        "intrebare": "Care este diferența principală dintre plotly.express și plotly.graph_objects?",
        "optiuni": [
            "plotly.express creează grafice 3D, graph_objects doar 2D",
            "plotly.express este gratuit, graph_objects necesită licență",
            "plotly.express oferă o sintaxă scurtă pentru grafice comune, graph_objects oferă control detaliat asupra fiecărui element",
            "plotly.express funcționează în Streamlit, graph_objects doar în Jupyter",
        ],
        "raspuns": "plotly.express oferă o sintaxă scurtă pentru grafice comune, graph_objects oferă control detaliat asupra fiecărui element",
        "explicatie": "px (plotly.express) este un strat de nivel înalt — scrii mai puțin cod pentru grafice standard. go (graph_objects) îți dă control total, ideal pentru grafice complexe sau personalizate, cum ar fi Heatmap."
    },
    {
        "sectiune": "Plotly",
        "intrebare": "Ce tip de grafic Plotly este cel mai potrivit pentru a arăta distribuția valorilor și outlierii unui dataset?",
        "optiuni": [
            "px.bar() — bar chart",
            "px.line() — grafic liniar",
            "px.box() — box plot",
            "px.pie() — pie chart",
        ],
        "raspuns": "px.box() — box plot",
        "explicatie": "Box plot-ul arată simultan mediana, cuartilele Q1 și Q3, valorile minime/maxime și outlierii — oferind o imagine completă a distribuției. Este mult mai informativ decât o simplă medie sau bar chart."
    },
]

# ── Inițializare session_state ────────────────────────────────────
if "quiz_raspunsuri" not in st.session_state:
    st.session_state.quiz_raspunsuri = {}
if "quiz_verificat" not in st.session_state:
    st.session_state.quiz_verificat = False
if "quiz_scor" not in st.session_state:
    st.session_state.quiz_scor = 0

# ── Instrucțiuni ──────────────────────────────────────────────────
st.markdown('<div class="sec-header">Instrucțiuni</div>', unsafe_allow_html=True)
st.markdown("""
Quizul conține **10 întrebări** organizate pe 4 teme: Streamlit Multipage, Pandas, Matplotlib și Plotly.
Selectează răspunsul pentru fiecare întrebare, apoi apasă **Verifică răspunsurile** la final.
""")

# ── Întrebările ───────────────────────────────────────────────────
sectiune_curenta = None

for i, q in enumerate(INTREBARI):

    # Header de secțiune când se schimbă tema
    if q["sectiune"] != sectiune_curenta:
        sectiune_curenta = q["sectiune"]
        st.markdown(f'<div class="sec-header">{sectiune_curenta}</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="q-card">
        <div class="q-num">Întrebarea {i + 1} din {len(INTREBARI)}</div>
        <div class="q-text">{q['intrebare']}</div>
    </div>
    """, unsafe_allow_html=True)

    raspuns_ales = st.radio(
        label=f"q_{i}",
        options=q["optiuni"],
        index=None,
        key=f"radio_{i}",
        label_visibility="collapsed"
    )

    if raspuns_ales:
        st.session_state.quiz_raspunsuri[i] = raspuns_ales

    # Feedback imediat după verificare
    if st.session_state.quiz_verificat and i in st.session_state.quiz_raspunsuri:
        ales = st.session_state.quiz_raspunsuri[i]
        corect = q["raspuns"]
        if ales == corect:
            st.markdown(f"""
            <div class="correct">
                <strong>Corect!</strong> {q['explicatie']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="wrong">
                <strong>Incorect.</strong> Răspunsul corect este: <strong>{corect}</strong><br><br>
                {q['explicatie']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

# ── Butoane ───────────────────────────────────────────────────────
st.markdown('<div class="sec-header">Rezultat</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("Verifică răspunsurile", type="primary", use_container_width=True):
        raspuns_lipsa = [i + 1 for i in range(len(INTREBARI)) if i not in st.session_state.quiz_raspunsuri]
        if raspuns_lipsa:
            st.warning(f"Nu ai răspuns la întrebările: {', '.join(map(str, raspuns_lipsa))}")
        else:
            scor = sum(
                1 for i, q in enumerate(INTREBARI)
                if st.session_state.quiz_raspunsuri.get(i) == q["raspuns"]
            )
            st.session_state.quiz_scor = scor
            st.session_state.quiz_verificat = True
            st.rerun()

with col2:
    if st.button("Resetează quizul", use_container_width=True):
        st.session_state.quiz_raspunsuri = {}
        st.session_state.quiz_verificat = False
        st.session_state.quiz_scor = 0
        st.rerun()

# ── Scor final ────────────────────────────────────────────────────
if st.session_state.quiz_verificat:
    scor = st.session_state.quiz_scor
    total = len(INTREBARI)
    procent = scor / total

    if procent == 1.0:
        culoare, mesaj = "#3ecf8e", "Perfect! Ai răspuns corect la toate întrebările."
    elif procent >= 0.7:
        culoare, mesaj = "#ffb347", "Bine! Mai recitește explicațiile întrebărilor greșite."
    else:
        culoare, mesaj = "#f87171", "Mai exersează! Recitește paginile corespunzătoare și încearcă din nou."

    st.markdown(f"""
    <div class="score-card" style="background:#1a1a1a; border: 1px solid #2e2e2e; border-top: 4px solid {culoare};">
        <div class="sc-val" style="color:{culoare};">{scor}/{total}</div>
        <div class="sc-sub" style="color:{culoare};">scor final</div>
        <div class="sc-msg">{mesaj}</div>
    </div>
    """, unsafe_allow_html=True)

    # Progres per secțiune
    st.markdown("**Detalii per temă:**")
    sectiuni = {}
    for i, q in enumerate(INTREBARI):
        sec = q["sectiune"]
        if sec not in sectiuni:
            sectiuni[sec] = {"corect": 0, "total": 0}
        sectiuni[sec]["total"] += 1
        if st.session_state.quiz_raspunsuri.get(i) == q["raspuns"]:
            sectiuni[sec]["corect"] += 1

    cols = st.columns(len(sectiuni))
    for col, (sec, val) in zip(cols, sectiuni.items()):
        p = val["corect"] / val["total"]
        c = "#3ecf8e" if p == 1.0 else "#ffb347" if p >= 0.5 else "#f87171"
        col.markdown(f"""
        <div style="background:#1a1a1a; border:1px solid #2e2e2e; border-top:3px solid {c};
                    border-radius:4px; padding:16px; text-align:center;">
            <div style="font-family:'Syne',sans-serif; font-size:26px; font-weight:800; color:{c};">
                {val['corect']}/{val['total']}
            </div>
            <div style="font-family:'IBM Plex Mono',monospace; font-size:10px; color:#888;
                        text-transform:uppercase; letter-spacing:1px; margin-top:6px;">
                {sec.split('—')[-1].strip()}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Continuă cu pagina 6: Proiect de Grup + Deploy pe Streamlit Community Cloud.")

st.markdown("---")
st.markdown('<p style="text-align:center;color:#444;font-size:12px;font-family:\'IBM Plex Mono\',monospace;">Fast Food Dashboard · Seminar 3 · Python & Streamlit</p>', unsafe_allow_html=True)
