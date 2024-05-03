
# Save an excel sheet of all my liked songs and their artists on Spotify

import spotipy
from dotenv import load_dotenv
import os
import spotipy.util as util
import pandas as pd
import datetime


# Set scope
scope = 'user-library-read'

# Load authentication variables from .env file
load_dotenv()
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
client_redirect = os.getenv('SPOTIPY_REDIRECT_URI')
username = input('Enter Spotify username:')

# Authenticate
token = util.prompt_for_user_token(username=username,
                           scope=scope,
                           client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri=client_redirect)


sp = spotipy.Spotify(auth=token)
print('Successfully authenticated')

# Initialize an empty list to store all the songs
all_songs = []

# Set the initial offset to 0
offset = 0

# Set the limit for each request
limit = 50

# Fetch the first batch of songs
results = sp.current_user_saved_tracks(limit=limit, offset=offset)

# Extract the first batch of items
all_songs.extend(results['items'])

# if having issues try restarting terminal
# Fetch subsequent batches of songs until all songs are retrieved
while len(all_songs) < results['total']:
    offset += limit
    results = sp.current_user_saved_tracks(limit=limit, offset=offset)
    all_songs.extend(results['items'])
    print(len(all_songs))

# Extract song names and artists from the results
songs = [item['track']['name'] for item in all_songs]
artists = [', '.join(artist['name'] for artist in item['track']['artists']) for item in all_songs]

# Create a DataFrame
df = pd.DataFrame({'Song': songs, 'Artist': artists})

# First three songs and artists
df[0:3]
df[0:40]

df = df.drop_duplicates()
print(len(df))

# Save
today_date = datetime.now().strftime('%Y_%m_%d')
file_path = f'mysongs_{today_date}.xlsx'
df.to_csv(file_path, index=False)

print('Successfully saved .csv file')

