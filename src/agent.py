from typing import AsyncGenerator

from agents import Agent, RawResponsesStreamEvent, Runner, function_tool
from blaxel.openai import bl_model, bl_tools
from openai.types.responses import ResponseTextDeltaEvent


@function_tool()
async def weather(city: str) -> str:
    """Get the weather in a given city"""
    return f"The weather in {city} is sunny"


async def agent(input: str) -> AsyncGenerator[str, None]:
    tools = await bl_tools(["blaxel-search"]) + [weather]
    model = await bl_model("sandbox-openai")

    agent = Agent(
        name="blaxel-agent",
        model=model,
        tools=tools,
        instructions="You are a helpful assistant.",
    )
    result = Runner.run_streamed(agent, input)
    async for event in result.stream_events():
        if isinstance(event, RawResponsesStreamEvent) and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            yield event.data.delta
