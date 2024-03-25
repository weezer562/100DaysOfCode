import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

year = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select("li.o-chart-results-list__item h3.c-title")
artists = soup.select("li.o-chart-results-list__item span.c-label.a-no-trucate")

# Scrape top 100 billboard songs for given year
song_artist_list = [(song.text.strip(), artist.text.strip()) for song, artist in zip(songs, artists)]

scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

user_id = sp.current_user()['id']
spotify_song_list = []

# Retrieve songs from Spotify
for song, artist in song_artist_list:
    try:
        track = sp.search(f"{song} {artist}", type='track', limit=1)
        spotify_song_list.append(track["tracks"]["items"][0]["uri"])
        print(f"{track["tracks"]["items"][0]["uri"]},{track["tracks"]["items"][00]["name"]}")
    except IndexError:
        print(f"{song} by {artist} doesn't exist in Spotify. Skipped.")

# Create Playlist if it does not exist
playlist = sp.user_playlist_create(user_id, f"Billboard 100 - {year}", public=False)

# Adding Tracks to playlist, 20 at a time
for index in range(0, len(spotify_song_list), 20):
    chunk = spotify_song_list[index:index+20]
    sp.playlist_add_items(playlist["id"], chunk, position=index)


