FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y chromium-driver chromium wget unzip curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test script
COPY test_employees.py .

# Default command
CMD ["python3", "test_employees.py"]
