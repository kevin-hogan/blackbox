FROM python:3
RUN pip install Flask requests
RUN apt-get update && apt-get install -y net-tools
ADD policy_evaluator.py /src/policy_evaluator.py
ADD startpolicy /src/startpolicy
