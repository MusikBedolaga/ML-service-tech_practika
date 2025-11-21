def process_text_service(text: str):
  processed = text.lower()
  word_count = len(text.split())
  
  return {
    "original": text,
    "processed": processed,
    "word_count": word_count
  }