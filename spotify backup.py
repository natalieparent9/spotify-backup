
# pip3 install spotipy

import spotipy
from dotenv import load_dotenv
import os
import spotipy.util as util
import sys

from spotipy.oauth2 import SpotifyClientCredentials

scope = 'user-library-read'

load_dotenv()
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
client_redirect = os.getenv('SPOTIPY_REDIRECT_URI')

# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



util.prompt_for_user_token(username='natalieparent9',
                           scope=scope,
                           client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri=client_redirect)


results = sp.current_user_saved_tracks()

print(sys.argv)
