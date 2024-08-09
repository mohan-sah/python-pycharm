from bs4 import BeautifulSoup
import requests

MOVIES_ENDPOINT =  "https://www.empireonline.com/movies/features/best-movies-2/"
SHOWS_ENDPOINT = "https://www.empireonline.com/tv/features/best-tv-shows/"
response = requests.get(SHOWS_ENDPOINT)
content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup.title.string)
if soup.title.string != "The 100 Greatest TV Shows Of All Time":
    titles = soup.find_all(name="h3", class_ = "listicleItem_listicle-item__title__BfenH")
    title_text = [title.get_text() for title in titles][::-1]
    with open("movies.txt", mode="w") as file:
        for movie in title_text:
            file.write(f"{movie}\n")
else:
    titles = soup.select(selector="span.content_content__i0P3p h2")
    title_text = [title.get_text() for title in titles][::-1]
    with open("show.txt", mode="w") as file:
        for show in title_text:
            file.write(f"{show}\n")

