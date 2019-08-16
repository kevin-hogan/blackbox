import time
import sys
import logging
import requests
from policies import AlertCounter
from countermeasures import FirewallSourceOfAlert
from flask import Flask, request, render_template, json
app = Flask(__name__)

policies = [
    AlertCounter("ICMP PING", 3, 5, FirewallSourceOfAlert())
]

@app.route('/ids_alert', methods = ['POST'])
def config():
    request.json.update({"ts": time.time()})
    [p.process_event(request.json) for p in policies]
    return ""
