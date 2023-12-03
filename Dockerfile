FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:5000 app:app

