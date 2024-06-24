import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='06d558d41a064279848b9881cd6b7686',
    client_secret='Y80a4366ccb804f5b9e9f4b1c551b295b',
    redirect_uri='http://localhost:5000/callback',
    scope='user-library-read playlist-modify-public'
))

def get_user_playlists():
    results = sp.current_user_playlists()
    return results