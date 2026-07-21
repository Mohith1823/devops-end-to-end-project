FROM python:3.11-slim

LABEL maintainer="Mohith"
LABEL project="DevOps End-to-End Project"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
