import streamlit as st
import requests
from streamlit_viz import show_comment_distri_by_stars,show_comment_distri_by_loc,filter_by_rating,plot_review_timeline,generate_wordcloud
import pandas as pd


# Définir l'URL de la route de prédiction
PREDICTION_URL = "http://localhost:8000/data_prediction_new_comment"

df = pd.read_csv('asurion_complete.csv')

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
    filter_by_rating(df)

# Page 1
def page1():
    st.subheader("Supply_chain")
    plot_review_timeline(df)
    show_comment_distri_by_stars(df)
    show_comment_distri_by_loc(df)
    
    



    

# Créer les composants de navigation
menu = ["Accueil", "Page 1",]
choice = st.sidebar.selectbox("Navigation", menu)

# Afficher la page en fonction du choix de l'utilisateur
if choice == "Accueil":
    home()
elif choice == "Page 1":
    page1()
    
    
    
    