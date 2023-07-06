from fastapi import FastAPI
from typing import Dict, Any
from database import get_document, search_documents, add_document, update_document, delete_document,text_cleaner,delete_punctiation,truncate_text_column
from fastapi import Depends
from elasticsearch import Elasticsearch
import pandas as pd
import warnings
import joblib
app = FastAPI()

@app.get('/')
def get_index():
    return {
        'data': 'Bienvenue'
        }

@app.get("/documents/{index}/{id}")
async def read_document(index: str, id: str):
    doc = get_document(index, id)
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

@app.post("/predictions")
async def predict(data: Dict[str, str]):
    warnings.filterwarnings('ignore')
    
    clf_final = joblib.load('mnb_final_model.joblib')
    
    df = pd.DataFrame(data, columns=['text'])

    text_cleaner("text")
    delete_punctiation(df, "text")
    truncate_text_column(df, 'text')

    result = clf_final.predict(df["text"])
        # Return the prediction result as a JSON object
    return {"result": result}