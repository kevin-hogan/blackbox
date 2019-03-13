FROM python:3
ARG DEBIAN_FRONTEND=noninteractive
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb \
    > msfinstall \
    && chmod 755 msfinstall \
    && ./msfinstall
RUN apt-get update && apt-get install -y \
    sudo \
    xterm \
    mininet \
    snort \
    python-pip
RUN python -m pip install --no-cache \
    ptvsd \
    ryu
RUN python2 -m pip install --no-cache \
    requests
RUN touch /etc/network/interfaces