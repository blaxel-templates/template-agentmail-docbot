import os

from blaxel.telemetry.span import SpanManager
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from agentmail import Message

from agent import agent


INBOX_USERNAME = os.getenv("INBOX_USERNAME")

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
async def handle_email(request: EmailInput):
    with SpanManager("blaxel-openai").create_active_span("agent-request", {}):
        return await agent(request.message)
