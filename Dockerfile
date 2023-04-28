# Base image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Update package repository dan install dependensi yang dibutuhkan
RUN apt-get update && apt-get install -y python3-tk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app/ app/
COPY main.py .

# Set entrypoint command
CMD ["python", "main.py"]
