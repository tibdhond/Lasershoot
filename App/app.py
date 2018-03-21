from flask import Flask, render_template
import random
app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"
@app.route("/<user>")
def show_stats(user):
    return render_template('test.html', user=user)