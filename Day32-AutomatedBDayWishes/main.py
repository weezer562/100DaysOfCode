import os
import random
import smtplib
import time
from datetime import datetime

import pandas
from dotenv import load_dotenv

TIME_INTERVAL = 60 * 60 * 24

load_dotenv("../creds.env")


def check_birthdays():
    data = pandas.read_csv("birthdays.csv").to_dict(orient="records")

    for person in data:
        month = person["month"]
        day = person["day"]

        today = datetime.today()

        if month == today.month and day == today.day:
            send_email(person["name"], person["email"])

    # Sleep 24 hours
    time.sleep(TIME_INTERVAL)
    check_birthdays()


def get_template(name):
    """Returns one of 3 available templates"""
    choice = random.randint(1, 3)
    with open(f"letter_templates/letter_{choice}.txt", "r") as file:
        lines = file.readlines()
        template = ''.join(lines)

        update_template = template.replace("[NAME]", name)

        subject = "Subject:HappyBirthday\n\n"

        return f"{subject}{update_template}"


def send_email(name, email):
    my_email = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASSWORD")

    message = get_template(name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=message)


check_birthdays()
