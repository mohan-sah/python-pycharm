import requests
from datetime import datetime as dt
#uses pixela api for habit tracker

# note: pixela is well documented api

TOKEN = "la8970oij54d7rtfugyibu"
USERNAME = "mohansah"
GRAPH_ID = "graph1"

#UPDATE THE VALUE HERE FOR PUT,DELETE,POST REQUEST
YEAR = dt.now().year
MONTH = dt.now().month
DAY = dt.now().day


today = dt(year=YEAR,month=MONTH,day=DAY)
DATE = str(today.strftime(format='%Y%m%d'))


pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response =requests.post(url = pixela_endpoint, json= user_parameters)
# print(response.text)
# user created that's why commented : https://pixe.la/@mohansah


headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "kilometer",
    "type": "float",
    "color": "sora"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, headers=headers,json=graph_config)
# print(response.text)
# graph created: process completed and that's why commented

value_create_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
value_create_config = {
    "date": f"{DATE}",
    "quantity": input(f"how many km today: ")
}
response = requests.post(url=value_create_endpoint, headers=headers, json=value_create_config)
print(response.text)
# graph value updated hence commented


# Update a pixel
value_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
value_update_config = {
    "quantity" : "10"
}

# response = requests.put(url=value_update_endpoint, headers=headers, json=value_update_config)
# print(response.text)
# update request fullfilled and hence commented

# delete a pixel- Update date

# value_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
# response = requests.delete(url=value_delete_endpoint, headers=headers)
# print(response.text)







