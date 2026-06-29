FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/ requirements/

RUN pip install --upgrade pip && \
    pip install -r requirements/prod.txt

COPY . .

RUN mkdir -p staticfiles media

EXPOSE 8000

ENTRYPOINT [ "docker/django/entrypoint.sh" ]
