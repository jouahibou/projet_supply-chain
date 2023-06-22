import csv 
fields = [
    {"name": "titre", "type": "text"},
    {"name": "nom", "type": "text"},
    {"name": "stars", "type": "float"},
    {"name": "localisation", "type": "keyword"},
    {"name": "nb_reviews", "type": "integer"},
    {"name": "date_review", "type": "date"},
    {"name": "date_experience", "type": "date"},
    {"name": "comment", "type": "text"}
    
]

with open ("types.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([field["name"] for field in fields]) 
    writer.writerow([field["type"] for field in fields]) 
csvfile.close()     