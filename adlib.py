#!/usr/bin/env python3

import tweepy

CONSUMER_KEY = '91yh0WCkI8fkyLnFEjcixCI8I'
CONSUMER_SECRET = '4e9HddAeR7cB24PsTwUUiiwcmAnnf8Nxd0uEh44H4r2RNqmRXE'
ACCESS_KEY = '2539948627-XTXBb6QSawDuQbaer6PEIoEbtTsGoQq6IP9VZzb'
ACCESS_SECRET = 'cV4Y04qJ1y1uyfimOr323blAOHIJTSJZFz4Fd0Nkjd4yr'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
