import os
import uvicorn
from fastapi import FastAPI, Request
from mangum import Mangum
from twilio.rest import Client
from utils import get_msg_details, send_message
from dotenv import load_dotenv

load_dotenv()

# get the important variable from .env file
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


# initialize the app
app = FastAPI()
handler = Mangum(app)


# create the twilio client to interact with Twilio platform
twilio_client = Client(account_sid, auth_token)


@app.post("/qa_response")
async def qa_bot(request: Request):
    form_data = await request.form()

    incoming_message, human_whatsapp_number, twilio_whatsapp_number = get_msg_details(
        req_data=form_data, debug=True
    )

    send_message(
        incoming_msg=incoming_message,
        human_whatsapp_number=human_whatsapp_number,
        twilio_whatsapp_number=twilio_whatsapp_number,
        client=twilio_client,
    )

    return ""


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
