from app.ml.model import predict_toxic

def run_toxic_moderation(text: str, threshold: float = 0.5) -> dict:
  return predict_toxic(text, threshold = threshold)
