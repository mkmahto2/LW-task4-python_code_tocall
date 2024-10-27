from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER,TO_PHONE_NUMBER

def make_call(to_phone_number, message_url="http://demo.twilio.com/docs/voice.xml"):
    # Initialize the Twilio client with account SID and auth token
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Make the call
    call = client.calls.create(
        to=to_phone_number,
        from_=TWILIO_PHONE_NUMBER,
        url=message_url  # This URL should point to TwiML XML or a Twilio demo URL
    )

    # Confirmation of the call
    print(f"Call initiated with SID: {call.sid}")

# Example Usage
to_number = TO_PHONE_NUMBER

make_call(to_number)  # Replace with the recipient's phone number
