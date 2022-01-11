import mysql.connector

def AddWatchListConnection(watchListUserId, userId):
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd@1",
    database="testdatabase"
  )

  myCursor = db.cursor()
  #print("insert into testdatabase.WatchList values("+watchListUserId+", "+userId+")")
  myCursor.execute("insert into testdatabase.WatchList (WatchListUserId, UserId) values("+watchListUserId+", "+userId+")")
  db.commit()
  print(myCursor.execute("select * from testdatabase.WatchList"))
  return True

