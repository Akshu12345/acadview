#Q3:-
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))
user=api.get_user('vivek_shivam007')
print(user.screen_name)
print(user.followers_count)

