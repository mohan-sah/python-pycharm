import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class EmailNotificationManager:
    def __init__(self):
        self.MY_PASS = os.environ["MY_PASS"]
        self.MY_EMAIL = os.environ["MY_EMAIL"]

    def send_email(self, receive_email="mohansahsmtp@gmail.com", product_title = "product_title", current_price = "current_price", link_to_buy = "link_to_buy"):

        MESSAGE = f"{product_title.strip()} is now {current_price} , buy at {link_to_buy}"

        msg = MESSAGE
        from_ = self.MY_EMAIL
        to_ = receive_email
        subject = 'Amazon Price Tracker'
        fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}'

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MY_PASS)
            # connection.sendmail(from_addr=self.MY_EMAIL, to_addrs=RECEIVE_EMAIL,
            #                     msg=f"Subject: Amazon Price Tracker\n\n{MESSAGE}")
            connection.sendmail(to_, from_, fmt.format(to_, from_, subject, msg).encode('utf-8'))
            print(f"sended to {receive_email}: {MESSAGE}")

    def send_html_email(self, receive_email="mohansahsmtp@gmail.com", product_title = "product_title", current_price = "current_price", link_to_buy = "link_to_buy"):
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

        # Email setup
        msg = MIMEMultipart()
        msg['From'] = self.MY_EMAIL
        msg['To'] = receive_email
        msg['Subject'] = 'Amazon Price Tracker'

        # Attach the HTML content
        msg.attach(MIMEText(html_content, 'html'))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MY_PASS)
            connection.sendmail(from_addr=self.MY_EMAIL, to_addrs=receive_email, msg=msg.as_string())
            print(f"Sent to {receive_email}: {product_title.strip()} is now {current_price}, buy at {link_to_buy}")
