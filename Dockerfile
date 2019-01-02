FROM python:3
# Below is installing firefox (called iceweasel on Debian) for testing display
RUN apt-get update && apt-get install -y iceweasel
RUN pip install --no-cache ptvsd
