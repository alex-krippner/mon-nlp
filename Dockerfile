FROM python:3.11.3-slim

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download ja_core_news_sm

COPY app.py app.py
