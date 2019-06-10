FROM python:3
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    sudo \
    xterm \
    mininet \
    python-pip
RUN python -m pip install --no-cache \
    ptvsd \
    ryu
RUN python2 -m pip install --no-cache \
    requests
RUN touch /etc/network/interfaces
ADD snort_learning_switch.py /src/snort_learning_switch.py
ADD startcontroller /src/startcontroller