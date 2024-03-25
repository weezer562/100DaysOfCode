import os
import smtplib

import requests
from bs4 import BeautifulSoup

GMAIL_USERNAME = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
URL = (f"https://www.amazon.com/dp/B0BSGH355C/?coliid=I2O51IYASC82M5&colid=2YPJ08JS741L4&psc=1&ref_"
       f"=list_c_wl_lv_ov_lig_dp_it")
BUY_PRICE = 89.99

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")

price = soup.find_all(class_="a-offscreen")[3].get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_USERNAME,
            to_addrs=GMAIL_USERNAME,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
