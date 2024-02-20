import datetime as dt
import os
import random
import sys
import smtplib

import pandas as pd

MY_EMAIL = "Gabomaster@outlook.com"
MESSAGE = """Subject:Hello World!\n\n
Das ist eine Testnachricht.

Mit freundlichen Gruessen,
ich selbst
"""

letter_templates = []
for file in os.listdir("letter_templates"):
    if "letter" in file:
        with open(f"letter_templates/{file}") as fl:
            letter_templates.append(fl.read())
today = dt.date.today()


def send_email():
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.starttls()

        connection.login(user=MY_EMAIL, password="smietki24")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="gabriel.remiszewski@outlook.de", msg=MESSAGE)


def has_birthday(person: pd.Series) -> bool:
    global today
    try:
        birthday = dt.datetime(day=person.day, month=person.month, year=person.year)
    except KeyError:
        print("Cannot find birthday in pandas Series", file=sys.stderr)

    return birthday.day == today.day and birthday.month == today.month


def send_birthday_email(person: pd.Series) -> None:
    global letter_templates
    letter: str = random.choice(letter_templates)
    letter = "Subject:Birthday!\n\n" + letter.replace("[NAME]", person["name"])

    try:
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password="smietki24")
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"], msg=letter)
    except:
        print(f"Cannot send email to {person["name"]}", file=sys.stderr)
    else:
        print(f"Successfully sent email to {person['name']}")


def check_for_birthdays():

    birthday_data: pd.DataFrame = pd.read_csv("birthdays.csv")

    for person in birthday_data.iterrows():
        if has_birthday(person[1]):
            send_birthday_email(person[1])


if __name__ == "__main__":
    check_for_birthdays()
