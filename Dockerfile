FROM python:3
RUN apt-get update && apt-get install -y x11-apps mininet
RUN pip install --no-cache ptvsd
