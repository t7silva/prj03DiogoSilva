
import cv2
import base64
import redis
import os

def publish_image(image_path):
    image = cv2.imread(image_path)
    _, buffer = cv2.imencode('.jpg', image)
    encoded = base64.b64encode(buffer).decode('utf-8')

    r = redis.Redis(host='valkey', port=6379)
    r.publish('images', encoded)
    print("Imagem enviada para os subscribers via Redis.")

if __name__ == '__main__':
    image_path = os.path.join('..', '..', 'images', 'nature_01.jpg')
    publish_image(image_path)
