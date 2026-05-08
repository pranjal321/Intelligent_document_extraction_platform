
import os
from fastapi import APIRouter, UploadFile, File
from app.services.extraction_service import ExtractionService
from app.database.db import SessionLocal, Base, engine
from app.database.models import ExtractedDocument

Base.metadata.create_all(bind=engine)

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/extract")
async def extract_document(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    data = ExtractionService.process_document(file_path)

    session = SessionLocal()

    record = ExtractedDocument(
        document_type=data["document_type"],
        extracted_data=data
    )

    session.add(record)
    session.commit()

    return {
        "success": True,
        "data": data
    }
