from blaxel.telemetry.span import SpanManager
from fastapi import APIRouter
from pydantic import BaseModel

from agent import agent

router = APIRouter()


class RequestInput(BaseModel):
    inputs: str


@router.post("/")
async def handle_request(request: RequestInput):
    with SpanManager("blaxel-openai").create_active_span("agent-request", {}):
        return await agent(request.inputs)
