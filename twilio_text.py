# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Set environment variables for your credentials
# Read more at http://twil.io/secure

def send_message(to, from_who, message_body):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=from_who,
        to=to
    )
    print(message.sid)
