FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . .
