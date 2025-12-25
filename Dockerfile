FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install -e .
ENV PYTHONUNBUFFERED=1
CMD ["python", "scripts/train_model.py", "--data", "data/sample_sales_data.csv"]
