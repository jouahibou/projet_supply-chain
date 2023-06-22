from fastapi import FastAPI
from typing import Dict, Any
from database import get_document, search_documents, add_document, update_document, delete_document

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

@app.get("/documents/{index}/_search")
async def search_documents(index: str, query: Dict[str, Any],es:Elasticsearch=Depends(get_es)):
    docs = search_documents(es,index, query)
    return docs

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