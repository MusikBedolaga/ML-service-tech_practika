from fastapi import APIRouter
from app.schemas.text import (
    TextRequest,
    TextResponse,
    ModerateRequest,
    ModerateResponse,
)
from app.services.text_processor import process_text_service
from app.ml.model import predict_toxic

router = APIRouter()

@router.post("/process", response_model=TextResponse)
def process_text(data: TextRequest):
  return process_text_service(data.text)

@router.post("/moderate", response_model=ModerateResponse)
def moderate_text(data: ModerateRequest):
  result = predict_toxic(data.text)
  return ModerateResponse(**result)