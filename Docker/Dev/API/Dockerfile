FROM python:3.10

WORKDIR /app

COPY ./Docker/Dev/API/requirements.txt .

RUN pip install -r requirements.txt 

COPY api/ .

CMD uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload