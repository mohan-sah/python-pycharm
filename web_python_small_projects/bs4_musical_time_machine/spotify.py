import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=   CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://www.google.com/",
                                               scope="user-library-read"))
DATE = "2000-08-12"
year = DATE.split("-")[0]
### finding the song list in spotify and getting their id

from main import playlist_data
song_uri = []
for song in playlist_data[1]:
    result = sp.search(q=f"track:{song} ", type="track")  # year:{year}
    try :
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_uri)

### creating new playlist

scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=   CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://www.google.com/",
                                               scope=scope))

user = sp.current_user()["id"]
playlist_name = 'Test'
playlist_details = sp.user_playlist_create(user = user, name = playlist_name , public=True, collaborative=False, description=f'hots of {DATE}')
playlist_id = playlist_details["id"]
print(playlist_id)


# can add cover
##https://www.google.com/?code=AQAgT1trhgTYzVW2NiHUI0TQUbKAMV_5oErMFx-KRM9RNxgJl2xqDNUOCNppLC2MuN4MlgdfmcqZbqCqAJQ7M3AWQuey3xLzGD1J2D3t2wNjbBUSWDRr8tEDU44WIF1JSFxR9HmnosDBfKAyCnzH0VZYBMGsVV8XOfIJk59w-qslRmCSYMfehkqNS1NKfnCtr_CA
### adding song from spotify

sp.playlist_add_items(playlist_id= playlist_id, items= song_uri, position=None)




## need balance between recall and presicion
## resuce missing search (0.09)  better
# (Hot S**t) Country Grammar doesn't exist in Spotify. Skipped.
# Purest Of Pain (A Puro Dolor) doesn't exist in Spotify. Skipped.
# Prayin' For Daylight doesn't exist in Spotify. Skipped.
# Come On Over Baby (All I Want Is You) doesn't exist in Spotify. Skipped.
# Swear It Again doesn't exist in Spotify. Skipped.
# You'll Always Be Loved By Me doesn't exist in Spotify. Skipped.
# Californication doesn't exist in Spotify. Skipped.
# Country Comes To Town doesn't exist in Spotify. Skipped.
# When You Need My Love doesn't exist in Spotify. Skipped.
# With Arms Wide Open doesn't exist in Spotify. Skipped.

## reduce missing search (.42)
# Incomplete doesn't exist in Spotify. Skipped.
# Everything You Want doesn't exist in Spotify. Skipped.
# Higher doesn't exist in Spotify. Skipped.
# Doesn't Really Matter doesn't exist in Spotify. Skipped.
# (Hot S**t) Country Grammar doesn't exist in Spotify. Skipped.
# Desert Rose doesn't exist in Spotify. Skipped.
# Breathe doesn't exist in Spotify. Skipped.
# What'Chu Like doesn't exist in Spotify. Skipped.
# The Next Episode doesn't exist in Spotify. Skipped.
# I Turn To You doesn't exist in Spotify. Skipped.
# What About Now doesn't exist in Spotify. Skipped.
# Big Pimpin' doesn't exist in Spotify. Skipped.
# Smooth doesn't exist in Spotify. Skipped.
# Purest Of Pain (A Puro Dolor) doesn't exist in Spotify. Skipped.
# Prayin' For Daylight doesn't exist in Spotify. Skipped.
# It Must Be Love doesn't exist in Spotify. Skipped.
# I Try doesn't exist in Spotify. Skipped.
# Where I Wanna Be doesn't exist in Spotify. Skipped.
# Faded doesn't exist in Spotify. Skipped.
# Amazed doesn't exist in Spotify. Skipped.
# Come On Over Baby (All I Want Is You) doesn't exist in Spotify. Skipped.
# Whatever doesn't exist in Spotify. Skipped.
# Swear It Again doesn't exist in Spotify. Skipped.
# Callin' Me doesn't exist in Spotify. Skipped.
# I Will...But doesn't exist in Spotify. Skipped.
# What You Want doesn't exist in Spotify. Skipped.
# Your Everything doesn't exist in Spotify. Skipped.
# You'll Always Be Loved By Me doesn't exist in Spotify. Skipped.
# Cold Day In July doesn't exist in Spotify. Skipped.
# Californication doesn't exist in Spotify. Skipped.
# Broadway doesn't exist in Spotify. Skipped.
# Country Comes To Town doesn't exist in Spotify. Skipped.
# When You Need My Love doesn't exist in Spotify. Skipped.
# It's Always Somethin' doesn't exist in Spotify. Skipped.
# Let's Make Love doesn't exist in Spotify. Skipped.
# With Arms Wide Open doesn't exist in Spotify. Skipped.
# Sour Girl doesn't exist in Spotify. Skipped.
# I Disappear doesn't exist in Spotify. Skipped.
# The One doesn't exist in Spotify. Skipped.
# Some Things Never Change doesn't exist in Spotify. Skipped.
# The Chain Of Love doesn't exist in Spotify. Skipped.
# Hey Papi doesn't exist in Spotify. Skipped.
