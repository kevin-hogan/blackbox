import sys
import logging
from flask import Flask, request, render_template, json
app = Flask(__name__)

homepage = "index.html"
confJson = None
app.logger.setLevel(level=logging.INFO)

@app.route('/config', methods = ['POST'])
def config():
    global confJson
    confJson = json.loads(json.dumps(request.json))
    return ""

@app.route('/alerts', methods = ['POST'])
def alerts():
    data = request.form
    message = data.get("alert")
    countermeasures = []
    if confJson:
        for cm in confJson["countermeasures"]:
            for alert in cm["response_to_alerts"]:
                if alert == message:
                    countermeasures.append(cm)
    
    for cm in countermeasures:
        if cm["name"] == "swap_homepage":
            app.logger.info("Swapping homepage!")
            global homepage
            homepage = "alternate_index.html"
    return ""

@app.route('/')
def get_homepage():
    return render_template(homepage)
