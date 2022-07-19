# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
RUN apt update \
    && apt install -y build-essential gcc python3-dev musl-dev \
    && apt install -y postgresql
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 manage.py migrate
CMD gunicorn ./oc_lettings_site/wsgi:application --bind 0.0.0.0:$PORT
