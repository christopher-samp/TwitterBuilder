from flask import Flask, jsonify
from flask_cors import CORS
import json
from datetime import datetime,timedelta
import requests

import tweepy

#auth = ""
#api = ""
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    get_auth_api()
    return "hello world!"

    
    
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
    access_token = "369867339-8drZ7FPKl8BdZjgJdlnj07x82r5SWz4derBVfN8S"
    access_token_secret = "bj3lqGkWCDABRMVA2LewMLvmd1K3YLPgcfNTUBMQ1FhMP"

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
    access_token = "369867339-8drZ7FPKl8BdZjgJdlnj07x82r5SWz4derBVfN8S"
    access_token_secret = "bj3lqGkWCDABRMVA2LewMLvmd1K3YLPgcfNTUBMQ1FhMP"

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
    print(theTweet)
    tweet = {
        "data": theTweet.data.text,
        "id": theTweet.data.id,
        "profile_image_https": theUser['profile_image_url_https']
    }
    tweetlist = [tweet]

    return jsonify(tweetlist)
    
@app.route('/GetUserById')
def get_user_by_id():
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-8drZ7FPKl8BdZjgJdlnj07x82r5SWz4derBVfN8S"
    access_token_secret = "bj3lqGkWCDABRMVA2LewMLvmd1K3YLPgcfNTUBMQ1FhMP"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    # client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)

    fullUser = api.get_user(id=369867339,user_auth=True, user_fields=['profile_image_url','public_metrics'])._json
    
    user = {
        "name": fullUser['name'],
        "id": fullUser['id'],
        "screen_name": fullUser['screen_name'],
        "followers_count": fullUser['followers_count'],
        "friends_count": fullUser['friends_count'],
        "statuses_count": fullUser['statuses_count'],
        "profile_image_url_https": fullUser['profile_image_url']
    }
    userList = [user]

    return jsonify(userList)

@app.route('/GetTweets/<keyword>')
def get_tweets(keyword):
    return get_tweets_helper(keyword, "popular", 10)

def get_tweets_helper(keyword, resultType, numTweets):
    consumer_key = "niFrGMblGwSn7TzYPntdFqeEr"
    consumer_secret = "T8d4UU9vahI4oUzVUX9Cxh2srs4axKXEZ6rbr0QvwPpOFfL52g"

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = "369867339-8drZ7FPKl8BdZjgJdlnj07x82r5SWz4derBVfN8S"
    access_token_secret = "bj3lqGkWCDABRMVA2LewMLvmd1K3YLPgcfNTUBMQ1FhMP"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)

    TweetList = []
    for status in tweepy.Cursor(api.search_tweets, keyword, tweet_mode = "extended", lang="en", result_type=resultType,
                            count=100).items(numTweets):
        print(status._json)
        
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
            "userid": status._json['user']['id']
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
    access_token = "369867339-8drZ7FPKl8BdZjgJdlnj07x82r5SWz4derBVfN8S"
    access_token_secret = "bj3lqGkWCDABRMVA2LewMLvmd1K3YLPgcfNTUBMQ1FhMP"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)

    contextUser = json.loads(get_user_by_id().get_data())
    contextUserFollowers = contextUser[0]['followers_count']

    UserList = []
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
                # if(usernameAt == "SaaS_group"):
                #     print(user._json)
                userObject = {
                    "userid": userid,
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




    
    
