FROM python:3.12

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /src

CMD unicorn main:app --bind=0.0.0.0:8000
