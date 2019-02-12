from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("here!")
    return "Hello World!"