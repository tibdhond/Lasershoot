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

cur.execute("SELECT * FROM dlwhackathon.game")
for row in cur.fetchall():
    print str(row[0]), str(row[1]), str(row[2]), str(row[3])
    
cur.close()
db.close()