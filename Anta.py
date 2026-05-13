import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Anta Dieye | Medical Portfolio",
    page_icon="👩🏿‍⚕️",
    layout="wide"
)

# =========================
# STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================
# GLOBAL STYLE PREMIUM
# =========================
st.markdown("""
<style>

/* 🌈 BACKGROUND PREMIUM MODERNE */
.stApp {
    background: linear-gradient(135deg, #eef2f7 0%, #f7f9fc 40%, #eef6ff 100%);
    animation: appFade 0.9s ease-in-out;
}

/* ENTRY ANIMATION */
@keyframes appFade {
    from {
        opacity: 0;
        transform: translateY(12px);
        filter: blur(6px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}

/* TITRES */
h1 {
    text-align: center;
    color: #0b1f3a;
    font-weight: 800;
}

h2, h3 {
    color: #1f3b5c;
}

/* CARD PREMIUM */
.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e6eaf0;
    box-shadow: 0px 10px 28px rgba(0,0,0,0.06);
    margin-bottom: 16px;
    transition: all 0.35s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 20px 45px rgba(0,0,0,0.12);
}

/* BUTTONS */
.stButton button {
    border-radius: 12px;
    border: 1px solid #e6eaf0;
    background: white;
    transition: 0.3s;
}

.stButton button:hover {
    background: #0b1f3a;
    color: white;
    transform: translateY(-3px);
}

/* METRICS */
[data-testid="stMetric"] {
    transition: 0.3s;
}

[data-testid="stMetric"]:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("👩🏿‍⚕️ Anta Dieye")
st.subheader("Sage-femme d'État | Échographiste obstétricale | Santé maternelle & néonatale")

st.success("📍 Saint-Louis, Sénégal | 📧 dieyeanta629@gmail.com")

# =========================
# DASHBOARD
# =========================
c1, c2, c3 = st.columns(3)

c1.metric("Expérience", "9+ ans")
c2.metric("Langues", "3")
c3.metric("Domaines", "6")

# =========================
# NAVIGATION
# =========================
col1, col2, col3, col4, col5 = st.columns(5)

if col1.button("🏠 Accueil"):
    st.session_state.page = "home"
if col2.button("💼 Expériences"):
    st.session_state.page = "exp"
if col3.button("🎓 Formation"):
    st.session_state.page = "edu"
if col4.button("🧠 Compétences"):
    st.session_state.page = "skills"
if col5.button("📞 Contact"):
    st.session_state.page = "contact"

# =========================
# HOME
# =========================
if st.session_state.page == "home":

    st.markdown("""
    <div class="card">
    <h3>👩🏿‍⚕️ Profil professionnel</h3>
    <p>
    Sage-femme d'État avec plus de 9 ans d'expérience en santé maternelle et néonatale.
    Spécialisée en échographie obstétricale, SONUB, planification familiale et gestion communautaire.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # LANGUES
    st.markdown("### 🗣️ Langues")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Français\n\n✔ Excellent")
    with col2:
        st.markdown("Wolof\n\n✔ Excellent")
    with col3:
        st.markdown("Anglais\n\n✔ Débutant")

    # SPECIALITES
    st.markdown("### 🧠 Spécialités")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Échographie obstétricale")
    with col2:
        st.markdown("SONUB")
    with col3:
        st.markdown("Santé reproductive")

# =========================
# EXPERIENCE
# =========================
elif st.session_state.page == "exp":

    st.header("💼 Expériences professionnelles")

    st.markdown("""
    <div class="card">
    <h3>2025 - DJINAKY</h3>
    <p>Sage-femme échographiste | SONUB | urgences obstétricales</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>2021 - 2024 KAFOUNTINE</h3>
    <p>Coordination santé communautaire | suivi indicateurs santé</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>2020 - 2021 MEKHE</h3>
    <p>Accouchements | vaccination | dépistage</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>2018 - 2019 EPS / CLINIQUES</h3>
    <p>Salle d’accouchement | soins obstétricaux | surveillance maternité</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FORMATION
# =========================
elif st.session_state.page == "edu":

    st.header("🎓 Formation académique")

    st.markdown("""
    <div class="card">
    CEFOREP - Échographie obstétricale (2024)<br>
    PNLP - Paludologie (2023)<br>
    ESUP - Licence soins obstétricaux<br>
    UGB - Langue française<br>
    Baccalauréat scientifique
    </div>
    """, unsafe_allow_html=True)

# =========================
# COMPETENCES (VERSION AMÉLIORÉE)
# =========================
elif st.session_state.page == "skills":

    st.header("🧠 Compétences professionnelles")

    st.markdown("""
    <div class="card">
    <h3>⚕️ Compétences cliniques</h3>
    <p>Échographie obstétricale, suivi grossesse à risque, urgences obstétricales</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🤰 Santé maternelle</h3>
    <p>CPN / CPON, planification familiale, prise en charge IST</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🏥 Santé publique</h3>
    <p>Vaccination PEV, santé communautaire, sensibilisation</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>💻 Digital & gestion</h3>
    <p>DHIS2, reporting santé, gestion des données médicales</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# CONTACT
# =========================
elif st.session_state.page == "contact":

    st.header("📞 Contact professionnel")

    st.markdown("""
    <div class="card">
    <p>👩🏿‍⚕️ Anta Dieye</p>
    <p>📍 Saint-Louis, Sénégal</p>
    <p>📧 dieyeanta629@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

    st.success("Disponible immédiatement pour collaboration")