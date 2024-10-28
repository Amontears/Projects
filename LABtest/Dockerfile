# Используем базовый образ с Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем зависимости
RUN poetry install --no-root

# Копируем весь проект
COPY . /app/

# Запускаем приложение
CMD ["python", "main.py"]




