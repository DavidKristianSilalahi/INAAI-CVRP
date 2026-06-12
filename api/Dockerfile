# api/Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy file konfigurasi dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code project
COPY src/ ./src/
COPY api/ ./api/

EXPOSE 8000

CMD ["uvicorn", "api.app.py:app", "--host", "0.0.0.0", "--port", "8000"]