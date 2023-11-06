from twilio.rest import Client

ACCOUNT_ID = "YOUR TWILIO ACCOUNT ID"
AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
CLIENT = Client(ACCOUNT_ID, AUTH_TOKEN)

from_num = "YOUR TWILIO AUTHORIZED NUMBER"
to_num = "YOUR PHONE NUMBER"

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, message):
        message = CLIENT.messages.create(
            from_=from_num,
            body=message,
            to=to_num
        )
        print(message.status)
