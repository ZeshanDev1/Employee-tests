FROM selenium/standalone-chrome:latest

USER root

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY test_employees.py .

CMD ["python", "test_employees.py"]
