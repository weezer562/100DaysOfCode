import datetime as dt
import os
import random
import smtplib

from dotenv import load_dotenv

load_dotenv('../creds.env')


def get_quote():
    with open("quotes.txt", encoding='UTF8') as quotes:
        data = quotes.readlines()
        choice = random.choice(data)
        return choice


def send_email():
    my_email = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASSWORD")
    to_email = os.getenv("YAHOO_EMAIL")

    quote = get_quote()
    message = f"Subject:Quote of the day\n\n{quote}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=message)


now = dt.datetime.now()

if now.weekday() == 0:
    send_email()
