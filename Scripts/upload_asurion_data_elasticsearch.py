#! /usr/bin/python
from elasticsearch import Elasticsearch, helpers
import csv

es = Elasticsearch(hosts = "http://@localhost:9200")


with open('/home/ubuntu/projet_supply-chain/Data/asurion_complete.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='asurion')
