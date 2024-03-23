from datetime import datetime, timedelta
import json
import os

import requests
from flight_data import FlightData

TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    def __init__(self):
        self.tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.tequila_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.headers = {
            "apikey": os.getenv("TEQUILA_API_KEY"),
            "accept": "application/json"
        }

    def get_code(self, city_name):
        params = {
            "term": city_name,
            "local": "en-US",
            "location_types": "airport",
            "active_only": True,
            "limit": 1
        }

        response = requests.get(url=self.tequila_endpoint, headers=self.headers, params=params)
        json_response = json.loads(response.text)
        return json_response["locations"][0]["code"]

    def search_flights(self, to_code):

        now = datetime.now()
        date_now_string = now.strftime("%d/%m/%Y")

        six_months = now + timedelta(days=180)
        six_months_string = six_months.strftime("%d/%m/%Y")

        params = {
            "fly_from": "LON",  # code
            "fly_to": to_code,
            "max_stopovers": 0,
            "date_from": date_now_string,  # now to 6 months from now
            "date_to": six_months_string,
            "nights_in_dst_from": 7,  # sample 03/04/2021
            "nights_in_dst_to": 28,
            "curr": "USD",
            "sort": "price",
            "limit": 1
        }

        response = requests.get(url=self.tequila_search_endpoint, headers=self.headers, params=params)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
