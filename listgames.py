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

cur.execute("SELECT * FROM dlwhackathon.game")
for row in cur.fetchall():
    print str(row[0]), str(row[1]), str(row[2]), str(row[3])
    
cur.close()
db.close()