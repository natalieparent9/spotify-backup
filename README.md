# Spotify backup

## Description

This program saves a .csv file with the names and artists of all the songs saved in Spotify liked songs library. No more anxiety about accidental loss of all those meticulously accumulated songs.

## Getting Started

### Dependencies

- Spotify access token
- Python 3.11.5
- Spotipy 2.23.0
- Pandas 2.0.3
- Made for MacOS, untested on Windows

### Installing

1. Create an app on Spotify to get credentials for access token <a href="https://developer.spotify.com/documentation/web-api">Spotify Web API</a>
2. Set the redirect URI in your app settings to: 'http://localhost:8888/callback'
[](redirect_uri.png)

3. Install the required dependencies using pip install -r requirements.txt.

### Executing program

1. Set Up Spotify Token: Obtain your Spotify API token and store it in an environment file (.env) for authentication.

```
SPOTIPY_CLIENT_ID =
SPOTIPY_CLIENT_SECRET =
SPOTIPY_REDIRECT_URI =
```
2. Change redirect URI to x in spotify websire project

3. Run the program
```
python spotify_backup.py
```
4. Input username

