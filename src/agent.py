from typing import AsyncGenerator

from agents import Agent, RawResponsesStreamEvent, Runner
from blaxel.openai import bl_model, bl_tools
from openai.types.responses import ResponseTextDeltaEvent


async def agent(input: str) -> AsyncGenerator[str, None]:
    tools = await bl_tools(["context7"])
    model = await bl_model("sandbox-openai")

    agent = Agent(
        name="docs-agent",
        model=model,
        tools=tools,
        instructions="You are a helpful developer assistant. You can answer questions about any documentation. Use context7 to get the relevant documentation and answer the user's query.",
    )
    result = Runner.run_streamed(agent, input)
    async for event in result.stream_events():
        if isinstance(event, RawResponsesStreamEvent) and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            yield event.data.delta
