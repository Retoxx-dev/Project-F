import pika, time
import email_sender

time.sleep(20) #Sleep 10 sec, let the rabbitmq container get up and be ready to accept connections - to be prettified in the future

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port='5672', credentials=credentials))

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
