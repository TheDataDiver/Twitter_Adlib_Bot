#!/usr/bin/env python3

import tweepy
import time
import os
import random

# LOGIN CREDENTIALS FOR TWITTER
CONSUMER_KEY = '91yh0WCkI8fkyLnFEjcixCI8I'
CONSUMER_SECRET = '4e9HddAeR7cB24PsTwUUiiwcmAnnf8Nxd0uEh44H4r2RNqmRXE'
ACCESS_KEY = '2539948627-XTXBb6QSawDuQbaer6PEIoEbtTsGoQq6IP9VZzb'
ACCESS_SECRET = 'cV4Y04qJ1y1uyfimOr323blAOHIJTSJZFz4Fd0Nkjd4yr'

# TWITTER ACCOUNT LOGIN API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# NAVIGATION TO FOLDER WITH FILES CONTAINING NOUNS, ADJECTIVES, VERBS, CONNECTORS
os.chdir('/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/Word_list')

# FUNCTION FOR RANDOM SELECTION OF SINGLE WORD
def wordselection(filename):
    with open(filename, 'r') as f:
        filelist = f.read().strip().split('\n')
        rnumber = random.randint(1, len(filelist))
        selectedword = filelist[rnumber]
        f.close()
        return selectedword
