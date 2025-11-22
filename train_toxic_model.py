import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
from pathlib import Path

DATA_PATH = Path("data/labeled.csv")

TEXT_COL = "comment"
LABEL_COL = "toxic"

MODEL_PATH = Path("models/toxic_model.joblib")

# Подготовка данных
def load_data():
  df = pd.read_csv(DATA_PATH)
  print("Данные в датасете: ")
  print(df.head())
  
  X = df[TEXT_COL].astype(str)
  Y = df[LABEL_COL].astype(int)
  
  return X, Y

# Обучение данных
def train():
  X, Y = load_data()
  
  X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
  )
  
  # Пайплайн: TF-IDF -> логистическая регрессия
  pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
      max_features=50000,
      ngram_range=(1, 2)
    )),
    ("clf", LogisticRegression(
      max_iter=1000,
      n_jobs=-1
    ))
  ])
  
  pipeline.fit(X_train, Y_train)
  
  # Оценка
  Y_pred = pipeline.predict(X_test)
  print("Отчёт по качеству:")
  print(classification_report(Y_test, Y_pred))
  
  # Сохранение модели
  MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
  joblib.dump(pipeline, MODEL_PATH)
  print(f"Модель сохранена в: {MODEL_PATH.absolute()}")
  
if __name__ == "__main__":
    train()