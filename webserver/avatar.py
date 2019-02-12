import sys
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/alerts', methods = ['POST'])
def hello():
    data = request.form
    print(str(data), file=sys.stderr)
    return "Alert Successful!"
