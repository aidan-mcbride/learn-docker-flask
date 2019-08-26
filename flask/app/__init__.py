import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # get name stored as env var
    app_name = os.getenv("ENV_NAME")

    if app_name:
        return "Hello from {}".format(app_name)

    return "Hello Worlds"
