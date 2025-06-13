FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev ffmpeg && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN ls -l /app
RUN ls -l /app/backend

EXPOSE 7860

CMD ["python", "/app/Frontend/app_interface.py"]