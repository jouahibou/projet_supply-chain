from elasticsearch import Elasticsearch,helpers
import csv 
import json

import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)


with open('types.csv') as f : 
    types = f.readline().strip().split(',')
    field_types = f.readline().strip().split(',')

es= Elasticsearch(hosts = "http://@localhost:9200")

# Mapping pour l'index asurion 

mapping ={
    "mappings" : {
        "properties":{
            types[i]:{'type':field_types[i]} for i in range(len(types))
        }
    }
}

#es.indices.create(index="asurion2", body = mapping)


with open('asurion_preprocess.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='asurion')
    
query = {
  "query": {
    "match_all": {}
  }   
    }    


response = es.search(index="asurion", body=query)  


print(response)