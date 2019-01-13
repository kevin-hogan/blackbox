FROM python:3
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    xterm \
    mininet \
    snort
RUN pip install --no-cache \
    ptvsd \
    ryu
RUN touch /etc/network/interfaces
