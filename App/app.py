from flask import Flask, render_template
import datetime

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

@app.route("/")
def hello():
    games = Game.query.all()
    return "Hello World!"

@app.route("/lifeofpi")
def alive():
    alive = False
    if(alive):
        return render_template('template.html', my_string="Foo", 
        my_list=[6,7,8,9,10,11], title="Alive!", current_time=datetime.datetime.now())
    else:
        return render_template('template.html', my_string="Foo", 
        my_list=[6,7,8,9,10,11], title="Dead!", current_time=datetime.datetime.now())

@app.route('/update')
def update():
    socketio.emit('new_score', "lol", broadcast=True)
    return "ok"

if __name__ == '__main__':
    socketio.run(app)
