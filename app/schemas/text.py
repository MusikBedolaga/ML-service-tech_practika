from pydantic import BaseModel

class TextRequest(BaseModel):
  text: str
  
class TextResponse(BaseModel):
  original: str
  processed: str
  word_count: int
  
class ModerateRequest(BaseModel):
  text: str
  
class ModerateResponse(BaseModel):
  ban: bool
  score: float
  
class ModerateJobResponse(BaseModel):
    job_id: str