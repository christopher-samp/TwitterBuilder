from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime,timedelta
import requests
import tweepy
import UserSql
from flask_apscheduler import APScheduler

app = Flask(__name__)
CORS(app)

scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)


@app.route('/')
def hello_world():
    get_auth_api()
    return "hello world!"

@scheduler.task('interval', id='tweet_scheduler_job', seconds=60, misfire_grace_time=900)
def tweet_scheduler():
    now = datetime.now().replace(second=0, microsecond=0)
    now.strftime('%Y-%m-%d %H:%M')
    print(now)
    tweets = UserSql.CheckForScheduledTweets(now)
    print(tweets)
    

    #check if tweets are empty, if they are continue, if they aren't tweet them, then update the sent tweets table
    if(tweets != []):
        sendTweet(tweets)

    print("TEST")
    
def get_auth_api():
    # Your app's API/consumer key and secret can be found under the Consumer Keys
    # section of the Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"
    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    # If the authentication was successful, this should print the
    # screen name / username of the account
    #return api.verify_credentials().screen_name
    
@app.route('/recent')
def recent_searches():
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)
    #print(client.get_tweet(1462814411970723844, user_auth=True))
    #print(api.get_saved_searches())
    #print(len(api.get_saved_searches()))
    theTweet = client.get_tweet(id=1462814411970723844, user_auth=True, expansions='author_id', media_fields='preview_image_url', tweet_fields="public_metrics")
    UsersId = theTweet.includes['users'][0].id
    
    theUser = api.get_user(id=UsersId, user_auth=True, user_fields=['profile_image_url'])._json
    tweet = {
        "data": theTweet.data.text,
        "id": theTweet.data.id,
        "profile_image_https": theUser['profile_image_url_https']
    }
    tweetlist.append(tweet)



    return jsonify(tweetlist)

@app.route('/GetWatchListTweets')
def get_watchlist_tweets():
    contextUserId = request.args.get('userId', None)
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)
    TweetList = []
    #call to sql to get list of users to get tweets for
    watchListIds = UserSql.GetWatchListConnections(contextUserId)
    for x in watchListIds:
        tweets = client.get_users_tweets(id=x[0], user_auth=True, exclude=['retweets','replies'], tweet_fields=['created_at','public_metrics'], user_fields=['username', 'name', 'id', 'profile_image_url'], expansions='author_id')

        users = {u["id"]: u for u in tweets.includes['users']}
        for tweet in tweets.data:
            if users[tweet.author_id]:
                user = users[tweet.author_id]
                dtime = tweet["created_at"]
                date_time = dtime.strftime("%m-%d-%Y, %H:%M:%S")
                tweetObject = {
                    "name": user.name,
                    "username": user.username,
                    "date": date_time,
                    "data": tweet["text"],
                    "profile_image_url_https": user.profile_image_url,
                    "id": str(tweet["id"]),
                    "retweets": tweet["public_metrics"]["retweet_count"],
                    "favorites": tweet["public_metrics"]["like_count"],
                    "userid": str(user.id)
                }
                TweetList.append(tweetObject)
            continue

    TweetList.sort(key=lambda x: datetime.strptime(str(x["date"]), "%m-%d-%Y, %H:%M:%S"), reverse=True)
    return jsonify(TweetList)

    
@app.route('/GetUserById/<userid>')
def get_user_by_id(userid):
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    # client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)

    fullUser = api.get_user(id=userid,user_auth=True, user_fields=['profile_image_url','public_metrics'])._json
    
    user = {
        "name": fullUser['name'],
        "id": str(fullUser['id']),
        "screen_name": fullUser['screen_name'],
        "followers_count": fullUser['followers_count'],
        "friends_count": fullUser['friends_count'],
        "statuses_count": fullUser['statuses_count'],
        "profile_image_url_https": fullUser['profile_image_url']
    }
    userList = [user]

    return jsonify(userList)

@app.route('/GetUserByScreenName/<screenName>')
def get_user_by_screen_name(screenName):
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    fullUser = api.get_user(screen_name=screenName,user_auth=True, user_fields=['profile_image_url','public_metrics','profile_banner_url'])._json

    banner = ""
    if "profile_banner_url" in fullUser:
        banner = fullUser['profile_banner_url']
    else:
        banner = "https://pbs.twimg.com/profile_banners/3251189440/1515410621"
    
    user = {
        "name": fullUser['name'],
        "id": str(fullUser['id']),
        "screen_name": fullUser['screen_name'],
        "followers_count": fullUser['followers_count'],
        "friends_count": fullUser['friends_count'],
        "statuses_count": fullUser['statuses_count'],
        "profile_image_url_https": fullUser['profile_image_url'],
        "description": fullUser['description'],
        "profile_banner_url": banner
    }
    userList = [user]

    return jsonify(userList)

@app.route('/GetTweets/<keyword>')
def get_tweets(keyword):
    return get_tweets_helper(keyword, "mixed", 100)

def get_tweets_helper(keyword, resultType, numTweets):
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    #client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)

    TweetList = []
    for status in tweepy.Cursor(api.search_tweets, keyword, tweet_mode = "extended", lang="en", result_type=resultType,
                            count=100).items(numTweets):

        favoriteCount=status._json['favorite_count']
        retweetCount=status._json['retweet_count']

        if "retweeted_status" in status._json:
            favoriteCount = status._json['retweeted_status']['favorite_count']
            retweetCount = status._json['retweeted_status']['retweet_count']
            
        tweet = {
            "data": status._json['full_text'],
            "id": str(status._json['id']),
            "retweets": status._json['retweet_count'],
            "favorites": favoriteCount,
            "date": status._json['created_at'],
            "profile_image_url_https": status._json['user']['profile_image_url_https'],
            "username": status._json['user']['screen_name'],
            "userid": str(status._json['user']['id'])
        }
        TweetList.append(tweet)
        
    return jsonify(TweetList)

@app.route('/NicheUsers/<keyword>')
def get_users_in_niche(keyword):
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)

    contextUser = json.loads(get_user_by_id(369867339).get_data())
    contextUserFollowers = contextUser[0]['followers_count']

    UserList = []

    if("@" in keyword):
        user = json.loads(get_user_by_screen_name(keyword).get_data())
        print(user)
        banner = ""
        if 'profile_banner_url' in user[0]:
            banner = user[0]['profile_banner_url']
        else:
            banner = "https://pbs.twimg.com/profile_banners/3251189440/1515410621"

        userObject = {
                    "userid": user[0]['id'],
                    "username": user[0]['name'],
                    "usernameAt": user[0]['screen_name'],
                    "description" : user[0]['description'],
                    "followers": user[0]['followers_count'],
                    "following": user[0]['friends_count'],
                    "profile_image_url_https": user[0]['profile_image_url_https'],
                    "profile_banner_url": banner,
                    "statuses_count": user[0]['statuses_count']
                }
                
        UserList.append(userObject)
        return jsonify(UserList)


    while(len(UserList) < 10):
        for user in tweepy.Cursor(api.search_users, keyword,
                                count=50).items(50):
            searchedUserFollowerCount = user._json['followers_count']
            if(searchedUserFollowerCount > contextUserFollowers and
               searchedUserFollowerCount < 10*contextUserFollowers):
                userid = user._json['id']
                username = user._json['name']
                usernameAt = user._json['screen_name']
                lastTweetTime = user._json['status']['created_at']
                description = user._json['description']

                banner = ""
                if 'profile_banner_url' in user._json:
                    banner = user._json['profile_banner_url']
                else:
                    banner = "https://pbs.twimg.com/profile_banners/3251189440/1515410621"

                if validate_users_activity(userid, usernameAt.lower(), username.lower(), description.lower(), keyword.lower(), lastTweetTime) == False:
                    continue

                userObject = {
                    "userid": str(userid),
                    "username": username,
                    "usernameAt": usernameAt,
                    "description" : description,
                    "followers": searchedUserFollowerCount,
                    "following": user._json['friends_count'],
                    "profile_image_url_https": user._json['profile_image_url_https'],
                    "profile_banner_url": banner,
                    "statuses_count": user._json['statuses_count']
                }
                
                UserList.append(userObject)
                
    return jsonify(UserList)

def validate_users_activity(userid, screenName, name, description, keyword, lastTweetTime):
    if keyword not in description and keyword not in screenName and keyword not in name:
        return False

    lastTweetTimeFormated = datetime.strftime(datetime.strptime(lastTweetTime,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
    lastTweetDateTime = datetime.strptime(lastTweetTimeFormated, '%Y-%m-%d %H:%M:%S')
    sevenDaysAgo = datetime.now() - timedelta(days=7)
    if(lastTweetDateTime < sevenDaysAgo):
        return False

    return True

@app.route('/AddWatchListUser')
def AddWatchListConnection():
    watchListUserId = request.args.get('watchListUserId', None)
    userId = request.args.get('userId', None)

    UserSql.AddWatchListConnection(watchListUserId, userId)
    return ""

@app.route('/RemoveFromWatchList')
def RemoveFromWatchListConnection():
    watchListUserId = request.args.get('watchListUserId', None)
    userId = request.args.get('userId', None)

    UserSql.RemoveFromWatchListConnection(watchListUserId, userId)
    return ""

@app.route('/ReplyToTweet')
def ReplyToTweet():
    replyTweetId = request.args.get('replyTweetId', None)
    retweetResponse = request.args.get('retweetResponse', None)

    print(replyTweetId)
    data = request.args.get('status', None)

    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)

    tweet = api.update_status(status=data, in_reply_to_status_id=replyTweetId)._json

    if(retweetResponse == "true"):
        client.retweet(tweet_id=tweet['id_str'])
    
    client.like(tweet_id=replyTweetId)

    return jsonify(success=True)

def sendTweet(tweets):
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-q5DSx09GROTNKesxvkexFO7cXszkGQQMGfx4lrZU"
    access_token_secret = "HJBb0vnWOJxwdLhjEuGOELWMB5PrVIjQAjk1FNfcdxhIu"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    for tweet in tweets:
        if(tweet['threadorderid'] != 1):
            newReplyTweet = api.update_status(status=tweet['tweetcontent'], in_reply_to_status_id=newReplyTweet['id_str'])._json
        else:
            newReplyTweet = api.update_status(status=tweet['tweetcontent'])._json
        print(newReplyTweet['id_str'])

@app.route('/ScheduleTweet')
def ScheduleTweet():
    tweets = request.args.get('tweets', None)
    print("Tweet JSON: "+tweets)
    tweetObjects = json.loads(tweets)
    returnValue = UserSql.InsertIntoScheduledTweets(tweetObjects)
    return jsonify(success="200")

scheduler.start()



    
    
