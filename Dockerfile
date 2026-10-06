FROM python:3.12-slim

WORKDIR /app

# Muestra la salida de print() en tiempo real
ENV PYTHONUNBUFFERED=1

COPY main.py .

CMD ["python", "main.py"]