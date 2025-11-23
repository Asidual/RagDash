from fastapi import APIRouter, UploadFile
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/v1/ingestion", tags=["Ingestion"])




#API INGESTION ROUTES
class DocumentUploadResponse(BaseModel):
    ingestion_id: str
    recived_files: List[str]

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_documents(project_id: str, files: List[UploadFile]):
    pass
    # Logica per l'upload del file



class IngestionResponse(BaseModel):
    status: str

@router.post("/process/{ingestion_id}")
async def ingest_documents(ingestion_id: str):
    pass
    # Logica per l'ingestione dei documenti



#API CHECK DOCUMENT IN DB
@router.get("/check_docs")
async def check_documents():
    pass
    # Logica per controllare i documenti nel database

#API DELETE ALL DOCUMENTS
@router.delete("/delete_docs")
async def delete_documents():
    pass
    # Logica per eliminare tutti i documenti dal database

#API LIST ALL DOCUMENTS
@router.get("/list_docs")
async def list_documents():
    pass
    # Logica per elencare tutti i documenti nel database

#API INFO DOCUMENT BY ID
@router.get("/doc_info/{doc_id}")
async def document_info(doc_id: str):
    pass
    # Logica per ottenere informazioni su un documento specifico tramite ID