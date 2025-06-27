from agents import Agent, Runner
from blaxel.openai import bl_model, bl_tools

from agentmail import AgentMail, Message
from markdown import markdown


async def agent(message: Message):
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

    result = await Runner.run(agent, message.model_dump_json())

    client = AgentMail()

    client.inboxes.messages.reply(
        inbox_id=message.inbox_id,
        message_id=message.message_id,
        html=markdown(result.final_output),
    )

    return result.final_output
