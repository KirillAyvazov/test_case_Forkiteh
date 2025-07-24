FROM python:3.11

RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
