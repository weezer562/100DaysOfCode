from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

flight_code = ""

if sheet_data["prices"][0]["iataCode"] == "":
    for row in sheet_data:
        flight_code = flight_search.get_code(row["city"])
        row["iataCode"] = flight_code
    data_manager.destination_data = sheet_data
    data_manager.update_data(id=1, code=flight_code)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data["prices"]:
    flight = flight_search.search_flights(to_code=flight_code)
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            mess=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
