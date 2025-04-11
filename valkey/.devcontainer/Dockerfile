
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    python3-opencv \
    libgl1-mesa-glx \
    && pip install pika redis numpy

WORKDIR /workspace
