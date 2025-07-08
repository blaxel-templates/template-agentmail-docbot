import logging
import os

from agentmail import AgentMail, Message
from blaxel.core import settings
from blaxel.telemetry.span import SpanManager
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from svix.webhooks import Webhook, WebhookVerificationError

from ..agent import agent

INBOX_USERNAME = os.getenv("INBOX_USERNAME")

logger = logging.getLogger(__name__)

client = AgentMail()

inbox = client.inboxes.create(
    username=INBOX_USERNAME,
    display_name="DocBot",
    client_id="docbot-inbox",
)
logger.debug(f"Inbox: id={inbox.inbox_id} username={INBOX_USERNAME}")

webhook = client.webhooks.create(
    url=f"https://run.blaxel.ai/{settings.workspace}/docbot/email",
    event_types=["message.received"],
    inbox_ids=[inbox.inbox_id],
    client_id="docbot-webhook",
)

logger.debug(f"Webhook: id={webhook.webhook_id}, url={webhook.url}")

router = APIRouter()


class RequestInput(BaseModel):
    inputs: str


@router.post("/")
async def handle_request(request: RequestInput):
    with SpanManager("blaxel-openai").create_active_span("agent-request", {}):

        async def response_stream():
            yield f"""This agent is made to be used with email, powered by AgentMail\n
Configure with an API key from https://agentmail.to\n
Then email the agent at {inbox.inbox_id}"""

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
