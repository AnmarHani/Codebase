FROM python:slim

WORKDIR /app

COPY config/requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .