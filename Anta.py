import streamlit as st

# ============================================================
# ANTA DIEYE — PORTFOLIO PROFESSIONNEL
# Version "Editorial / Medical Luxury"
# ============================================================

st.set_page_config(
    page_title="Anta Dieye | Portfolio professionnel",
    page_icon="👩🏿‍⚕️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# ÉTAT
# ============================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

# ============================================================
# DESIGN SYSTEM — CSS / ANIMATIONS
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --ink: #102a2d;
    --ink-soft: #496467;
    --teal: #087f73;
    --teal-dark: #075c55;
    --mint: #dff5ef;
    --cream: #fbfaf6;
    --gold: #c79b52;
    --white: #ffffff;
    --line: rgba(16,42,45,.10);
    --shadow: 0 22px 70px rgba(16,42,45,.10);
}

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 8% 8%, rgba(8,127,115,.12), transparent 28%),
        radial-gradient(circle at 92% 18%, rgba(199,155,82,.12), transparent 25%),
        linear-gradient(135deg, #fbfaf6 0%, #f3faf8 52%, #f8fbfa 100%);
    color: var(--ink);
    animation: pageIn .8s ease both;
}

@keyframes pageIn {
    from { opacity:0; transform:translateY(14px); }
    to { opacity:1; transform:translateY(0); }
}

@keyframes float {
    0%,100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(8,127,115,.18); }
    50% { box-shadow: 0 0 0 14px rgba(8,127,115,0); }
}

@keyframes reveal {
    from { opacity:0; transform:translateY(25px); }
    to { opacity:1; transform:translateY(0); }
}

.block-container {
    max-width: 1250px;
    padding-top: 1.4rem;
    padding-bottom: 3rem;
}

#MainMenu, footer, header { visibility: hidden; }

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 34px;
    padding: 54px 58px;
    min-height: 430px;
    display: flex;
    align-items: center;
    background:
        radial-gradient(circle at 85% 20%, rgba(199,155,82,.25), transparent 23%),
        radial-gradient(circle at 72% 90%, rgba(8,127,115,.22), transparent 30%),
        linear-gradient(125deg, #0b3335 0%, #075c55 55%, #087f73 100%);
    color: white;
    box-shadow: 0 30px 90px rgba(7,92,85,.24);
    animation: reveal .8s ease both;
}

.hero:before {
    content: "";
    position: absolute;
    width: 290px;
    height: 290px;
    right: -85px;
    top: -85px;
    border: 1px solid rgba(255,255,255,.20);
    border-radius: 50%;
}

.hero:after {
    content: "";
    position: absolute;
    width: 390px;
    height: 390px;
    right: -135px;
    top: -135px;
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 50%;
}

.hero-copy {
    position: relative;
    z-index: 2;
    max-width: 820px;
}

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.18);
    font-size: .82rem;
    letter-spacing: .11em;
    text-transform: uppercase;
    margin-bottom: 22px;
}

.hero h1 {
    font-family: "Playfair Display", serif !important;
    font-size: clamp(3rem, 7vw, 5.8rem) !important;
    line-height: .96 !important;
    color: white !important;
    text-align: left !important;
    margin: 0 0 20px !important;
    letter-spacing: -.035em;
}

.hero h1 span { color: #f0d49b; }

.hero-sub {
    font-size: 1.15rem;
    line-height: 1.75;
    color: rgba(255,255,255,.84);
    max-width: 760px;
}

.hero-badge {
    position: absolute;
    right: 7%;
    bottom: 12%;
    width: 126px;
    height: 126px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.24);
    backdrop-filter: blur(12px);
    font-size: 3.2rem;
    animation: float 4s ease-in-out infinite;
}

.nav-shell {
    margin: 22px 0 30px;
    padding: 9px;
    border-radius: 22px;
    background: rgba(255,255,255,.78);
    border: 1px solid var(--line);
    box-shadow: 0 12px 35px rgba(16,42,45,.07);
    backdrop-filter: blur(15px);
}

.stButton button {
    width: 100%;
    min-height: 46px;
    border-radius: 15px !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    color: var(--ink) !important;
    font-weight: 700 !important;
    transition: all .25s ease !important;
}

.stButton button:hover {
    transform: translateY(-3px);
    background: var(--mint) !important;
    border-color: rgba(8,127,115,.18) !important;
    color: var(--teal-dark) !important;
    box-shadow: 0 10px 24px rgba(8,127,115,.10);
}

.section-kicker {
    color: var(--teal);
    text-transform: uppercase;
    letter-spacing: .16em;
    font-size: .76rem;
    font-weight: 800;
    margin-bottom: 7px;
}

.section-title {
    font-family: "Playfair Display", serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: var(--ink);
    margin-bottom: 8px;
}

.section-desc {
    color: var(--ink-soft);
    line-height: 1.75;
    margin-bottom: 25px;
}

.card {
    background: rgba(255,255,255,.86);
    border: 1px solid var(--line);
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 18px;
    box-shadow: 0 16px 45px rgba(16,42,45,.07);
    transition: transform .30s ease, box-shadow .30s ease, border-color .30s ease;
    animation: reveal .65s ease both;
}

.card:hover {
    transform: translateY(-7px);
    box-shadow: var(--shadow);
    border-color: rgba(8,127,115,.22);
}

.profile-card {
    background: linear-gradient(145deg, rgba(255,255,255,.94), rgba(223,245,239,.65));
}

.metric-card {
    text-align: center;
    padding: 24px 15px;
}

.metric-number {
    font-family: "Playfair Display", serif;
    color: var(--teal-dark);
    font-size: 2.4rem;
    font-weight: 700;
}

.metric-label {
    color: var(--ink-soft);
    font-size: .84rem;
    text-transform: uppercase;
    letter-spacing: .09em;
}

.icon-circle {
    width: 50px;
    height: 50px;
    display: grid;
    place-items: center;
    border-radius: 16px;
    background: var(--mint);
    color: var(--teal-dark);
    font-size: 1.35rem;
    margin-bottom: 15px;
}

.timeline {
    position: relative;
    margin: 18px 0 5px;
    padding-left: 32px;
}

.timeline:before {
    content: "";
    position: absolute;
    left: 8px;
    top: 8px;
    bottom: 8px;
    width: 2px;
    background: linear-gradient(var(--teal), rgba(8,127,115,.08));
}

.timeline-item {
    position: relative;
    margin-bottom: 18px;
    padding: 24px 26px;
    border-radius: 22px;
    background: rgba(255,255,255,.88);
    border: 1px solid var(--line);
    box-shadow: 0 13px 35px rgba(16,42,45,.06);
    transition: all .3s ease;
}

.timeline-item:hover {
    transform: translateX(7px);
    box-shadow: 0 22px 55px rgba(16,42,45,.11);
}

.timeline-item:before {
    content: "";
    position: absolute;
    left: -31px;
    top: 28px;
    width: 14px;
    height: 14px;
    background: var(--teal);
    border: 4px solid #eaf7f4;
    border-radius: 50%;
    animation: pulse 3s infinite;
}

.timeline-year {
    color: var(--gold);
    font-weight: 800;
    font-size: .84rem;
    letter-spacing: .1em;
    text-transform: uppercase;
}

.timeline-title {
    font-family: "Playfair Display", serif;
    font-size: 1.35rem;
    margin: 5px 0;
    color: var(--ink);
}

.skill-card {
    min-height: 190px;
}

.skill-card h3 {
    color: var(--ink);
    margin-bottom: 8px;
}

.tag {
    display: inline-block;
    padding: 7px 11px;
    margin: 4px 4px 0 0;
    border-radius: 999px;
    background: #edf8f5;
    color: var(--teal-dark);
    border: 1px solid rgba(8,127,115,.10);
    font-size: .82rem;
    font-weight: 600;
}

.contact-card {
    background: linear-gradient(135deg, #0b3335, #087f73);
    color: white;
    border: none;
    box-shadow: 0 25px 65px rgba(7,92,85,.25);
}

.contact-card h2, .contact-card p { color: white !important; }

.availability {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    margin-top: 12px;
    padding: 9px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.18);
}

.dot {
    width: 9px;
    height: 9px;
    background: #83e6bd;
    border-radius: 50%;
    box-shadow: 0 0 0 6px rgba(131,230,189,.12);
}

.footer {
    text-align: center;
    padding: 35px 0 10px;
    color: #6d8182;
    font-size: .82rem;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,.75);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 18px !important;
    box-shadow: 0 10px 30px rgba(16,42,45,.05);
    transition: transform .3s ease;
}

div[data-testid="stMetric"]:hover { transform: translateY(-5px); }

@media (max-width: 800px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero { padding: 38px 28px; min-height: 480px; }
    .hero h1 { font-size: 3.1rem !important; }
    .hero-badge { right: 7%; bottom: 7%; width: 90px; height: 90px; font-size: 2.2rem; }
    .section-title { font-size: 2rem; }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# NAVIGATION
# ============================================================
pages = {
    "home": ("⌂", "Accueil"),
    "exp": ("✦", "Expériences"),
    "edu": ("◇", "Formation"),
    "skills": ("✚", "Compétences"),
    "contact": ("✉", "Contact"),
}

st.markdown('<div class="nav-shell">', unsafe_allow_html=True)
nav_cols = st.columns(len(pages))
for col, (key, (icon, label)) in zip(nav_cols, pages.items()):
    with col:
        if st.button(f"{icon}  {label}", key=f"nav_{key}"):
            st.session_state.page = key
            st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# HERO — TOUJOURS VISIBLE
# ============================================================
st.markdown("""
<section class="hero">
    <div class="hero-copy">
        <div class="eyebrow">✦ Portfolio professionnel · Santé</div>
        <h1>Anta <span>Dieye</span></h1>
        <div class="hero-sub">
            Sage-femme d'État · Échographiste obstétricale ·
            Santé maternelle & néonatale
            <br><br>
            Une expertise construite autour de l'accompagnement des femmes,
            de la qualité des soins et de la santé communautaire.
        </div>
    </div>
    <div class="hero-badge">👩🏿‍⚕️</div>
</section>
""", unsafe_allow_html=True)

# ============================================================
# DASHBOARD
# ============================================================
st.write("")
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Expérience", "9+ ans", "Santé")
with m2:
    st.metric("Langues", "3", "Communication")
with m3:
    st.metric("Domaines", "6", "Expertise")
with m4:
    st.metric("Localisation", "Saint-Louis", "Sénégal")

st.write("")

# ============================================================
# HOME
# ============================================================
if st.session_state.page == "home":

    st.markdown("""
    <div class="section-kicker">01 · Profil</div>
    <div class="section-title">Une professionnelle engagée au service de la santé</div>
    <div class="section-desc">
        Parcourez le portfolio pour découvrir son parcours, ses compétences,
        ses formations et ses domaines d'intervention.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1.35, 1])

    with c1:
        st.markdown("""
        <div class="card profile-card">
            <div class="icon-circle">♡</div>
            <h2>Profil professionnel</h2>
            <p style="line-height:1.85;color:#496467;">
                Sage-femme d'État avec plus de 9 ans d'expérience en santé
                maternelle et néonatale. Spécialisée en échographie obstétricale,
                SONUB, planification familiale et gestion communautaire.
            </p>
            <div>
                <span class="tag">Échographie obstétricale</span>
                <span class="tag">SONUB</span>
                <span class="tag">Santé reproductive</span>
                <span class="tag">Santé communautaire</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="icon-circle">◎</div>
            <h2>Signature professionnelle</h2>
            <p style="line-height:1.85;color:#496467;">
                Une approche centrée sur la sécurité, l'écoute, la prévention
                et la qualité de la prise en charge maternelle et néonatale.
            </p>
            <p style="font-family:'Playfair Display',serif;font-size:1.25rem;color:#075c55;">
                « Soigner avec compétence, accompagner avec humanité. »
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-kicker" style="margin-top:30px;">02 · Langues</div>
    <div class="section-title">Communication</div>
    """, unsafe_allow_html=True)

    l1, l2, l3 = st.columns(3)
    for col, title, level in [
        (l1, "Français", "Excellent"),
        (l2, "Wolof", "Excellent"),
        (l3, "Anglais", "Débutant"),
    ]:
        with col:
            st.markdown(
                f"""<div class="card metric-card">
                    <div style="font-size:2rem;">◉</div>
                    <h3>{title}</h3>
                    <div class="metric-label">{level}</div>
                </div>""",
                unsafe_allow_html=True
            )

# ============================================================
# EXPÉRIENCES
# ============================================================
elif st.session_state.page == "exp":

    st.markdown("""
    <div class="section-kicker">03 · Parcours</div>
    <div class="section-title">Expériences professionnelles</div>
    <div class="section-desc">
        Un parcours progressif entre pratique clinique, échographie,
        urgences obstétricales et coordination communautaire.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline">

        <div class="timeline-item">
            <div class="timeline-year">2025 · DJINAKY</div>
            <div class="timeline-title">Sage-femme échographiste</div>
            <div style="color:#496467;line-height:1.7;">
                SONUB · urgences obstétricales
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-year">2021 — 2024 · KAFOUNTINE</div>
            <div class="timeline-title">Coordination santé communautaire</div>
            <div style="color:#496467;line-height:1.7;">
                Coordination santé communautaire · suivi des indicateurs de santé
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-year">2020 — 2021 · MEKHE</div>
            <div class="timeline-title">Pratique obstétricale & prévention</div>
            <div style="color:#496467;line-height:1.7;">
                Accouchements · vaccination · dépistage
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-year">2018 — 2019 · EPS / CLINIQUES</div>
            <div class="timeline-title">Soins obstétricaux</div>
            <div style="color:#496467;line-height:1.7;">
                Salle d'accouchement · soins obstétricaux · surveillance maternité
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FORMATION
# ============================================================
elif st.session_state.page == "edu":

    st.markdown("""
    <div class="section-kicker">04 · Formation</div>
    <div class="section-title">Formation académique & spécialisations</div>
    <div class="section-desc">
        Des formations complémentaires venant renforcer l'expertise clinique
        et la pratique en santé maternelle.
    </div>
    """, unsafe_allow_html=True)

    e1, e2 = st.columns(2)

    with e1:
        st.markdown("""
        <div class="card">
            <div class="icon-circle">⌁</div>
            <h3>CEFOREP</h3>
            <p style="color:#087f73;font-weight:700;">Échographie obstétricale · 2024</p>
            <p style="color:#496467;">Spécialisation en échographie obstétricale.</p>
        </div>

        <div class="card">
            <div class="icon-circle">+</div>
            <h3>PNLP</h3>
            <p style="color:#087f73;font-weight:700;">Paludologie · 2023</p>
        </div>

        <div class="card">
            <div class="icon-circle">◇</div>
            <h3>ESUP</h3>
            <p style="color:#087f73;font-weight:700;">Licence soins obstétricaux · 2015–2014</p>
        </div>
        """, unsafe_allow_html=True)

    with e2:
        st.markdown("""
        <div class="card">
            <div class="icon-circle">A</div>
            <h3>UGB</h3>
            <p style="color:#087f73;font-weight:700;">Langue française</p>
        </div>

        <div class="card">
            <div class="icon-circle">★</div>
            <h3>Baccalauréat</h3>
            <p style="color:#087f73;font-weight:700;">2012–2011</p>
        </div>

        <div class="card profile-card">
            <h3>Parcours en constante évolution</h3>
            <p style="color:#496467;line-height:1.8;">
                La formation académique est complétée par des spécialisations
                directement liées aux besoins de la pratique professionnelle.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# COMPÉTENCES
# ============================================================
elif st.session_state.page == "skills":

    st.markdown("""
    <div class="section-kicker">05 · Expertise</div>
    <div class="section-title">Compétences professionnelles</div>
    <div class="section-desc">
        Un profil multidimensionnel combinant expertise clinique,
        santé maternelle, santé publique et outils numériques.
    </div>
    """, unsafe_allow_html=True)

    skills = [
        ("⚕️", "Compétences cliniques",
         "Échographie obstétricale, suivi grossesse à risque, urgences obstétricales"),
        ("🤰", "Santé maternelle",
         "CPN / CPON, planification familiale, prise en charge IST"),
        ("🏥", "Santé publique",
         "Vaccination PEV, santé communautaire, sensibilisation"),
        ("⌘", "Digital & gestion",
         "DHIS2, reporting santé, gestion des données médicales"),
    ]

    cols = st.columns(2)
    for i, (icon, title, desc) in enumerate(skills):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card skill-card">
                <div class="icon-circle">{icon}</div>
                <h3>{title}</h3>
                <p style="color:#496467;line-height:1.8;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# CONTACT
# ============================================================
elif st.session_state.page == "contact":

    st.markdown("""
    <div class="section-kicker">06 · Contact</div>
    <div class="section-title">Construisons une collaboration utile</div>
    <div class="section-desc">
        Pour une collaboration professionnelle, une mission ou un échange
        autour de la santé maternelle et communautaire.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card contact-card">
        <div class="icon-circle" style="background:rgba(255,255,255,.12);color:white;">✉</div>
        <h2>Anta Dieye</h2>
        <p style="line-height:2;">
            📍 Saint-Louis, Sénégal<br>
            📧 dieyeanta629@gmail.com
        </p>
        <div class="availability">
            <span class="dot"></span>
            Disponible immédiatement pour collaboration
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
    <div style="font-family:'Playfair Display',serif;font-size:1.1rem;color:#075c55;">
        Anta Dieye · Portfolio professionnel
    </div>
    <div style="margin-top:7px;">
        Sage-femme d'État · Échographiste obstétricale · Santé maternelle & néonatale
    </div>
</div>
""", unsafe_allow_html=True)
