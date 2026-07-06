from fastapi import APIRouter, UploadFile, File
from backend.services.contract_parser import extract_text

router = APIRouter()

@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)

    return {
        "filename": file.filename,
        "extracted_text": text[:1000]  # preview
    }
