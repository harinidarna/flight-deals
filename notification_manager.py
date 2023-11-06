from twilio.rest import Client

ACCOUNT_ID = "AC6c0cc819c25b0fb4821d22988a71557e"
AUTH_TOKEN = "46917cea2fae606237fc1e5b5b5e3587"
CLIENT = Client(ACCOUNT_ID, AUTH_TOKEN)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, message):
        message = CLIENT.messages.create(
            from_='+12516168643',
            body=message,
            to='+919866115715'
        )
        print(message.sid)
