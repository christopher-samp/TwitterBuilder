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

def GetScheduledTweets(userId):
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd@1",
    database="testdatabase"
  )

  myCursor = db.cursor()
  myCursor.execute("SELECT * FROM testdatabase.ScheduledTweets where UserId = "+userId+" AND sent=0")
  
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
  for tweet in tweets:
    print(tweet)
    insertQuery = ('INSERT INTO ScheduledTweets '
                  '(userid, tweetcontent, timetosend, sent, done, tweettype, threadorderid) '
                  'VALUES '
                  '("%s","%s", "%s", "0", "0", "%s", "%s")' % (tweet["userid"], tweet["tweetContent"], tweet["timeToSend"], tweet["tweetType"], tweet["threadOrderId"]))

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

  myCursor.execute('SELECT * FROM testdatabase.ScheduledTweets where timetosend = "%s"' % (str(time)))
  
  tweets = myCursor.fetchall()

  tweetList = []
  for tweet in tweets:
    tweetObject = {
      "id" : tweet[0],
      "userid" : tweet[1],
      "tweetcontent" : tweet[2],
      "timetosend" : tweet[3],
      "sent" : tweet[4],
      "timesent" : tweet[5],
      "done" : tweet[6],
      "tweettype" : tweet[7],
      "threadorderid" : tweet[8]
    }

    tweetList.append(tweetObject)
  
  return tweetList

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