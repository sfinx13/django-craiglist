#syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system --group app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev python3-dev

WORKDIR $APP_HOME
COPY . $APP_HOME
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chown -R app:app $APP_HOME

USER app