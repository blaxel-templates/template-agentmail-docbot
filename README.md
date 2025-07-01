# Blaxel Demo

## DocBot

DocBot is an email assistant for developers. It is capable of answering technical queries based on up-to-date documentaion. You can email ours at `docbot@agentmail.to`.

## Deploy

To deploy DocBot using Blaxel, simply configure the following environment variables:

```env
BLAXEL_WORKSPACE=    # the name of your Blaxel workspace
INBOX_USERNAME=      # a unique username for your DocBot's inbox
AGENTMAIL_API_KEY=   # your AgentMail API key
```

Then run `bl deploy` and email your DocBot.
