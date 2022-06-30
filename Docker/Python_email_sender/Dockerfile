FROM python:3.10

WORKDIR /app

COPY ./Docker/Python_email_sender/requirements.txt .

RUN pip install -r requirements.txt

COPY mail_sender_api/ .

EXPOSE 8001

CMD uvicorn mail_sender_api.main:app --host 0.0.0.0 --port 8001 --reload