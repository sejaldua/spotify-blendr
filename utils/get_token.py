import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

token = util.prompt_for_user_token('sejaldua', 
        scope='playlist-read-private', 
        client_id=os.environ.get('CLIENT_ID'), 
        client_secret=os.environ.get('CLIENT_SECRET'), 
        redirect_uri='http://localhost:4567/')
print(token)
urn = 'spotify:artist:2qk9voo8llSGYcZ6xrBzKx'
artist = sp.artist(urn)
print(artist)