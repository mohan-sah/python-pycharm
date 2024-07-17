import datetime as dt
import smtplib
from random import choice

# #date module try
#
# now = dt.datetime.now()
# year = now.year
# day_of_the_week = now.weekday()
# if year == 2024:
#     print(day_of_the_week)
# date_of_birthday = dt.datetime(year =2002 , month= 8, day=5)
# print(date_of_birthday)

# TODO:1. Use the datetime module to obtain the current day of the week.

MY_EMAIL = "mohansah944@gmail.com"
RECEIVE_EMAIL = "mohansahsmtp@yahoo.com"
MY_PASS = ""
try:
    with open(file="../passkey.txt") as passkey:

        MY_PASS = passkey.read() # "owsf zfcf emwg lsre" <- need passkey from sender's mail
        print(type(MY_PASS))
        MY_PASS = "odsfzjcfemoglsxe"
        print(type(MY_PASS))
        print(MY_PASS)
except FileNotFoundError:
    print("need a txt file with passkey: "
          "which look like this : 'owsf zfcf emwg lsre' \n"
          "and you will get from sender's account- security-generate passkey")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    # TODO:2. Open the quotes.txt file and obtain a list of quotes.
    with open(file="quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        # TODO:3. Use the random module to pick a random quote from your list of quotes.
        quotes_to_send = choice(quotes)
        print(quotes_to_send)

    # # TODO:4. Use the smtplib to send the email to yourself.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECEIVE_EMAIL,
                            msg=f"subject: MONDAY MOTIVATION \n\n {quotes_to_send}")
