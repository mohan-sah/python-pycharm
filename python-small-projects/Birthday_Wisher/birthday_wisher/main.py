##################### Extra Hard Starting Project ######################
# hosted at https://www.pythonanywhere.com/user/mohansah/tasks_tab/
import datetime as dt
import pandas as pd
from random import randint
import smtplib
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

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today_tuple = (dt.datetime.now().day,dt.datetime.now().month)

data = pd.read_csv("birthdays.csv")

birthday_dict = {(row['day'],row.month): row for (index, row) in data.iterrows()}
print(birthday_dict)
if today_tuple in birthday_dict:
        birthday_person  = birthday_dict[today_tuple]

        file_path = f"./letter_templates/letter_{randint(1,3)}.txt"
        with open(file_path) as letter_file:
            content = letter_file.read().replace("[NAME]",birthday_person["person_name"])
            print(content)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],msg=f"Subject: Happy Birthday\n\n {content}") #🎂🎊🎁🎈
            print(f"sended to {birthday_person['email']}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




