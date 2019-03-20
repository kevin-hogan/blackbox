FROM python:3
RUN pip install Flask
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y \
    sudo \
    libc6:i386 \
    libncurses5:i386 \
    libstdc++6:i386 \
    libc6-dev-i386
RUN pip install pexpect
ENV PATH="/src/reconfig/bin:${PATH}"
