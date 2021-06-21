FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN python -m pip install gunicorn flask python-dotenv pymongo dnspython

WORKDIR /app
COPY . /app

CMD exec gunicorn app:app --workers 1 --threads 8 --timeout 0 --bind :$PORT
