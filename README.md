# ML Text Service (FastAPI)

Небольшой сервис на FastAPI для обработки текста.  
Сейчас выполняет базовые операции (преобразование строки), в будущем планируется подключение ML-моделей.

## Запуск модели

Настроено виртуальное окружение.

Создаём виртуальное окружение:
python -m venv venv

Разрешаем запуск скриптов:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Активация окружения:
PS C:\...\ML-service-tech_practika> . .\venv\Scripts\Activate.ps1

После того как убедились, что окружение настроено выполняем след команды:
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

запускаем файл train_toxic_model.py
python

Модель
LogisticRegression	быстрая, легко интерпретировать	хуже работает на агрессивных текстах
LinearSVC (SVM)	лучше разделяет токсичный / нетоксичный текст, устойчив к шуму	не умеет predict_proba
CalibratedClassifierCV(SVM)	 Точность SVM + выдаёт вероятности	чуть медленнее

## Стек

- Python 3.13
- FastAPI
- Uvicorn

## Структура проекта

```text
app/
  api/
    v1/
      routes.py        # HTTP-роуты (контроллеры)
  schemas/
    text.py            # Pydantic-схемы запросов/ответов
  services/
    text_processor.py  # Бизнес-логика обработки текста
main.py                # Точка входа приложения

