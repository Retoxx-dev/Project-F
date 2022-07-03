import pika

def send_email(email_recipient):
    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port='5672', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='mail_sender')
    
    channel.basic_publish(exchange='', routing_key='mail_sender', body=email_recipient)
    connection.close()