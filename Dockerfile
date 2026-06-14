FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

COPY . .

CMD [ "python", "app.py" ]