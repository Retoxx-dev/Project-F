import requests

def post_send_email(email_recipient):
    requests.post(f"http://email_sender:8001/email/{email_recipient}", timeout=20)