import MySQLdb

db = MySQLdb.connect(host="eu-cdbr-azure-west-b.cloudapp.net", user="b7f7d467f4d922", passwd="94f415a0", db="dlwhackathon")

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