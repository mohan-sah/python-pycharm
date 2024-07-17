##################### Hard Starting Project ######################
import random
import smtplib

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
import pandas as pd
import datetime as dt
from random import choice
import os

MY_EMAIL = "mohansah944@gmail.com"
RECEIVE_EMAIL = "mohansahsmtp@yahoo.com"
MY_PASS = ""
try:
    with open(file="../passkey.txt") as passkey:
        MY_PASS = passkey.read() # "owsf zfcf emwg lsre" <- need passkey from sender's mai
except FileNotFoundError:
    print("need a txt file with passkey: "
          "which look like this : 'owsf zfcf emwg lsre' \n"
          "and you will get from sender's account- security-generate passkey")


now  = dt.datetime.now()
letter_data = "" #letter data
present_day = now.day
present_month = now.month
present_birthday = []


try:
    file = pd.read_csv(filepath_or_buffer="birthdays.csv")
except FileNotFoundError:
    print("add a birthday.csv file in format: name,email,year,month,day\n"
            "Test,test@email.com,1961,12,21")
else:
    birthday = pd.DataFrame(file)
    for (index,row) in birthday.iterrows():
        if row.month == present_month and row.day == present_day:
            present_birthday.append([row.person_name,row.email])

        print(present_birthday)
    print(birthday)

    for i in present_birthday:
        RECEIVE_EMAIL = i[1]
        with open(file=f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter_data = file.read().replace("[NAME]", f"{i[0]}",1)
            print(letter_data)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=RECEIVE_EMAIL,
                                    msg=f"subject: HAPPY BIRTHDAY!! \n\n {letter_data}")








# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



