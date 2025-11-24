from pathlib import Path
from functools import lru_cache

import joblib

# Путь к сохранённой модели (тот же, куда сохраняет train_toxic_model.py)
MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "toxic_model.joblib"


@lru_cache
def get_model():
    """
    Лениво загружает модель из файла и кэширует её.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Модель не была найдена по пути: {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    return model


def predict_toxic(text: str, threshold: float = 0.35) -> dict:
    """
    Делает предсказание токсичности для одного текста.
    Возвращает словарь с полями:
      - score: вероятность токсичности (класс 1)
      - ban: True/False в зависимости от порога
    """
    model = get_model()

    # model — это Pipeline(TfidfVectorizer -> классификатор), у него есть predict_proba
    proba = model.predict_proba([text])[0][1]
    ban = proba >= threshold

    return {
        "score": float(proba),
        "ban": bool(ban),
    }
