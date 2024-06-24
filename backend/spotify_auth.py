from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp_oauth = SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='user-library-read playlist-modify-public'
)

sp = spotipy.Spotify(auth_manager=sp_oauth)

def get_user_playlists():
    results = sp.current_user_playlists()
    return results

def get_auth_url():
    return sp_oauth.get_authorize_url()

def get_token(code):
    token_info = sp_oauth.get_access_token(code)
    return token_info