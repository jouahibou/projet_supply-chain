from elasticsearch import Elasticsearch
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def import_data_from_es(host, index):
    
    es = Elasticsearch(hosts = [host])
    
    query = {
        "query": {
            "match_all": {}
        },
        "size": 1000  # Adjust batch size as per your requirements
    }
    scroll = es.search(index=index, body=query, scroll="5m")
    scroll_id = scroll["_scroll_id"]
    hits = scroll["hits"]["hits"]
    data = [hit["_source"] for hit in hits]

    while len(hits) > 0:
        scroll = es.scroll(scroll_id=scroll_id, scroll="5m")
        hits = scroll["hits"]["hits"]
        data.extend([hit["_source"] for hit in hits])
    df = pd.DataFrame(data)
    return df