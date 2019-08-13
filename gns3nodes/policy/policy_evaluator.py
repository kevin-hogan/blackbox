import sys
import logging
import requests
from collections import deque
from string import Template
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.logger.setLevel(level=logging.INFO)

CONTROLLER_IP = "10.0.0.3"
CONTROLLER_FIREWALL_URI = Template("http://" + CONTROLLER_IP + ":8080/firewall/block/$block_ip")
PING_ALERT_MESSAGE = "ICMP PING"
alert_deque = deque()

def count_rule(alert_deque):
    filtered_deque = [a for a in alert_deque if PING_ALERT_MESSAGE in a["msg"]]
    if len(filtered_deque) > 3:
        print("Firewalling " + request.json["src"])
        # requests.get(url = CONTROLLER_FIREWALL_URI.substitute(block_ip=request.json["src"]))

@app.route('/ids_alert', methods = ['POST'])
def config():
    global alert_deque
    alert_deque.append(request.json)
    count_rule(alert_deque)
    return ""