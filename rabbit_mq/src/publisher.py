
import cv2
import base64
import pika
import os

def publish_image(image_path):
    image = cv2.imread(image_path)
    _, buffer = cv2.imencode('.jpg', image)
    encoded = base64.b64encode(buffer).decode('utf-8')

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.exchange_declare(exchange='images', exchange_type='fanout')
    channel.basic_publish(exchange='images', routing_key='', body=encoded)
    print("Imagem enviada para os subscribers.")
    connection.close()

if __name__ == '__main__':
    image_path = os.path.join('..', '..', 'images', 'nature_01.jpg')
    publish_image(image_path)
