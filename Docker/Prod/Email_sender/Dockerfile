FROM python:3.10 AS build

#Setup virtual environment
WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

#Install libraries/dependencies
COPY ./Docker/Prod/Email_sender/requirements.txt .
RUN pip install -r requirements.txt



FROM python:3.10-slim AS build-image

WORKDIR /usr/app
COPY --from=build /usr/app/venv ./venv

#Create non-root user
RUN useradd --create-home appuser
USER appuser

#Copy email_sender files
WORKDIR /home/appuser
COPY mail_sender/ ./mail_sender

#Check if venv path is usable
ENV PATH="/usr/app/venv/bin:$PATH"

CMD ["python", "-u", "mail_sender/main.py"]