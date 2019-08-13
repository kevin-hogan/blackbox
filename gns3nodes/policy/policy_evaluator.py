import sys
import logging
import requests
from string import Template
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.logger.setLevel(level=logging.INFO)

CONTROLLER_IP = "10.0.0.3"
CONTROLLER_FIREWALL_URI = Template("http://" + CONTROLLER_IP + ":8080/firewall/block/$block_ip")
PING_ALERT_MESSAGE = "ICMP PING"

@app.route('/ids_alert', methods = ['POST'])
def config():
    if PING_ALERT_MESSAGE in request.json["msg"]:
        print("Firewalling " + request.json["src"])
        requests.get(url = CONTROLLER_FIREWALL_URI.substitute(block_ip=request.json["src"]))
    return ""
