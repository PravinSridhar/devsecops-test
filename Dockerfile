# base image
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN useradd -m myuser

# set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code (COPY SRC DEST)
COPY app/ ./app/

# ownership
RUN chown -R myuser:myuser /app

# switch to non-root user
USER myuser

# Expose service port
EXPOSE 8000

# Start fastapi
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]