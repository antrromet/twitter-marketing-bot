import tweepy
from tweepy import OAuthHandler
import time
from datetime import datetime

start_time = datetime.now()


consumer_key = 'PUT YOUR CONSUMER KEY HERE'
consumer_secret = 'PUT YOUR CONSUMER SECRET HERE'
access_token = 'PUT YOUR ACCESS TOKEN HERE'
access_secret = 'PUT YOUR ACCESS SECRET HERE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# File in which all the followers name will be written
handle_names = open('handle_names', 'w+')

# The screen name of the user of whos followers needs to be fetched
for i,user in enumerate(tweepy.Cursor(api.followers, screen_name="twitter").items()):
    print (str(i)+". "+user.screen_name)
    handle_names.write(user.screen_name+"/n")

# Customize your msg to be delivered to the recipients
# It will sleep for 1 minute after every tweet to prevent Twitter from blocking your application
with open('handle_names') as f:
    for id in f:
        print ("Tweeted to "+id)
        api.update_status("@"+id+" This is a custom msg from the tweet bot!")
        time.sleep(60)

# Prints the total time taken for the script to complete
print datetime.now() - start_time