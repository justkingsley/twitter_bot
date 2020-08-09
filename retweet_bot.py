
# Import Tweepy, sleep, credentials.py
import tweepy
import time 

from credentials import consumer_key
from credentials import consumer_secret
from credentials import access_token
from credentials import access_token_secret


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#INTERVAL = 60 * 60 * 6

for tweet in tweepy.Cursor(api.search, q=('#zimbabweanlivesmatter, #freehopewell  -filter:retweets'), lang='en').items(5):
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        #time.sleep(INTERVAL)
        print('Retweeted the tweet')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, q=('#zimbabweanlivesmatter, #freehopewell-filter:retweets'),lang='en').items(10):
            try:
                # Add \n escape character to print() to organize tweets
                print('\nTweet by: @' + tweet.user.screen_name)

                # Retweet tweets as they are found
                tweet.favorite()
                print('Like the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break