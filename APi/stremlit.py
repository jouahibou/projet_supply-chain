import streamlit as st
import requests
from Stats1 import pages1

# Définir l'URL de la route de prédiction
PREDICTION_URL = "http://localhost:8000/data_prediction_new_comment"

def predict_star_rating(review):
    params = {"review": review}
    response = requests.get(PREDICTION_URL, params=params)
    data = response.json()
    predicted_rating = data["predicted_star_comment"]
    return predicted_rating

# Page d'accueil
def home():
    st.title("Supply Chain ")
    st.subheader("Prédiction de note /5 pour les commentaires")
    # Créer deux colonnes pour saisir le commentaire et afficher la note prédite
    col1, col2 = st.columns(2)
    # Champ de texte pour saisir le commentaire
    with col1:
        review = st.text_input("Saisissez votre commentaire :")

    # Bouton pour soumettre le commentaire et afficher la note prédite
    with col2:
        if st.button("Prédire la note"):
            # Vérifier si le commentaire est vide
            if review == "":
                st.warning("Veuillez saisir un commentaire.")
            else:
                # Faire la prédiction
                predicted_rating = predict_star_rating(review)
                # Afficher la note prédite
                st.success(f"La note prédite pour votre commentaire est : {predicted_rating}/5")

# Page 1
def page1():
    pages1()


# Page 2
def page2():
    st.subheader("Page 2")
    # Contenu de la page 2

# Créer les composants de navigation
menu = ["Accueil", "Stats 1", "Page 2"]
choice = st.sidebar.selectbox("Navigation", menu)

# Afficher la page en fonction du choix de l'utilisateur
if choice == "Accueil":
    home()
elif choice == "Stats 1":
    page1()
else:
    page2()