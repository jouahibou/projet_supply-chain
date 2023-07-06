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



data = {'text': ["excellent service with any insurance claim you obviously have to explain the damage and click through the fraud acknowledgements, etc. that was not difficult at all.after that, the process was slick slick slick. the claim was filed late on a thursday afternoon and the replacement arrived on the friday morning.clear instructions the whole way and a very simple process",
                 "i never received the phone. you sent me a note last thursday that it was on its way. today is late tuesday night. still no phone. really frustrating.",
                 "absolutely disgusted with asurion - not trustworthy, no integrity i am completely disgusted with your company. a cell phone is an essential part of communication, and it is unacceptable for a simple glass replacement to take more than two weeks. from the first scheduled meeting to have the tech come to my home to repair (note that i had to reschedule appointments to be home), they canceled an hour after the scheduled arrival time. service truck was in the shop, multiple reschedule attempts - all failed to have the tech come to my home to fix the issue. five times after they were supposed to arrive, they cancelled! unacceptable. adam with ubreakifix. i finally caved and called at&t for assistance. they helped me get an appointment scheduled by contacting your company on my behalf... this time, there was no rescheduling; they simply did not show up, no call, no text.when i called, the asurion tech shipped the phone, promising that i would receive it the next day via fedex - lie, it arrived two days later. this has been the worst experience - your company's customer service is worse than comcast/xfinity's. satan trained ineffective employees. you're the worst!"]}
response = requests.post("http://localhost:8000//predictions", json=data)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)