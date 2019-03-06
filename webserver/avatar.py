import sys
from flask import Flask, request, render_template
app = Flask(__name__)

homepage = "index.html"

@app.route('/alerts', methods = ['POST'])
def alerts():
    data = request.form
    message = data.get("alert")
    if message == "ssh_attempt":
        global homepage
        homepage = "alternate_index.html"
    elif message == "ICMP":
        # TODO Add countermeasure for ICMP packet alert
        pass
    return ""

@app.route('/')
def get_homepage():
    return render_template(homepage)
