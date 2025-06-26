from agents import Agent, Runner
from blaxel.openai import bl_model, bl_tools

from markdown import markdown


async def agent(input: str):
    tools = await bl_tools(["context7"])
    model = await bl_model("gpt-4o-mini")

    agent = Agent(
        name="docs-agent",
        model=model,
        tools=tools,
        instructions="""You are a helpful developer email assistant.
You will receive an email from a developer.
Your task is respond to the email in a friendly and helpful manner.

If the developer asks a technical question, use the context7 tools to retieve the relevant documentation.
First use the context7 resolve-library-id tool to resolve the relevant library id.
Then use the context7 get-library-docs tool to retrieve the relevant documentation.

Finally, respond to the developer as if you are writing an email.
Generate markdown and include relevant hyperlinks to the documentation.
Do not specify the email subject, only the email body.
Do not include any other text in your response.
""",
    )

    result = await Runner.run(agent, input)
    return markdown(result.final_output)
