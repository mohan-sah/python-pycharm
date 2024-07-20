import requests
from twilio.rest import Client

LATITUDE = float(12.971599)
LONGITUDE = float(77.594566)
APIkey="3834e7bb91a4f4f38562524e4ef0cafa"
cityID = "bengaluru"

AuthToken="5ae3d74913260604ea2ccc67cf860d08"
account_sid = 'AC0b2cb719c76ef32a1470c79d02480c63'
auth_token = AuthToken


parameters = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "appid": APIkey,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()


data = response.json()
print(data)
will_rain = False
for i in range(4):
    id = data["list"][i]['weather'][0]['id']
    if int(id)<700:
        will_rain = True
        break
if will_rain: #sms
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+19252737310',
        to='+919141143670',
        body="it's going to rain today . Don't forget to carry ☂️ "
    )
    print(message.status)

if will_rain: #whatsapp
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today . Don't forget to carry ☂️",
        to = 'whatsapp:+919141143670'
    )
    print(message.status)

#🎉 Congratulations! You’ve got a Twilio phone number!
# +19252737310









