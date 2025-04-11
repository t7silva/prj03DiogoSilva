
FROM python:3.10-slim

# Instalar dependências do sistema para o OpenCV funcionar corretamente
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && pip install opencv-python pika redis numpy

WORKDIR /workspace

