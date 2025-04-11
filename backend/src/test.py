from flask import Flask

#initiallizing flask

app = Flask(__name__)

@app.route("/")


def home():
    return "This is from flask frfrrrrrrr"

