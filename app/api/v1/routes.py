from fastapi import APIRouter
from app.schemas.text import TextRequest, TextResponse
from app.services.text_processor import process_text_service

router = APIRouter()

@router.post("/process", response_model=TextResponse)
def process_text(data: TextRequest):
  return process_text_service(data.text)