from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify

import json
import time
import sys
import os

# Authenticate with Spotify using the Client Credentials flow

load_dotenv()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def homepage():
    # Displays homepage
    # return render_template('index.html')
    return render_template('track-feature.html')
  
@app.route('/new_releases', methods=['GET'])
def new_releases():
  
    # Use the country from the query parameters, if provided
    if 'country' in request.args:
        country = request.args['country']
    else:
        country = 'SE'
    
    # Send request to the Spotify API
    new_releases = sp.new_releases(country=country, limit=5, offset=0)
    
    # Return the list of new releases
    return jsonify(new_releases)

# TODO: complete this method:
#       - provide track info on each
@app.route('/track_features', methods=['GET'])
def track_features():

    # Use the country from the query parameters, if provided
    if 'artist' in request.args:
        artist = request.args['artist']
    else:
        artist = 'Drake'

    print(artist)

    results = sp.search(q=artist, limit=1, offset=0)
    features = []
    data = []
    for idx, track in enumerate(results['tracks']['items']):
        print(idx+1, track['name'], track['id'])
        features = sp.audio_features(str(track['id']))
        data.append({'track': track['name'], 'features': features})
        # print(json.dumps(features, indent=4)) 

    return jsonify(data)


# if len(sys.argv) > 1:
#     tids = sys.argv[1:]
#     print(tids)   

#     if 'debug' in tids:
#     	sp.trace = True

#     start = time.time()
    
#     results = sp.search(q=tids, limit=5)
#     for idx, track in enumerate(results['tracks']['items']):
#         print(idx, track['name'], track['id'])
#         features = sp.audio_features(str(track['id']))
#         print(json.dumps(features, indent=4))

#     delta = time.time() - start
#     # print(json.dumps(features, indent=4))
#     print("features retrieved in %.2f seconds" % (delta,))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


