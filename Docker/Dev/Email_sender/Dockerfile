FROM python:3.10

WORKDIR /app

COPY ./Docker/Dev/Email_sender/requirements.txt .

RUN pip install -r requirements.txt

COPY mail_sender/ .

CMD ["python", "-u", "mail_sender/main.py"]