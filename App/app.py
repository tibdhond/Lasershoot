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

#tablename.query.watiknodigheb().all()
@app.route("/")
def hello():
    games = Game.query.all()
    return "Hello World!"

@app.route("/<gameid>")
def alive(gameid):
    scores_freddy = Scores.query.filter((Scores.game==gameid) and (Scores.idpi=="freddy")).all()
    scores_brico = Scores.query.filter((Scores.game==gameid) and (Scores.idpi=="brico")).all()
    scores_e17 = Scores.query.filter((Scores.game==gameid) and (Scores.idpi=="e17")).all()
    return  render_template('lifeofpi.html', score_freddy=len(scores_freddy), score_brico=len(scores_brico),
        score_e17=len(scores_e17))