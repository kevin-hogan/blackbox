FROM python:3
ARG DEBIAN_FRONTEND=noninteractive
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb \
    > msfinstall \
    && chmod 755 msfinstall \
    && ./msfinstall
RUN apt-get update && apt install -y \
    sudo \
    net-tools \
    nmap \
    mininet \
    openvswitch-testcontroller
RUN sudo ln /usr/bin/ovs-testcontroller /usr/bin/ovs-controller 
COPY src /src