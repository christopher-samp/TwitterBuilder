from flask import Flask, jsonify
from flask_cors import CORS
import json

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
    print(fullUser)
    # return "asdf"
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
    for status in tweepy.Cursor(api.search_tweets, keyword, tweet_mode = "extended", lang="en",
                            count=100).items(10):
        print(status._json)
        
        favoriteCount=0
        if "retweeted_status" in status._json:
            favoriteCount = status._json['retweeted_status']['favorite_count']
            
        tweet = {
            "data": status._json['full_text'],
            "id": str(status._json['id']),
            "retweets": status._json['retweet_count'],
            "favorites": favoriteCount,
            "date": status._json['created_at'],
            "profile_image_url_https": status._json['user']['profile_image_url_https'],
            "username": status._json['user']['screen_name']
        }
        TweetList.append(tweet)
        
    return jsonify(TweetList)
    
    
