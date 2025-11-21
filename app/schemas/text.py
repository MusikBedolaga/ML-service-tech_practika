from pydantic import BaseModel

class TextRequest(BaseModel):
  text: str
  
class TextResponse(BaseModel):
  original: str
  processed: str
  word_count: int