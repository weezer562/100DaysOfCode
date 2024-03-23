import os

from twilio.rest import Client

TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.getenv("TWILIO_SID")


class NotificationManager:

    @staticmethod
    def send_sms(mess):
        my_twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
        my_number = os.getenv("MY_NUMBER")

        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=mess,
                from_=my_twilio_number,
                to=my_number
            )
        print(message.status)
