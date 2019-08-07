FROM python:3
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y snort
RUN pip install snortunsock requests
ADD blackbox.rules /etc/snort/rules/blackbox.rules
ADD snort.conf /etc/snort/snort.conf
ADD src /src
