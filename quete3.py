import streamlit as st
from streamlit_authenticator import Authenticate

lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}
authenticator = Authenticate(
    lesDonneesDesComptes,
    "app_cookie",
    "random_key",
    30
)
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

if st.session_state['authentication_status'] is None:
    authenticator.login()

def accueil():
    st.title("Bienvenue sur ma page")
    st.image("https://animalux.fr/cdn/shop/articles/chat-noir-blanc.webp?v=1721545193&width=1500", use_container_width=True)

def photo_album_page():
    st.title("Bienvenue dans l'album de mon chat")
    st.write(f"Bonjour, {st.session_state['name']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://animalux.fr/cdn/shop/articles/chat-noir-blanc.webp?v=1721545193&width=1500", caption="Chat 1", use_container_width=True)
    with col2:
        st.image("https://www.assuropoil.fr/wp-content/uploads/chat-ecaille-de-tortue.png", caption="Chat 2", use_container_width=True)
    with col3:
        st.image("https://france3-regions.francetvinfo.fr/image/ioqGJbBjjk8McsAe7Oflhgs6Ofs/3872x2592/regions/2023/11/23/dsc-0025-1-655f21700b2c4927769660.jpg", caption="Chat 3", use_container_width=True)

st.sidebar.title("Navigation")

if 'page' not in st.session_state:
    st.session_state.page = "Accueil"

if st.sidebar.button('Accueil'):
    st.session_state.page = "Accueil"
if st.sidebar.button('Les photos de mon chat'):
    st.session_state.page = "Les photos de mon chat"

if st.session_state.get("authentication_status"):
    if st.session_state.page == "Les photos de mon chat":
        photo_album_page()
    else:
        accueil()
    
    if st.sidebar.button('Déconnexion'):
        st.session_state['authentication_status'] = None
        st.session_state.page = "Accueil"
        st.session_state.clear()

elif st.session_state.get("authentication_status") is False:
    st.error("L'username ou le mot de passe est incorrect")
elif st.session_state.get("authentication_status") is None:
    st.warning('Les champs username et mot de passe doivent être remplis')