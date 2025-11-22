from pathlib import Path
from functools import lru_cache

import joblib

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "toxic_model.joblib"

# Загрузска модели 
@lru_cache
def get_model():
  if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Модель не была найдена по пути: {MODEL_PATH}")
  model = joblib.load(MODEL_PATH)
  return model

# Предикт модели
"""
    Делает предсказание токсичности для одного текста.
    Возвращает словарь с полями:
      - score: вероятность токсичности (класс 1)
      - ban: True/False в зависимости от порога
"""
def predict_toxic(text: str, threshold: float = 0.5) -> dict:
  model = get_model()
  
  proba = model.predict_proba([text])[0][1]
  ban = proba >= threshold
  
  return {
    "score": float(proba),
    "ban": bool(ban),
  }