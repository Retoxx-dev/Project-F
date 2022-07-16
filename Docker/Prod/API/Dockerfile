FROM python:3.10 AS build

#Setup virtual environment
WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

#Install libraries/dependencies
COPY ./Docker/Prod/API/requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.10 AS build-image

WORKDIR /usr/app
COPY --from=build /usr/app/venv ./venv

#Create non-root user
RUN useradd --create-home appuser
USER appuser

#Copy api files
WORKDIR /home/appuser
COPY api/ ./api

#Check if venv path is usable
ENV PATH="/usr/app/venv/bin:$PATH"

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]