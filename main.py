from flask import Flask as fl

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, cum</p>"