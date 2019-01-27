
##Kieran Thompson

import tweepy
from twitterKey import *
import datetime


def twitterMain():
    auth = tweepy.OAuthHandler(ckey,csecret)
    auth.set_access_token(akey,asecret)

    api = tweepy.API(auth)

    date = datetime.datetime.now().strftime("%d\%m\%y")
    ##post image with pic
    api.update_with_media('screenshot.PNG','Update ' + date)


    


