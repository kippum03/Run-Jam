from flask import Flask, request, jsonify
from spotify_auth import get_user_playlists

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Poke Jam"

@app.route('/playlists', methods=['GET'])
def playlists():
    playlists = get_user_playlists()
    return jsonify(playlists)

if __name__ == '__main__':
    app.run(debug=True)