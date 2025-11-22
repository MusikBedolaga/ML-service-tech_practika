from fastapi import APIRouter, HTTPException
from rq.job import Job
from app.schemas.text import (
    TextRequest,
    TextResponse,
    ModerateRequest,
    ModerateResponse,
    ModerateJobResponse,
)
from app.services.text_processor import process_text_service
from app.ml.model import predict_toxic
from app.core.rq_config import get_moderation_queue, get_redis

router = APIRouter()

@router.post("/process", response_model=TextResponse)
def process_text(data: TextRequest):
  return process_text_service(data.text)

@router.post("/moderate", response_model=ModerateResponse)
def moderate_text(data: ModerateRequest):
  result = predict_toxic(data.text)
  return ModerateResponse(**result)

@router.post("/moderate/async", response_model=ModerateJobResponse)
def moderate_text_async(data: ModerateRequest):
  queue = get_moderation_queue()
  job = queue.enqueue(
      "app.tasks.moderation.run_toxic_moderation",
      data.text,
      job_timeout=10,
  )
  
  return ModerateJobResponse(job_id=job.id)

@router.get("/moderate/result/{job_id}", response_model=ModerateResponse)
def get_moderation_result(job_id: str):
    redis_conn = get_redis()
    try:
        job = Job.fetch(job_id, connection=redis_conn)
    except Exception:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.is_failed:
        raise HTTPException(status_code=500, detail="Job failed")

    if job.result is None:
        raise HTTPException(status_code=202, detail="Result is not ready yet")

    return ModerateResponse(**job.result)