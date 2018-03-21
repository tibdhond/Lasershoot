import MySQLdb
import time
import datetime
import os
import subprocess

db = MySQLdb.connect(host="eu-cdbr-azure-west-b.cloudapp.net", user="b7f7d467f4d922", passwd="94f415a0", db="dlwhackathon")

#create a cursor for the select
cur = db.cursor()

gameRunning = False
proc = "" #notreally

while True:
    db = MySQLdb.connect(host="eu-cdbr-azure-west-b.cloudapp.net", user="b7f7d467f4d922", passwd="94f415a0", db="dlwhackathon")
    cur = db.cursor()
    
    
    cur.execute("select id,status from dlwhackathon.game order by timestamp desc")
    row = cur.fetchone()

    print "gepolld:", str(row[0]), str(row[1])

    if int(row[1]) != 1:
        print "Spel is niet bezig!"
        if gameRunning:
            gameRunning = False
            #TODO actually stop the game, how?
            #os.system("python theActualGame.py")
            proc.terminate()
            print "stopped game script"
    else:
        print "Spel is bezig!"
        if not gameRunning:
            gameRunning = True
            # TODO actually start the game
            #os.system("python theActualGame.py")
            proc = subprocess.Popen(
                "python theActualGame.py",
                stderr=subprocess.STDOUT,  # Merge stdout and stderr
                stdout=subprocess.PIPE,
                shell=True)
            print "started game script"
    
    
        
    cur.close()
    db.close()
    time.sleep(10)