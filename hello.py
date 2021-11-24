from flask import Flask
import tweepy

#auth = ""
#api = ""
app = Flask(__name__)
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
    consumer_key = ""
    consumer_secret = ""

    # Your account's (the app owner's account's) access token and secret for your
    # app can be found under the Authentication Tokens section of the
    # Keys and Tokens tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps
    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    client = tweepy.Client(auth, consumer_key, consumer_secret, access_token, access_token_secret)
    #print(client.get_tweet(1462814411970723844, user_auth=True))
    #print(api.get_saved_searches())
    #print(len(api.get_saved_searches()))
    
    return client.get_tweet(1462814411970723844, user_auth=True).data.text
    
    
