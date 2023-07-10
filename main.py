from flask import Flask, render_template, request, jsonify, Blueprint
from flask_cors import CORS

import os
import sys

from models import model
from settings import DSN, USN, PWD

app = Flask(__name__, static_folder="./build/static", template_folder="./build/templates/")
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000, threaded=True)
