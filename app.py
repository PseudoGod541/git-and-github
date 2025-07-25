from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/hi")
def hi():
    return "Hi"