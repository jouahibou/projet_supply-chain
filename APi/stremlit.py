import streamlit as st
import requests
from streamlit_viz import show_comment_distri_by_stars,show_comment_distri_by_loc,filter_by_rating,plot_review_timeline
import pandas as pd
from import_database import import_data_from_es
from PIL import Image


# Définir l'URL de la route de prédiction
PREDICTION_URL = "http://localhost:8000/data_prediction_new_comment"

df = import_data_from_es(host = "http://79.125.3.215:9200", index = "asurion")

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
    
def page2():
    # Créer une liste des noms de fichiers d'images
    image_files = ["image1.png", "image2.png", "image3.png", "image4.png","image5.png"]

    # Créer une liste de titres correspondant aux images
    image_titles = ["Rated 1 out of 5 stars", "Rated 2 out of 5 stars", "Rated 3 out of 5 stars", "Rated 4 out of 5 stars","Rated 5 out of 5 stars"]

    # Demander à l'utilisateur de choisir une image
    selected_image = st.selectbox("nuange de mots", image_titles)

    # Trouver l'index de l'image sélectionnée dans la liste des titres
    index = image_titles.index(selected_image)

    # Charger l'image sélectionnée à partir du fichier
    image = Image.open(image_files[index])

    # Afficher l'image sur Streamlit
    st.image(image, caption=selected_image, use_column_width=True)    



    

# Créer les composants de navigation
menu = ["Accueil", "Comments","Nuages de mots"]
choice = st.sidebar.selectbox("Navigation", menu)

# Afficher la page en fonction du choix de l'utilisateur
if choice == "Accueil":
    home()
elif choice == "Comments":
    page1()
else:
    page2()    
    
    
    
    