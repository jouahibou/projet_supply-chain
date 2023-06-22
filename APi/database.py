from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

es= Elasticsearch(hosts = "http://@localhost:9200")


def get_document(index:str,id:str):
    """ index : le nom de l'index dans elasticsearch
    id l'identification unique du document elasticsearch 
    que l'on souhaite recupérer """
    try:
        res = es.get(index=index,id=id)
        return res['_source']
    except NotFoundError:
        return None


def search_documents(es:Elasticsearch,index: str,query :dict):
    """ index le nom de l'index dans elasticsearch
    query le corps de la requéte elasticsearch pour rechercher un 
    document """
    res = es.search(index=index,body=query)
    return [hit['_source'] for hit in res['hits']['hits']]

def add_document(index:str,document:dict):
    """ index le nom de l'index dans elasticsearch
        document qu'on souhaite ajouter"""
    res = es.index(index=index,body=document)
    return res['result'] == 'created'

def update_document(index: str, id: str, document: dict):
    """index : le nom de l'index dans Elasticsearch.
id : l'identifiant unique du document Elasticsearch que vous souhaitez mettre à jour.
document : le document mis à jour que vous souhaitez ajouter à Elasticsearch."""
    res = es.update(index=index, id=id, body={"doc": document})
    return res['result'] == 'updated'

def delete_document(index: str, id: str):
    """ index : le nom de l'index dans Elasticsearch.
      l'identifiant unique du document Elasticsearch que vous souhaitez supprimer.
    """
    res = es.delete(index=index, id=id)
    return res['result'] == 'deleted'




