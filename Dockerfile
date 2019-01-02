FROM python:3
RUN apt-get update && apt-get install -y \
    xterm \
    mininet
RUN pip install --no-cache \
    ptvsd \
    ryu
