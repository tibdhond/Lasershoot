import MySQLdb

db = MySQLdb.connect(host="dlw-hackathon.westeurope.cloudapp.azure.com", user="hackathon", passwd="Delaware.2011", db="hackathon")

#create a cursor for the select
cur = db.cursor()

#Get rows
cur.execute("SELECT * FROM dlwhackathon.gamemodes")

# loop to iterate
for row in cur.fetchall() :
      #data from rows
      id = str(row[0])
      name = str(row[1])

      #print it
      print "The ID is: " + id
      print "The game mode is: " + name
	  
# INSERT ROW
#Sample insert query
try:
    cur.execute("INSERT INTO dlwhackathon.gamemodes (id, name) VALUES ('5', 'test3')") 
    db.commit()
except:
    db.rollback()
	
cur.close()
db.close()