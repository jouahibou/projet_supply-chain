import requests
import json

# Créer un document
data = {
    "titre": "titanic",
    "nom": "jouahibou",
    "stars": 4.5,
    "localisation": "Paris",
    "nb_reviews": 10,
    "date_review": "2022-06-20",
    "date_experience": "2022-06-15",
    "comment": "C'était un excellent séjour !"
}
#response = requests.post('http://localhost:8000/documents/asurion', json=data)
#print(response.json())


# Lire un document
#response = requests.get('http://localhost:8000/documents/asurion/M6-HJ4kB2lCuUadSSTsI')
#doc = response.json()
#if doc is not None:
 #   print(doc)
#else:
#    print('Document not found')
    
data = {
    "titre": "data engineer",
    "nom": "DataScientest",
    "stars": 4.5,
    "localisation": "Paris",
    "nb_reviews": 10,
    "date_review": "2022-06-20",
    "date_experience": "2022-06-15",
    "comment": "C'était un excellent séjour !"
}
#response = requests.put('http://localhost:8000/documents/asurion/M6-HJ4kB2lCuUadSSTsI', json=data)
#print(response.json())

# Supprimer un document
#response = requests.delete('http://localhost:8000/documents/asurion/M6-HJ4kB2lCuUadSSTsI')
#print(response.json())




# URL de l'API
url = "http://localhost:8000/predict/"

# Phrase à prédire
sentence = "excellent service with any insurance claim you obviously have to explain the damage and click through the fraud acknowledgements, etc. that was not difficult at all.after that, the process was slick slick slick. the claim was filed late on a thursday afternoon and the replacement arrived on the friday morning.clear instructions the whole way and a very simple process"

# Envoyer une requête POST à l'API
response = requests.post(url + sentence)

import requests

# URL de votre API FastAPI
url = "http://localhost:8000/predict/"

# Texte à prédire
sentence = "Ceci est un exemple de texte à prédire."

# Envoyer une requête POST avec le texte comme paramètre
response = requests.post(url + sentence)

# Vérifier que la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Récupérer la prédiction depuis la réponse
    prediction = response.json()["prediction"]
    print(f"La prédiction pour le texte '{sentence}' est : {prediction}")
else:
    print("La requête a échoué avec le code de statut :", response.status_code)