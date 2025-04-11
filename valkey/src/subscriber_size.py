
import redis
import base64
import cv2
import numpy as np

def process_image(msg):
    decoded = base64.b64decode(msg['data'])
    nparr = np.frombuffer(decoded, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(f"Resolução da imagem: {img.shape[1]}x{img.shape[0]}")

r = redis.Redis(host='valkey', port=6379)
pubsub = r.pubsub()
pubsub.subscribe(**{'images': process_image})
print("A aguardar imagem para calcular a resolução via Redis...")
pubsub.run_in_thread(sleep_time=1)
