from flask import Flask, request, redirect, session, jsonify, url_for, send_from_directory
from spotify_auth import get_user_playlists, get_auth_url, get_token
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/playlists', methods=['GET'])
def playlists():
    if 'token_info' not in session:
        return redirect(url_for('login'))
    token_info = session['token_info']
    return jsonify(get_user_playlists())

@app.route('/login')
def login():
    auth_url = get_auth_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = get_token(code)
    session['token_info'] = token_info
    return redirect(url_for('playlists'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
