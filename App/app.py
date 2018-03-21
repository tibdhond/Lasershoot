from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/lifeofpi")
def alive():
    return  render_template('lifeofpi.html',my_string="Alive in Tucson", my_list=[0,1,2])