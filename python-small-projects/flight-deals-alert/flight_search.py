import os

import requests
from pprint import pprint
from datetime import datetime as dt,timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_Key = os.getenv("FLIGHT_API_Key")
API_Secret = os.getenv("FLIGHT_API_Secret")

now = dt.now()
from_time = dt.now() + timedelta(days=1)
from_time = from_time.strftime("%Y-%m-%d")
to_time = dt.now() + timedelta(days=90)
to_time = to_time.strftime("%Y-%m-%d")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):

        URL_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {
            "Authorization": f"Bearer {self._get_new_token()}"
        }
        parameters = {
            "keyword": city_name,
            "max": 1,
            "include": ["AIRPORTS"]
        }

        response = requests.get(url=URL_ENDPOINT, headers=headers, params=parameters)
        response.raise_for_status()
        iatacode = response.json()['data'][0]['iataCode']
        return iatacode
    def _get_new_token(self):
        URL_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        parameters = {
            "grant_type":"client_credentials",
            "client_id": API_Key,
            "client_secret" : API_Secret
        }

        response = requests.post(url=URL_ENDPOINT, headers=headers, data=parameters)
        response.raise_for_status()

        access_token = response.json()['access_token']
        return access_token

    def check_flight(self, origin_city_code, destination_city_code, from_time = from_time, to_time = to_time):

        PRICE = 500000




        URL_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {self._get_new_token()}"
        }
        parameters = {
            "originLocationCode": "BLR",
            "destinationLocationCode": "PAR",
            "departureDate" : from_time,
            "returnDate" : to_time,
            "adults": 1,
            "nonStop":"true",
            "currencyCode" : "INR",
            "maxPrice" : PRICE,
            "max" : 10

        }
        response = requests.get(url=URL_ENDPOINT, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        return data



flight_search = FlightSearch()
flight_search.check_flight("BLR","PAR",None,None)









# type             : amadeusOAuth2Token
# username         : mohansah944@gmail.com
# application_name : Flight_Price_lowest
# client_id        : yf58gGSLCYDtBjq2SMKQlcUZb62EvUG
# token_type       : Bearer
# access_token     : DjaSzucggfU2LCG2Brix5F3TtZ4O
# expires_in       : 1799


