FROM python:3
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y snort
ADD blackbox.rules /etc/snort/rules/blackbox.rules
ADD snort.conf /etc/snort/snort.conf
