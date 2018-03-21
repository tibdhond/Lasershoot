import MySQLdb
import time
import datetime

db = MySQLdb.connect(host="eu-cdbr-azure-west-b.cloudapp.net", user="b7f7d467f4d922", passwd="94f415a0", db="dlwhackathon")

#create a cursor for the select
cur = db.cursor()

# db scheme
# Game
#       Id
#       gamemode
#       timestamp
#       status 
# GameModes
#       id
#       name
# Scores
#       id
#       game
#       timestamp
#       idpi


cur.execute("select id from dlwhackathon.game order by timestamp desc")
row = cur.fetchone()
newId = int(row[0]) + 1

try:
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("""INSERT INTO dlwhackathon.game (id, gamemode, timestamp, status) VALUES (%s, %s, %s, %s)""", (newId, 'capture_the_flag', timestamp, '1')) 
    db.commit()
except Exception as e:
    print "error: ", str(e)
    db.rollback()
    
cur.close()
db.close()