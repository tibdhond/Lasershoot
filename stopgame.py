import MySQLdb
import time
import datetime

db = MySQLdb.connect(host="dlw-hackathon.westeurope.cloudapp.azure.com", user="hackathon", passwd="Delaware.2011", db="hackathon")

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

    
cur.execute("select id,status from dlwhackathon.game order by timestamp desc")
row = cur.fetchone()

print "Recentste spel:", str(row[0]), str(row[1])

if int(row[1]) != 1:
    print "Er is geen spel bezig!"
else:
    try:
        id = int(row[0])
        cur.execute("UPDATE dlwhackathon.game SET status = '0' WHERE Id = %s", (id,))
        db.commit();
        print "spel", str(row[0]), "gestopt"
    except Exception as e:
        print "error: ", str(e)
        db.rollback()
    
cur.close()
db.close()