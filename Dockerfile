FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root --no-dev

COPY . .