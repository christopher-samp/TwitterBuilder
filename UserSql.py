import mysql.connector

def AddWatchListConnection(watchListUserId, userId):
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd@1",
    database="testdatabase"
  )

  myCursor = db.cursor()
  myCursor.execute("insert into testdatabase.WatchList (WatchListUserId, UserId) values("+watchListUserId+", "+userId+")")
  db.commit()
  return True

def RemoveFromWatchListConnection(watchListUserId, userId):
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd@1",
    database="testdatabase"
  )

  myCursor = db.cursor()
  myCursor.execute("delete from testdatabase.WatchList where WatchListUserId="+watchListUserId+" AND UserId="+userId)
  db.commit()
  return True

def GetWatchListConnections(userId):
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd@1",
    database="testdatabase"
  )

  myCursor = db.cursor()
  myCursor.execute("SELECT WatchListUserId FROM testdatabase.WatchList where UserId = "+userId)
  
  return myCursor.fetchall()

