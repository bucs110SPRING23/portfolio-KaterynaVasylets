import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os

# Spotify API credentials
SPOTIFY_CLIENT_ID = '929f22ff8f34416fb233c27cd66b5249'
SPOTIFY_CLIENT_SECRET = '63be50b90cda4cf587cfcf3f2ebcf3e6'

# Last.fm API credentials
LASTFM_API_KEY = '9ad0f476570de1894d19e3359b8938a0'

class APIHandler:
    def __init__(self, api_url):
        self.api_url = api_url

    def __str__(self):
        return f"APIHandler for {self.api_url}"

    def handle_request(self):
        raise NotImplementedError("Subclasses should implement this method.")


class LastFMAPIHandler(APIHandler):
    def handle_request(self, genre, limit):
        url = f'{self.api_url}?method=tag.gettoptracks&tag={genre}&api_key={LASTFM_API_KEY}&format=json&limit={limit}'
        response = requests.get(url)
        data = json.loads(response.text)
        try:
            return data['tracks']['track']
        except KeyError:
            print("The key 'tracks' or 'track' does not exist in data.")
            return []


class SpotifyAPIHandler(APIHandler):
    def __init__(self, api_url, client_id, client_secret):
        super().__init__(api_url)
        self.client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def handle_request(self, genre, limit):
        results = self.sp.recommendations(seed_genres=[genre], limit=limit)
        return results['tracks']


class Proxy:
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def get_recommendations(self, genre, limit):
        return self.api_handler.handle_request(genre, limit)


lastfm_handler = LastFMAPIHandler('http://ws.audioscrobbler.com/2.0/')
spotify_handler = SpotifyAPIHandler('https://api.spotify.com/v1/', SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

print("What's your favorite music genre?")
genre = input().lower()

print("How many recommendations do you want?")
limit = int(input())

lastfm_proxy = Proxy(lastfm_handler)
spotify_proxy = Proxy(spotify_handler)

lastfm_recommendations = lastfm_proxy.get_recommendations(genre, limit)
spotify_recommendations = spotify_proxy.get_recommendations(genre, limit)

print("\nLast.fm Recommendations:")
for i, track in enumerate(lastfm_recommendations):
    print(f"{i + 1}. {track['name']} by {track['artist']['name']}")

print("\nSpotify Recommendations:")
for i, track in enumerate(spotify_recommendations):
    print(f"{i + 1}. {track['name']} by {track['artists'][0]['name']}")