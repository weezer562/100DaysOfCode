import datetime
import os

import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now().strftime("%Y%m%d")
add_config = {
    "date": today,
    "quantity": input("How many Kilometers did you cycle today? "),
}

response = requests.post(url=add_pixel_endpoint, json=add_config, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240319"

put_config = {
    "quantity": "4453.53"
}

# response = requests.put(url=update_endpoint, json=put_config, headers=headers)

#DELETE
# response = requests.delete(url=update_endpoint, headers=headers)

print(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html")
