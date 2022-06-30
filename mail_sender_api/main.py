from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from . import email_sender

app = FastAPI()

origins = [
    "http://localhost:80/",
    "http://localhost:82/",
    "http://localhost/",
    "http://api:80/",
    "http://api"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/email/{emailaddress}")
def send_email(emailaddress:str):
    return email_sender.email_new(recipient=emailaddress)