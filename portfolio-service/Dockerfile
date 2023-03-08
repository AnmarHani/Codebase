FROM python:3.12.0a5-slim-bullseye

WORKDIR /app

COPY config/requirements.txt .

RUN pip install -r requirements.txt

COPY . .