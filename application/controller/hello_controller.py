from application import app
from flask import render_template

@app.route("/")
def hello():
    return render_template("index.html")
