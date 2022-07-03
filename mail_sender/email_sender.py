import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_sender_address = os.environ.get("EMAIL_SENDER_USERNAME")
email_sender_password = os.environ.get("EMAIL_SENDER_PASSWORD")
email_sender_server = os.environ.get("EMAIL_SENDER_SERVER")
email_sender_port = os.environ.get("EMAIL_SENDER_PORT")

def email_new(recipient: str):
    message = MIMEMultipart()
    message['Subject'] = "Your account has been created!"
    message['From'] = str(email_sender_address)
    message['To'] = recipient

    html = MIMEText("Your ServiceDesk account has been created!")
    message.attach(html)
    with smtplib.SMTP(email_sender_server, email_sender_port) as server:
        server.starttls()
        server.login(email_sender_address, email_sender_password)
        server.sendmail(email_sender_address, recipient, message.as_string())
    
        