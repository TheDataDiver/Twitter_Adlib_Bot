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


# RANDOM WORD SELECTION AND PRINTING OF HOROSCOPE FOR EACH SIGN
noun = wordselection('concrete_nouns.txt').capitalize()
# noun2 = wordselection('concrete_nouns.txt')
verb = wordselection('verbs.txt').lower()
# adjective = wordselection('adjectives.txt')
# adverb = wordselection('adverbs.txt')


# CHECKING IF EDITED WALLPAPER DIRECTORY ALREADY EXISTS, IF NOT CREATE THE DIRECTORY
if not os.path.exists('/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/edited_wallpaper'):
    os.makedirs('/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/edited_wallpaper')


# COUNTING HOW MANY JPG FILES ARE PRESENT IN THE STOCK WALLPAPER FOLDER
os.chdir('/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/stock_wallpaper')
i = 0
x = []
for file in os.listdir():
    if file.endswith('.jpg'):
        i += 1


# GENERATING A RANDOM NUMBER USED TO SELECT THE IMAGE
imagenumber = random.randint(0, i - 1)


# SPECIFYING FONT PATHS AND SELECTED IMAGE PATH
image_font_path = '/Users/johnjameshutchinson/Library/Fonts/'
image_path_input = '/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/stock_wallpaper/'
image_path_output = '/Users/johnjameshutchinson/icloud/GitHub/Twitter/Blessed_Adlibs/edited_wallpaper/'
image_name_input = '{}.jpg'.format(imagenumber)


# OPENING THE IMAGE AND FINDING ITS DIMENSIONS
im = Image.open(image_path_input + image_name_input)
W, H = im.size
# position = (W / 2, H / 2)
message = '{} the {}'.format(verb, noun)
font = ImageFont.truetype(image_font_path + 'impact.ttf', size=300)
color = (0, 0, 0)


# INITIALISING DRAWING CONTEXT WITH IMAGE AS OBJECT BACKGROUND
draw = ImageDraw.Draw(im)
w, h = draw.textsize(message)
draw.text(((W-w)/2,(H-h)/2), message, fill=color, font=font)


# SAVING THE EDITED IMAGE
image_name_output = '{}_edited.jpg'.format(imagenumber)
im.save(image_path_output + image_name_output)


# BASH SCRIPT TO RENAME PICTURES IN INCREMENTING ORDER
# find . -name '*.jpg' \
# | awk 'BEGIN{ a=0 }{ printf "mv \"%s\" %04d.jpg\n", $0, a++ }' \
# | bash


######## INSERT FONTS OVER IMAGE ON PYTHON


######## UPLOAD IMAGE WITH HASHTAGS TO TWITTER


######## IMPACT FONT



######## IF YOU MENTION THE ACCOUNT, IT WILL PUT WHATEVER IS IN THE MENTION ON A RANDOM IMAGE FOR YOU
