from flask import Flask, render_template

import datetime, threading, time, random

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

    
@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter
from flask_socketio import SocketIO, send, emit
socketio = SocketIO(app)

#tablename.query.watiknodigheb().all()
@app.route("/")
def hello():
    games = Game.query.all()
    return render_template("index.html", games=games)

@app.route("/showscore/<gameid>")
def showscore(gameid):
    scores_freddy = Scores.query.filter((Scores.game==gameid) & (Scores.idpi=="freddy")).all()
    scores_brico = Scores.query.filter((Scores.game==gameid) & (Scores.idpi=="brico")).all()
    scores_e17 = Scores.query.filter((Scores.game==gameid) & (Scores.idpi=="e17")).all()

    return render_template('score.html', score_freddy=len(scores_freddy), score_brico=len(scores_brico),
        score_e17=len(scores_e17))

def pi_alive(name):
    return bool(random.getrandbits(1))

def pis():
    pi = ['freddy', 'brico', 'e17']
    alives = {}
    for p in pi:
        alives[p] = pi_alive(p)

    return alives

@app.route("/pi/<string:name>")
def alive(name):
    alive = pi_alive(name)
    return render_template('template.html', current_pi=name,
                           status=alive, current_time=datetime.datetime.now())

@app.route('/update')
def update():

    socketio.emit('new_status', pis())
    return "ok"

if __name__ == '__main__':
    socketio.run(app)
