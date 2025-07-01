# Blaxel Demo

## DocBot

DocBot is an email assistant for developers. It is capable of answering technical queries based on up-to-date documentaion. You can email it at `docbot@agentmail.to`.

## Deploy

To deploy DocBot using Blaxel, simply configure the following environment variables:

```env
INBOX_USERNAME=      # a unique username for your DocBot's inbox
BLAXEL_WORKSPACE=    # the name of your Blaxel workspace
OPENAI_API_KEY=      # your OpenAI API key
AGENTMAIL_API_KEY=   # your AgentMail API key
```

Then run `bl deploy` and email your DocBot.
