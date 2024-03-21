from datetime import datetime, timedelta
import itertools
import json
import os
from twilio.rest import Client

import requests

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.getenv("TWILIO_SID")

status = 0


def check_stock_diff():
    global status
    alpha_api_key = os.getenv("ALPHA_ADVANTAGE_API_KEY")
    num_days = 2

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": alpha_api_key,
        "datatype": "json"
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()

    json_response = json.loads(response.text)
    days_data = dict(itertools.islice(json_response["Time Series (Daily)"].items(), num_days))

    today = datetime.now()
    today_formatted = today.strftime("%Y-%m-%d")

    yesterday = today - timedelta(days=1)
    yesterday_formatted = yesterday.strftime("%Y-%m-%d")

    today_close = days_data[today_formatted]["4. close"]
    yesterday_close = days_data[yesterday_formatted]["4. close"]

    diff = 1 - abs(today_close / yesterday_close)
    if today_close > yesterday_close:
        status = "🔺"
    else:
        status = "🔻"

    return diff


def get_news(dec_change):
    news_api_key = os.getenv("NEWSAPI_API_KEY")

    parameters = {
        "q": f"{COMPANY_NAME}",
        "pageSize": 3,
        "page": 1,
        "apikey": news_api_key
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()

    json_response = json.loads(response.text)

    message = ""
    for index in range(3):
        message += (f"{STOCK}: {status}{dec_change*100}%\n{json_response["articles"][index]["title"]}\n"
                    f"Brief: {json_response["articles"][index]["description"]}")
        send_sms(message)


def send_sms(message):
    my_twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
    my_number = os.getenv("MY_NUMBER")

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body=message,
            from_=my_twilio_number,
            to=my_number
        )
    print(message.status)


change = check_stock_diff()
if change > .05:
    get_news(change)
