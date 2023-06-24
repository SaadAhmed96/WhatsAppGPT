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


def send_message(incoming_msg, client, human_whatsapp_number, twilio_whatsapp_number):
    """
    Sends a message using the Twilio Messaging API.

    Args:
        incoming_msg (str): The incoming message to be sent.
        client (Twilio Client): The Twilio client object used for sending messages.
        human_whatsapp_number (str): The recipient's WhatsApp number.
        twilio_whatsapp_number (str) : Your Twilio-provided WhatsApp number.

    Returns:
        None
            This function does not return any value.
    """
    model_response = get_gpt_response(incoming_msg)

    message = client.messages.create(
        from_=twilio_whatsapp_number,
        body=model_response,
        to=human_whatsapp_number,
    )

    return
