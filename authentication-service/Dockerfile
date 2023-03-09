FROM python:slim-buster

WORKDIR /app

COPY config/requirements.txt .

RUN pip install -r requirements.txt

COPY . .