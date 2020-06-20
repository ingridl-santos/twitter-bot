import tweepy
from time import sleep
from credenciais import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q = '#BLACKPARADE').items():
    try:
        print('\nTuitado por: @' + tweet.user.screen_name)
        tweet.retweet()
        print('RT o tweet')

        tweet.favorite()
        print('Tweet favoritado')

        sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break