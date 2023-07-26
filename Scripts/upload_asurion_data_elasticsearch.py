from elasticsearch import Elasticsearch, helpers
import csv

# Créer une instance de connexion Elasticsearch
es = Elasticsearch(hosts = "http://@localhost:9200")


# Définir le nom de l'index
index_name = "asurion"

# Définir les paramètres de mapping et de settings
settings = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 2
    },
    "mappings": {
        "properties": {
            "comment": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "date_experience": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "date_review": {
                "type": "date"
            },
            "localisation": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "nb_reviews": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "nom": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "stars": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "titre": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            }
        }
    }
}

# Créer l'index avec les paramètres spécifiés
es.indices.create(index=index_name, body=settings)

# Importer des données à partir d'un fichier CSV
with open('/home/ubuntu/projet_supply-chain/Data/asurion_complete.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    # Préparer les données pour l'importation en utilisant la méthode helpers.bulk
    actions = [
        {
            "_index": index_name,
            "_source": row
        }
        for row in reader
    ]

    # Importer les données à l'aide de la méthode helpers.bulk
    helpers.bulk(es, actions)