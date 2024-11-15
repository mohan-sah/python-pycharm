import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

class MovieSearch():
    #this class is responsible for talking to the movie database
    def get_movie_by_name(self,movie_name):
        URL = "https://api.themoviedb.org/3/search/movie"
        parameters = {
        "query":movie_name,
        "api_key": API_KEY
        }
        response = requests.get(url=URL,params=parameters)
        response.raise_for_status()
        data =response.json()
        return data


# movie = MovieSearch()
# data = movie.get_movie_by_name("Jack+Reacher")
# print(data)