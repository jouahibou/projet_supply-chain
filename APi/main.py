from fastapi import FastAPI
from typing import Dict, Any
<<<<<<< HEAD
from database import get_document, search_documents, add_document, update_document, delete_document,cleaner_rev,delete_punctiation,truncate_text_column
from fastapi import Depends
from elasticsearch import Elasticsearch
import pandas as pd
import warnings
import joblib
import logging

import warnings
=======
from database import get_document,cleaner_rev, add_document, update_document, delete_document
from fastapi import Depends
from elasticsearch import Elasticsearch
import joblib
import logging
import pandas as pd

import warnings

import logging
import warnings
>>>>>>> seydina_deve
warnings.filterwarnings("ignore")
import joblib
import re
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
<<<<<<< HEAD
stop_words = set(stopwords.words('english'))
=======
>>>>>>> seydina_deve

app = FastAPI()




@app.get('/')
def get_index():
    return {
        'data': 'Bienvenue'
        }

@app.get("/documents/{index}")
async def read_document(index: str):
    doc = get_document(index)
    if doc is None:
        return {"error": "Document not found"}
    return doc


@app.post("/documents/{index}")
async def create_document(index: str, document: Dict[str, Any]):
    success = add_document(index, document)
    if success:
        return {"success": True}
    return {"error": "Failed to create document"}

@app.put("/documents/{index}/{id}")
async def update_document(index: str, id: str, document: Dict[str, Any]):
    success = update_document(index, id, document)
    if success:
        return {"success": True}
    return {"error": "Failed to update document"}

@app.delete("/documents/{index}/{id}")
async def delete_document(index: str, id: str):
    success = delete_document(index, id)
    if success:
        return {"success": True}
    return {"error": "Failed to delete document"}

@app.get("/data_prediction_new_comment", 
        description ="Donne une prédiction de la note /5 qu'un client peut mettre.",
        tags=["Prediction"])
async def data_prediction_new_comment(review: str):  
    try:
        with open("mnb_final_model.joblib", "rb") as f:
            ml_model = joblib.load(f)
        review_clean = cleaner_rev(review)    
        df=pd.DataFrame(pd.Series(review_clean, name="text"))
        result = ml_model.predict(df["text"])
        return {
                "predicted_star_comment": int(result)
            }
    except Exception as e:
        logging.error(f"Error: {e}")
        return {
            "error": "An error occurred while predicting the star rating"
        }
    