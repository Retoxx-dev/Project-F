import pika, time
import email_sender
import os

time.sleep(20) #Sleep 10 sec, let the rabbitmq container get up and be ready to accept connections - to be prettified in the future
rabbitmq_user = os.environ.get("RABBITMQ_DEFAULT_USER")
rabbitmq_password = os.environ.get("RABBITMQ_DEFAULT_PASS")
rabbitmq_host = os.environ.get("RABBITMQ_HOSTNAME")
rabbitmq_port = int(os.environ.get("RABBITMQ_PORT"))

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials))

channel = connection.channel()
channel.queue_declare(queue='mail_sender')

def callback(ch, method, properties, body):
    body = body.decode()
    print("Ready to receive messages")
    print(f"Received the email: {body}")
    print("Sending...")
    email_sender.email_new(recipient=body)
    print("Email has been sent")
    
channel.basic_consume(queue='mail_sender', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
