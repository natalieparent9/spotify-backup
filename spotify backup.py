
# pip3 install spotipy

import spotipy
from dotenv import load_dotenv
import os
import spotipy.util as util
import sys
from spotipy.oauth2 import SpotifyClientCredentials

# Set scope
scope = 'user-library-read'

# Load authentication variables from .env file
load_dotenv()
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
client_redirect = os.getenv('SPOTIPY_REDIRECT_URI')


# Authenticate
token = util.prompt_for_user_token(username='natalieparent9',
                           scope=scope,
                           client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri=client_redirect)


sp = spotipy.Spotify(auth=token)

# Get my saved songs
results = sp.current_user_saved_tracks()

# See what is in the results
print(results.keys())
print(type(results)) # dictionary

items = results['items']
print(type(items)) # list
print(items[1]) # items is a list of dictionaries
print(items[1].keys()) # dictionary contains added_at and track
print(items[1]['track'].keys()) # track is also a dictionary
print(items[1]['track']['name']) # name of the song
print(items[1]['track']['artists']) 
print(type(items[1]['track']['artists'])) # list
print(items[1]['track']['artists'][0])  # 1 does not exist
print(items[1]['track']['artists'][0]['name']) # artist name


for item in results['items']:
    track = item['track']
    print(track['name'] + ' - ' + track['artists'][0]['name'])
