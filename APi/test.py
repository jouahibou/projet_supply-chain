import requests
import json
import logging

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





# Phrase à prédire
#sentence = "excellent service with any insurance claim you obviously have to explain the damage and click through the fraud acknowledgements, etc. that was not difficult at all.after that, the process was slick slick slick. the claim was filed late on a thursday afternoon and the replacement arrived on the friday morning.clear instructions the whole way and a very simple process"

#import requests

#logging.basicConfig(filename='apps.log', level=logging.DEBUG)

#url = "http://localhost:8000/data_prediction_new_comment"
#params = {"review": sentence}

#response = requests.get(url, params=params)

#if response.ok:
#    data = response.json()
#    print("Note prédite:", data["predicted_star_comment"])
#else:
#    print("Erreur:", response.status_code, response.text)