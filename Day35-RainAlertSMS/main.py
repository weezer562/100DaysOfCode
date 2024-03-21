import json
import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

MY_LAT = 33.7701
MY_LONG = 118.1937

# Test rain location
# MY_LAT = 35.58
# MY_LONG = -98.45

TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.getenv("TWILIO_SID")

load_dotenv('../creds.env')

api_key = os.getenv("OPEN_WEATHER_API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

json_response = json.loads(response.text)

weather_list = json_response["list"]

my_twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
my_number = os.getenv("MY_NUMBER")

for value in weather_list:
    if value["weather"][0]["id"] < 700:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body="Looks like rain, Cover up!!",
                from_=my_twilio_number,
                to=my_number
            )
        print(message.status)

        break

