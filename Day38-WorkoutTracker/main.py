import json
import os
from datetime import datetime

import requests

APP_ID = os.getenv("NUTRIX_APP_ID")
API_KEY = os.getenv("NUTRIX_API_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PROJECT_NAME = os.getenv("SHEETY_PROJECT_NAME")
SHEETY_SHEET_NAME = os.getenv("SHEETY_SHEET_NAME")

WEIGHT = 100.00
HEIGHT = 185.00
AGE = 25

nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

exercise_config = {
    "query": input("What did you do today? "),
    "age": AGE,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT
}

headers = {
    "X-APP-ID": APP_ID,
    "X-APP-KEY": API_KEY,
    'CONTENT-TYPE': 'application/json'
}

response = requests.post(url=nutrix_endpoint, json=exercise_config, headers=headers)
json_response = json.loads(response.text)

sheety_headers = {
    "AUTHORIZATION": f"Bearer {SHEETY_TOKEN}"
}

for exercise in json_response["exercises"]:
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.time().strftime("%I:%M:%S %p")

    sheety_body = {
        "workout": {
            "date": date,
            "time": str(time),
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response_post = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_body)

response = requests.get(url=sheety_endpoint, headers=sheety_headers)
