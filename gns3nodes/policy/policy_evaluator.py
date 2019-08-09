import sys
import logging
import requests
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.logger.setLevel(level=logging.INFO)

CONTROLLER_IP = "10.0.0.3"
PING_ALERT_MESSAGE = "ICMP PING"

@app.route('/ids_alert', methods = ['POST'])
def config():
    if PING_ALERT_MESSAGE in request.json["msg"]:
        print("Firewalling " + request.json["src"])
        requests.get(url = "http://" + CONTROLLER_IP + ":8080/firewall/block/" + request.json["src"])
    return ""
