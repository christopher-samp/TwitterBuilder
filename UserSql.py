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

def InsertIntoScheduledTweets(tweets):
  #tweets is a list of tweets
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd@1",
    database="testdatabase"
  )

  myCursor = db.cursor()
  threadOrder = 1
  for tweet in tweets:
    insertQuery = ('INSERT INTO ScheduledTweets '
                  '(userid, tweetcontent, timetosend, sent, done, tweettype, threadorderid) '
                  'VALUES '
                  '("%s","%s", "%s", "0", "0", "%s", "%s")' % (tweet.userid, tweet.data, tweet.date, tweet.tweetType, threadOrder))
    threadOrder = threadOrder+1

    myCursor.execute(insertQuery)
    db.commit()
  
  return True

def CheckForScheduledTweets(time):
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd@1",
    database="testdatabase"
  )

  myCursor = db.cursor()

  myCursor.execute("SELECT * FROM testdatabase.ScheduledTweets where timetosend = "+time)
  
  return myCursor.fetchall()
  

# CREATE TABLE ScheduledTweets (
#                                     id int unsigned NOT NULL AUTO_INCREMENT, 
#                                     userid bigint NOT NULL,
#                                     tweetcontent blob NOT NULL, 
#                                     timetosend datetime NOT NULL, 
#                                     sent tinyint(1) NOT NULL, 
#                                     timesent timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
#                                     done tinyint(1) NOT NULL, 
#                                     tweettype varchar(16) NOT NULL DEFAULT "tweet", 
#                                     threadorderid int NOT NULL DEFAULT 1,
#                                     PRIMARY KEY (id))