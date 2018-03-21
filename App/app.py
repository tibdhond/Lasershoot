from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('config.Configuration')
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

db.reflect() # reflection to get table meta

class Game(db.Model):
    __tablename__ = 'game'

class GameModes(db.Model):
    __tablename__ = 'gamemodes'

class Scores(db.Model):
    __tablename__ = 'scores'


@app.route("/")
def hello():
    games = Game.query.all()
    0/0
    return "Hello World!"

@app.route("/lifeofpi")
def alive():
    return  render_template('lifeofpi.html',my_string="Alive in Tucson", my_list=[0,1,2])