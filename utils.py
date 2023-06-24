import os
from model import get_gpt_response


def get_msg_details(req_data, debug=True):
    """
    Get message details from Twilio request data.

    Args:
        req_data (dict): The Twilio request data.
        debug (bool, optional): Whether to print debug information. Defaults to True.

    Returns:
        tuple: A tuple containing the incoming message, the human's WhatsApp number, and the Twilio WhatsApp number.
    """

    incoming_message = req_data["Body"]
    human_whatsapp_number = req_data["From"]
    twilio_whatsapp_number = req_data["To"]

    if debug:
        print(f"Incoming human message: {incoming_message}")
        print(f"The human_whatsapp_number is: {human_whatsapp_number}")
        print(f"The twilio_whatsapp_number is: {twilio_whatsapp_number}")

    return incoming_message, human_whatsapp_number, twilio_whatsapp_number


# Sending message logic through Twilio Messaging API
def send_message(incoming_msg, client, human_whatsapp_number, twilio_whatsapp_number):
    model_response = get_gpt_response(incoming_msg)

    message = client.messages.create(
        from_=twilio_whatsapp_number,
        body=model_response,
        to=human_whatsapp_number,
    )

    return
