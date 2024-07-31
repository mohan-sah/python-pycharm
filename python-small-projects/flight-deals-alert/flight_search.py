import requests
from pprint import pprint

API_Key = "yf58gGSLCYDtBjq2SMKQlcUZb62EvUGa"
API_Secret = "rKjU0TEWGst3PCzG"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):

        URL_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {
            "Authorization": f"Bearer {flight_search._get_new_token()}"
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



flight_search = FlightSearch()
city = "Paris"



#test.api.amadeus.com/v2






# type             : amadeusOAuth2Token
# username         : mohansah944@gmail.com
# application_name : Flight_Price_lowest
# client_id        : yf58gGSLCYDtBjq2SMKQlcUZb62EvUGa
# token_type       : Bearer
# access_token     : DjaSzucggfU2LCG2Brix5F3TtZ4O
# expires_in       : 1799

{'type': 'amadeusOAuth2Token',
 'username': 'mohansah944@gmail.com'
    , 'application_name': 'Flight_Price_lowest',
 'client_id': 'yf58gGSLCYDtBjq2SMKQlcUZb62EvUGa',
 'token_type': 'Bearer',
 'access_token': 'NywpHOPpxbD44H9x2yaDAimmjMwK',
 'expires_in': 1799, 'state': 'approved', 'scope': ''}
