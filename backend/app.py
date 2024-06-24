from flask import Flask, request, jsonify, send_from_directory
from spotify_auth import get_user_playlists
from poke_api import get_pokemon_data

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/playlists', methods=['GET'])
def playlists():
    playlists = get_user_playlists()
    return jsonify(playlists)

@app.route('/pokemon/<name>', methods=['GET'])
def pokemon(name):
    data = get_pokemon_data(name)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)