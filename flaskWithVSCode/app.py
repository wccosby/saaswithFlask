import re
from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "hello flask from vscode"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y, at %X")

    # filter name to only letters, url arguments can contain arbitrary text so we restrict
    # to safe characters only
    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    
    return render_template("hello_there.html",
                            title="Hello, Flask",
                            name=clean_name,
                            formatted_time=formatted_now)


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

