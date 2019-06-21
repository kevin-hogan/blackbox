import sys
import logging
import requests
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.logger.setLevel(level=logging.INFO)

CONTROLLER_IP = "10.0.0.3"

@app.route('/ids_alert', methods = ['GET'])
def config():
    #confJson = json.loads(json.dumps(request.json))
    print("Endpoint hit!")
    requests.get(url = "http://" + CONTROLLER_IP + ":8080/firewall/block/192.168.0.5")
    return ""
