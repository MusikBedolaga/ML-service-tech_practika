# ML Text Service (FastAPI)

Небольшой сервис на FastAPI для обработки текста.  
Сейчас выполняет базовые операции (преобразование строки), в будущем планируется подключение ML-моделей.

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
