##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas
import datetime as dt
import smtplib
import os

my_gmail_email = os.environ.get("my_gmail_email")
my_gmail_password = os.environ.get("my_gmail_password")

my_outlook_email = os.environ.get("my_outlook_email")
my_outlook_password = os.eviron.get("my_outlook_password")

today = dt.datetime.now()

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
today_birthday = [birthday_dict for birthday_dict in birthdays if birthday_dict["month"] == today.month and birthday_dict["day"] == today.day]

if not today_birthday == []:
    random_letter_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file=random_letter_file, mode="r") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", today_birthday[0]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail_email, password=my_gmail_password)
        connection.sendmail(from_addr=my_gmail_email, to_addrs=my_outlook_email, msg=f"Subject:Birthday!\n\n{letter_content}")
