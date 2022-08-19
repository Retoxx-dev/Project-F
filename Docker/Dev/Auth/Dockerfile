FROM python:3.10

WORKDIR /app

COPY ./Docker/Dev/Auth/requirements.txt .

RUN pip install -r requirements.txt 

COPY auth/ .

CMD uvicorn auth.main:app --host 0.0.0.0 --port 8002 --reload