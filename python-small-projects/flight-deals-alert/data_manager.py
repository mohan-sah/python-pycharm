import requests
import pandas as pd
from pprint import pprint
from dotenv import load_dotenv

import os
from dotenv import load_dotenv

load_dotenv()

MY_ENV_VAR = os.getenv('MY_ENV_VAR')
SHEETY_AUTHORIZATION = os.getenv('SHEETY_AUTHORIZATION')

SHEETY_ENDPOINT = "https://api.sheety.co/d5cbe021794f22c079cba500da92b423/flightPrices/sheet1"
headers = {
    "Authorization": SHEETY_AUTHORIZATION
}


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.parameters = None
        self.response = None
        self.datarow = None
        self.SHEETY_ENDPOINT = SHEETY_ENDPOINT

        self.headers = {
            "Authorization": SHEETY_AUTHORIZATION
        }

    def getdata(self):
        self.response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        self.response.raise_for_status()
        self.datarow = self.response.json()['sheet1']
        return self.datarow

    def edit_exiting_record(self):
        for city in self.datarow:
            self.parameters = {
                "sheet1": {"iataCodes": city["iataCodes"],
                           }
            }
            self.response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", headers=headers, json=self.parameters)
            self.response.raise_for_status()


# data_manager = DataManager()
# data_manager.edit_exiting_record()

# #This class is responsible for talking to the Google Sheet.
# SHEETY_ENDPOINT = "https://api.sheety.co/d5cbe021794f22c079cba500da92b423/flightPrices/sheet1"
# headers = {
#         "Authorization": "Basic ZmxpZ2h0X3ByaWNlczpqazQ4cndxOWVhZnVzZGlvam4jZGo="
#     }
#
# response =  requests.get(url=SHEETY_ENDPOINT, headers=headers)
# response.raise_for_status()
# data = response.json()
# pprint(data)
