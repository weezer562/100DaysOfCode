import json
import os
from pprint import pprint
import requests

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PROJECT_NAME = os.getenv("SHEETY_FLIGHT_PROJECT_NAME")
SHEETY_SHEET_NAME = os.getenv("SHEETY_FLIGHT_SHEET_NAME")


class DataManager:
    def __init__(self):
        self.sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

        self.sheety_headers = {
            "AUTHORIZATION": f"Bearer {SHEETY_TOKEN}"
        }

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        json_response = json.loads(response.text)

        return json_response

    def update_data(self, id, code):
        put_url = f"{self.sheety_endpoint}/{id}"

        flight_body = {
            "price": {
                "iataCode": code,
            }
        }

        response = requests.put(url=put_url, json=flight_body, headers=self.sheety_headers)
        pprint(response.text)
