# use of trackapi.nutritionix of exercise NLP
# use of shetty for google sheets access


import requests
from datetime import datetime as dt
import json
import os


APP_ID = os.environ.get("APP_ID", "APP_ID not found in environment varible")
API_KEY = os.environ.get("API_KEY", "APP_KEY not found in environment varible")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "SHEETY_TOKEN not found in environment varible")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "SHEETY_ENDPOINT not found in environment varible")

print(APP_ID,API_KEY,SHEETY_TOKEN)
headers = {
    'Content-Type': 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
QUERY = input("tell me about your exercise? :")
WEIGHT_KG = 74
HEIGHT_CM = 183
AGE = 22

parameters = {
    "query": QUERY,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

api_endpoint = exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=api_endpoint, headers=headers, json=parameters)
response.raise_for_status()
data = response.json()['exercises']


##saving data from exercise api
# save_file = open("savedata.json", "w")
# json.dump(value, save_file, indent = 6)
# save_file.close()
# DON'T RUN ABOVE BLOCK

# ## importing data json file
#
# with open("./savedata.json") as file:
#     data = json.load(file)['exercises']

EXERCISE_NAME = data[0]['user_input']
EXERCISE_DURATION = data[0]['duration_min']
EXERCISE_CALORIES = data[0]['nf_calories']
DATE = dt.strftime(dt.now(), "%d/%m/%Y")
TIME = dt.strftime(dt.now(), "%H:%M:%S")

print(EXERCISE_DURATION, EXERCISE_CALORIES, EXERCISE_NAME)

body = {
    "workout": {"date": DATE,
                "time": TIME,
                "exercise": EXERCISE_NAME.title(),
                "duration": EXERCISE_DURATION,
                "calories": round(EXERCISE_CALORIES,0)

                }
}

headers = {
    "Authorization": SHEETY_TOKEN
}
print(body)


response = requests.post(SHEETY_ENDPOINT, json=body, headers=headers)
print(response.raise_for_status())
print(response.json())
