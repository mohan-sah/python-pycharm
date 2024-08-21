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

