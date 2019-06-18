FROM python:3
RUN pip install Flask
RUN apt-get update && apt-get install -y net-tools
ADD avatar.py /src/avatar.py
ADD templates /src/templates
ADD startwebserver /src/startwebserver
CMD sh -c "(./src/startwebserver &) && bash"