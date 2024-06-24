import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='YOUR_SPOTIFY_CLIENT_ID',
    client_secret='YOUR_SPOTIFY_CLIENT_SECRET',
    redirect_uri='YOUR_SPOTIFY_REDIRECT_URI',
    scope='user-library-read playlist-modify-public'
))

def get_user_playlists():
    results = sp.current_user_playlists()
    return results