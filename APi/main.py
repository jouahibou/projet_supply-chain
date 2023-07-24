from fastapi import FastAPI
from database import get_document,cleaner_rev, add_document, update_document, delete_document
from fastapi import Depends
import joblib
import logging
import pandas as pd
import warnings




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
    