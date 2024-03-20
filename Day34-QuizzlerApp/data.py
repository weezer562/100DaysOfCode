import requests


class Data:
    def __init__(self):
        self.question_data = get_questions()


def get_questions():
    parameters = {
        "amount": 30,
        "type": "boolean",
        "catagory": 18
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]
