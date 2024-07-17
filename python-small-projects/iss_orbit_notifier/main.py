import time

import requests
from datetime import datetime as dt
import smtplib

MY_EMAIL = "mohansah944@gmail.com"
RECEIVE_EMAIL = "mohansahsmtp@yahoo.com"
MY_PASS = ""
try:
    with open(file="passkey.txt") as passkey:
        MY_PASS = passkey.read()  # "owsf zfcf emwg lsre" <- need passkey from sender's mai
except FileNotFoundError:
    print("need a txt file with passkey: "
          "which look like this : 'owsf zfcf emwg lsre' \n"
          "and you will get from sender's account- security-generate passkey")

LATITUDE = 12.971599
LONGITUDE = 77.594566


def is_iss_nearby():
    response = requests.get("http://api.open-notify.org/iss-now.json#")
    print(response.status_code)
    response.raise_for_status()

    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']["latitude"])

    iss_position = (longitude, latitude)
    if ((LATITUDE - 5 >= iss_position[1] >= LATITUDE + 5) and
            (LONGITUDE - 5 >= iss_position[1] >= LONGITUDE + 5)):
        return True
    else:
        return False


def still_dark():
    parameters = {"lat": LATITUDE,
                  "lng": LONGITUDE,
                  "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hr = int(data["results"]['sunrise'].split("T")[1].split(":")[0])
    sunset_hr = int(data["results"]['sunset'].split("T")[1].split(":")[0])
    time_now_hr = dt.now().hour
    if time_now_hr in range(sunrise_hr, sunset_hr):
        return True
    else:
        return False


while True:
    time.sleep(60) #how long does iss take to orbit earth = 90min
    if still_dark() and is_iss_nearby():
    # if True:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVE_EMAIL,
                                msg=f"Subject: Iss in NIGHT SKY\n\nThe iss is above you into the night sky")
            print(f"sended to {RECEIVE_EMAIL}")
