import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.AuthToken = os.getenv("AuthToken")
        self.account_sid = os.getenv("account_sid")

    def send_message(self, price,
                     departure_Airport_IATA_Code,
                     arrival_Airport_IATA_Code,
                     outbound_Date,
                     inbound_Date):
        client = Client(username=self.account_sid, password=self.AuthToken)
        message = client.messages.create(from_='+19252737310',
                                         to='+919141143670',
                                         body=f"- Low Price Alert! Only ₹{price} to fly from {departure_Airport_IATA_Code}"
                                              f" to {arrival_Airport_IATA_Code}, on {outbound_Date} until {inbound_Date}. ", )
        print(message.status)
        if message.status == 200:
            print("successfully sent")
        else:
            print("not sent")
