# Creates .env file and adds variables that are needed, to be filled by user

import os

def setup():
    print("Welcome to Spotify Library Exporter Setup!")
    print("This program requires set up of Spotify API token first https://developer.spotify.com/documentation/web-api")
    print("Ensure redirect URI is set to 'http://localhost:8888/callback' in app settings on Spotify website")
    
    # Write the username and token to the .env file
    with open(".env", "w") as env_file:
        env_file.write(f"SPOTIPY_CLIENT_ID=\n")
        env_file.write(f"SPOTIPY_CLIENT_SECRET=\n")
        env_file.write(f"SPOTIPY_REDIRECT_URI=http://localhost:8888/callback\n")
    print("Setup complete.")

if __name__ == "__main__":
    if not os.path.isfile(".env"):
        setup()
        print('.env file has been created, please add client ID and secret to file')
    else:
        print("Environment file already exists. Setup complete.")
