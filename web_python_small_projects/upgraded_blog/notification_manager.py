import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
  border-radius: 5px;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

img {
  border-radius: 5px 5px 0 0;
}

.container {
  padding: 2px 16px;
}
</style>
</head>
<body>

<h2>Round Card</h2>

<div class="card">
  <img src="https://www.vecteezy.com/vector-art/2454057-man-faceless-profile" alt="Avatar" style="width:100%">
  <div class="container">
    <h4><b>Jane Doe</b></h4> 
    <p>Interior Designer</p> 
  </div>
</div>

</body>
</html> """

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
        MY_PASS = os.environ["MY_PASS"]
        MSG = message_body
        with smtplib.SMTP("smtp.gmail.com") as connection:

            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=RECEIVE_EMAIL,msg=MSG )
            print(f"sended to {RECEIVE_EMAIL}")



    def send_html_email(self, receive_email="mohansahsmtp@gmail.com"):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        # Example values
        product_title = product_title
        current_price = "$99.99"
        link_to_buy = link_to_buy
        receive_email = receive_email

        # HTML content for the email
        html_content = f"""
        <html>
          <body>
            <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHlkZGI4czV3eHR2Zng4ejA4Z2V6cjQ2NWpyMjQ5Y3UyNW9haHk1MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Dmz31oe42yacpyVDWU/giphy.gif" alt="Animated GIF" />

            <p>{product_title.strip()} is now {current_price},💲👇⬇️📉 buy at <a href="{link_to_buy}">this link</a>.</p>
            <p>Check out the image below:</p>
            <img src="https://appbrewery.github.io/instant_pot/assets/images/71QFLNzx2-L._AC_SX679_.jpg" width="500" height="500" alt="Instant Pot Image" />
          </body>
        </html>
        """
        html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
  border-radius: 5px;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

img {
  border-radius: 5px 5px 0 0;
}

.container {
  padding: 2px 16px;
}
</style>
</head>
<body>

<h2>Round Card</h2>

<div class="card">
  <img src="https://www.vecteezy.com/vector-art/2454057-man-faceless-profile" alt="Avatar" style="width:100%">
  <div class="container">
    <h4><b>{}</b></h4> 
    <p>Interior Designer</p> 
  </div>
</div>

</body>
</html> """
        # Email setup
        msg = MIMEMultipart()
        msg['From'] = self.MY_EMAIL
        msg['To'] = receive_email
        msg['Subject'] = 'Amazon Price Tracker'

        # Attach the HTML content
        msg.attach(MIMEText(html, 'html'))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MY_PASS)
            connection.sendmail(from_addr=self.MY_EMAIL, to_addrs=receive_email, msg=msg.as_string())
            print(f"Sent to {receive_email}: {product_title.strip()} is now {current_price}, buy at {link_to_buy}")
