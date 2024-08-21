from bs4 import BeautifulSoup
import requests

CLIENT_ID = "f5df19c3290f42d4ac9f6431e3d576d7"
CLIENT_SECRET = "c88bb34c5b074f3b8a51d974875c9994"
URL_ENDPOINT = "https://www.billboard.com/charts/hot-100/"
# DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
DATE = "2000-08-12"

response = requests.get(f"{URL_ENDPOINT}/{DATE}/")
content = response.text
soup = BeautifulSoup(content,"html.parser")
playlist_title = soup.title.text
print(playlist_title)

#
song_title = soup.select("ul li h3.c-title")
title = None
if song_title:
    title = [title.get_text(strip=True) for title in song_title]

print(title)

song_artists = soup.select("li ul li span.c-label")
artist = None
if song_artists:
    artist_texts = [artist.get_text(strip=True) for artist in song_artists]
    # Filter out entries that are likely to be numbers or non-artist names
    artist = [text for text in artist_texts if not text.isdigit() and text != '-']
print(artist)
playlist_data = [playlist_title,title,artist]
print(playlist_data)







