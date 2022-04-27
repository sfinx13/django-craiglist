#syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye
# Python won’t try to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE=1
# Force the stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev python3-dev
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt