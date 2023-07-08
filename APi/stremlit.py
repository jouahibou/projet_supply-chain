import streamlit as st
import requests

# Définir l'URL de la route de prédiction
PREDICTION_URL = "http://localhost:8000/data_prediction_new_comment"
# Définir l'URL de la route d'ajout de document
DOCUMENT_URL = "http://localhost:8000/documents/asurion"

# Définir la fonction pour ajouter un document
def add_document(index, document):
    response = requests.post(f"{DOCUMENT_URL}/{index}", json=document)
    return response.ok

# Définir la fonction de prédiction
def predict_star_rating(review):
    params = {"review": review}
    response = requests.get(PREDICTION_URL, params=params)
    data = response.json()
    predicted_rating =  data["predicted_star_comment"]
    return predicted_rating

# Définir l'application Streamlit
def main():
    # Titre de l'application
    st.title("Prédiction de note /5 pour les commentaires")

    # Créer deux colonnes pour saisir le commentaire et afficher la note prédite
    col1, col2 = st.columns(2)

    # Champ de texte pour saisir le commentaire
    with col1:
        review = st.text_input("Saisissez votre commentaire :")

    # Bouton pour soumettre le commentaire et afficher la note prédite
    with col2:
        if st.button("Prédire la note"):
            # Faire la prédiction
            predicted_rating = predict_star_rating(review)
            # Afficher la note prédite
            st.success(f"La note prédite pour votre commentaire est : {predicted_rating}/5")

    # Séparateur
    st.write("---")

    # Créer un conteneur pour ajouter le commentaire
    with st.container():
        st.subheader("Ajouter un document ")

        # Créer des champs de saisie pour les propriétés du document
        titre = st.text_input("Titre")
        nom = st.text_input("Nom")
        stars = st.number_input("Étoiles", min_value=0.0, max_value=5.0, step=0.1)
        localisation = st.text_input("Localisation")
        nb_reviews = st.number_input("Nombre de commentaires", min_value=0, step=1)
        date_review = st.date_input("Date de la critique")
        date_experience = st.date_input("Date de l'expérience")
        comment = st.text_area("Commentaire")

        # Bouton pour ajouter le document
        if st.button("Ajouter"):
            # Créer le document à partir des données saisies
            document = {
                "titre": titre,
                "nom": nom,
                "stars": stars,
                "localisation": localisation,
                "nb_reviews": nb_reviews,
                "date_review": str(date_review),
                "date_experience": str(date_experience),
                "comment": comment
            }

            # Ajouter le document à MongoDB
            success = add_document("asurion", document)
            if success:
                st.success("Le commentaire a été ajouté avec succès à la base de données MongoDB !")
            else:
                st.error("Une erreur s'est produite lors de l'ajout du commentaire à la base de données MongoDB.")    

if __name__ == "__main__":
    main()