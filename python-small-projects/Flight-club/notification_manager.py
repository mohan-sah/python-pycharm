import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.
load_dotenv()
class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_emails(self,receive_mail, message_body):
        MY_EMAIL = "mohansah944@gmail.com"
        RECEIVE_EMAIL = receive_mail
        MY_PASS = ""
        MSG = message_body

        try:
            with open(file="passkey.txt") as passkey:
                MY_PASS = passkey.read()  # "owsf zfcf emwg lsre" <- need passkey from sender's mai
        except FileNotFoundError:
            print("need a txt file with passkey: "
                  "which look like this : 'owsf zfcf emwg lsre' \n"
                  "and you will get from sender's account- security-generate passkey")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            print("inside2")
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=RECEIVE_EMAIL,msg=f"Subject: FLIGHT CLUB \n\n{MSG}" )
            print(f"sended to {RECEIVE_EMAIL}")


#