import time
import sys
import logging
import requests
from collections import deque, defaultdict
from string import Template
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.logger.setLevel(level=logging.INFO)

CONTROLLER_IP = "10.0.0.3"
CONTROLLER_FIREWALL_URI = Template("http://" + CONTROLLER_IP + ":8080/firewall/block/$block_ip")
# requests.get(url = CONTROLLER_FIREWALL_URI.substitute(block_ip=request.json["src"]))

class AlertCounter:
    def __init__(self, alert_message, count_threshold, time_window_s, to_trigger):
        self.alert_message = alert_message
        self.count_threshold = count_threshold
        self.time_window_s = time_window_s
        self.to_trigger = to_trigger
        self.alert_timestamps = defaultdict(deque)

    def alert(self, alert):
        ts_for_source = self.alert_timestamps[alert["src"]]
        while ts_for_source and (time.time() - ts_for_source[-1]) > self.time_window_s:
            ts_for_source.pop()

        if alert["msg"] == self.alert_message:
            ts_for_source.appendleft(alert["ts"])
        
        if len(ts_for_source) > self.count_threshold:
            self.to_trigger(alert["src"])
            ts_for_source.clear()

icmp_counter = AlertCounter("ICMP PING", 3, 5, lambda src: print("Firewalling " + src))

@app.route('/ids_alert', methods = ['POST'])
def config():
    request.json.update({"ts": time.time()})
    icmp_counter.alert(request.json)
    return ""