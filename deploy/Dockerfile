# NeuroSync AI Backend Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend ./backend
WORKDIR /app/backend

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 