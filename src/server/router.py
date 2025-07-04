import os

from blaxel.telemetry.span import SpanManager
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from agentmail import AgentMail, Message
from svix.webhooks import Webhook, WebhookVerificationError

from agent import agent


BLAXEL_WORKSPACE = os.getenv("BLAXEL_WORKSPACE")
INBOX_USERNAME = os.getenv("INBOX_USERNAME")


client = AgentMail()

inbox = client.inboxes.create(
    username=INBOX_USERNAME,
    display_name="DocBot",
    client_id="docbot-inbox",
)

webhook = client.webhooks.create(
    url=f"https://run.blaxel.ai/{BLAXEL_WORKSPACE}/docbot/email",
    event_types=["message.received"],
    inbox_ids=[inbox.inbox_id],
    client_id="docbot-webhook",
)


router = APIRouter()


class RequestInput(BaseModel):
    inputs: str


@router.post("/")
async def handle_request(request: RequestInput):
    with SpanManager("blaxel-openai").create_active_span("agent-request", {}):

        async def response_stream():
            yield f"""This agent is made to be used with email, powered by AgentMail\n
Configure with an API key from https://agentmail.to\n
Then email the agent at {INBOX_USERNAME}@agentmail.to"""

        return StreamingResponse(response_stream(), media_type="text/event-stream")


class EmailInput(BaseModel):
    message: Message


@router.post("/email")
async def handle_email(request: Request):
    wh = Webhook(webhook.secret)

    try:
        verified = wh.verify(await request.body(), request.headers)

        with SpanManager("blaxel-openai").create_active_span("agent-request", {}):
            return await agent(Message(**verified["message"]))
    except WebhookVerificationError:
        raise HTTPException(status_code=401)
