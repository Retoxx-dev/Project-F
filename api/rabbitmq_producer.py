import pika
import os

rabbitmq_user = os.environ.get("RABBITMQ_DEFAULT_USER")
rabbitmq_password = os.environ.get("RABBITMQ_DEFAULT_PASS")
rabbitmq_host = os.environ.get("RABBITMQ_HOSTNAME")
rabbitmq_port = os.environ.get("RABBITMQ_PORT")


def send_email(email_recipient):
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='mail_sender')
    
    channel.basic_publish(exchange='', routing_key='mail_sender', body=email_recipient)
    connection.close()