import streamlit as st
import requests

# Définition de la classe Input pour définir le format des données en entrée
class Input:
    def __init__(self, text: str):
        self.text = text

# Fonction pour appeler l'API FastAPI et obtenir la prédiction
def get_prediction(input_data: Input) -> int:
    url = "http://localhost:8000/predict"
    response = requests.post(url, json=input_data.__dict__)
    prediction = response.json()["prediction"]
    return prediction

# Fonction pour afficher l'interface utilisateur
def run_app():
    st.title("Prédiction binaire")

    # Saisie du texte
    text = st.text_area("Saisissez votre texte ici", height=200)

    # Création d'un objet Input à partir du texte saisi
    input_data = Input(text)

    # Faire une prédiction en appelant l'API FastAPI
    if st.button("Prédire"):
        prediction = get_prediction(input_data)
        st.write(f"La prédiction est {prediction}")

# Lancer l'interface utilisateur
if __name__ == "__main__":
    run_app()