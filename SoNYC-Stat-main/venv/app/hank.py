import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
os.environ['SPOTIPY_CLIENT_ID'] = "f5eb6f7b95d84bd48dea9a50c1cca18f"
os.environ['SPOTIPY_CLIENT_SECRET'] = "37a907df23374db5b9ac602f4847c2b4"


SPOTIPY_CLIENT_ID = '8d9592f7b421418aa35a5f72ea38b9ed'
SPOTIPY_CLIENT_SECRET = '482945fe0ec241b081475de39b4de7bd'

def get_choice(search, choice):
    for item in search:
        if item["name"].lower() == choice.lower():
            return item

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
birdy_uri = 'spotify:artist:4dpARuHxo51G3z768sgnrY'
results = spotify.artist_albums(birdy_uri, album_type='album')
# for key in results: print(key)
#print(results["items"])
albums = results['items']
while results['next']:
    count = 0
    results = spotify.next(results)
    for album in albums:
        if album["name"] == results["items"]["name"]:
            count = 1
        else:
            print(album["name"],results["items"]["name"])

    if count == 0:
        albums.extend(results['items'])

for album in albums:
    print(album['name'])
   # for key in album: print(key)

album_choice = input("which album would you like to look at?")

def get_album_info(album_obj):
    print( "'"+album_obj["name"]+"' was released on ",album_obj["release_date"], "and had",album_obj["total_tracks"], "tracks on it.")

chosen_album = get_choice(albums, album_choice)
print(get_album_info(chosen_album))