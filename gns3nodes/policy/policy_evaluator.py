import sys
import logging
from flask import Flask, request, render_template, json
app = Flask(__name__)
app.logger.setLevel(level=logging.INFO)

@app.route('/ids_alert', methods = ['GET'])
def config():
    #confJson = json.loads(json.dumps(request.json))
    print("Endpoint hit!")
    return ""
