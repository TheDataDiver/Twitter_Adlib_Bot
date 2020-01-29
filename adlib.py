#!/usr/bin/env python3

import tweepy
import time
import os
import random
from PIL import Image, ImageDraw, ImageFont

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

# FUNCTION FOR PRINTING OF AD-LIB
def adlib():
    print("%s the %s" % (verb, noun))

# RANDOM WORD SELECTION AND PRINTING OF HOROSCOPE FOR EACH SIGN
noun = wordselection('concrete_nouns.txt')
noun2 = wordselection('concrete_nouns.txt')
verb = wordselection('verbs.txt')
adjective = wordselection('adjectives.txt')
adverb = wordselection('adverbs.txt')
adlib()

# CHECKING IF EDITED WALLPAPER DIRECTORY ALREADY EXISTS, IF NOT CREATE THE DIRECTORY
if not os.path.exists('/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/edited_wallpaper'):
    os.makedirs('/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/edited_wallpaper')

# COUTING HOW MANY JPG FILES ARE PRESENT IN THE STOCK WALLPAPER FOLDER
os.chdir('/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/stock_wallpaper')
i = 0
x = []
for file in os.listdir():
    if file.endswith('.jpg'):
#        x.append(file)
        i += 1
print(i)
