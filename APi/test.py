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
response = requests.put('http://localhost:8000/documents/asurion/M6-HJ4kB2lCuUadSSTsI', json=data)
print(response.json())

# Supprimer un document
response = requests.delete('http://localhost:8000/documents/asurion/M6-HJ4kB2lCuUadSSTsI')
print(response.json())