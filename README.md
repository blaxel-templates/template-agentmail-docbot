# Email Assistant - AgentMail

<p align="center">
  <img style="border-radius:10px" src=".github/assets/cover.png" alt="AgentMail x Blaxel" width="90%"/>
</p>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-powered-brightgreen.svg)](https://openai.com/)
[![GPT-4](https://img.shields.io/badge/GPT--4-enabled-orange.svg)](https://openai.com/gpt-4)

</div>

DocBot is an intelligent email assistant designed for developers. It answers technical queries based on up-to-date documentation, making it an invaluable tool for development teams. You can email our demo instance at `docbot@agentmail.to`. 

This templates shows how to integrate agentic inbox provider AgentMail with Blaxel to create a customer success agent that autonomously handles technical questions via email (inbound and outbound).

## 📑 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Running Locally](#running-the-server-locally)
  - [Testing](#testing-your-agent)
  - [Deployment](#deploying-to-blaxel)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## ✨ Features

- **Email-based AI Assistant**: Receive and respond to technical queries via email
- **Documentation-focused**: Specialized in answering questions based on current documentation
- **OpenAI Assistants Integration**: Built on OpenAI Assistants API for sophisticated responses
- **AgentMail Integration**: Seamless email handling through AgentMail platform
- **Real-time Processing**: Streaming responses for efficient email communication
- **Tool Integration**: Support for additional tools like web search and documentation lookup
- **Developer-friendly**: Optimized for technical questions and development workflows

## 🚀 Quick Start

For those who want to get up and running quickly:

```bash
# Clone the repository
git clone https://github.com/blaxel-ai/template-agentmail-docbot.git

# Navigate to the project directory
cd template-agentmail-docbot

# Install dependencies
uv sync

# Configure environment variables
cp .env-sample .env
# Edit .env with your INBOX_USERNAME and AGENTMAIL_API_KEY

# Start the server
bl serve --hotreload

# In another terminal, test the agent
bl chat --local template-agentmail-docbot
```

## 📋 Prerequisites

- **Python:** 3.10 or later
- **[UV](https://github.com/astral-sh/uv):** An extremely fast Python package and project manager, written in Rust
- **AgentMail Account:** Sign up for AgentMail to get your API key
- **Blaxel Platform Setup:** Complete Blaxel setup by following the [quickstart guide](https://docs.blaxel.ai/Get-started#quickstart)
  - **[Blaxel CLI](https://docs.blaxel.ai/Get-started):** Ensure you have the Blaxel CLI installed. If not, install it globally:
    ```bash
    curl -fsSL https://raw.githubusercontent.com/blaxel-ai/toolkit/main/install.sh | BINDIR=/usr/local/bin sudo -E sh
    ```
  - **Blaxel login:** Login to Blaxel platform
    ```bash
    bl login YOUR-WORKSPACE
    ```

## 💻 Installation

**Clone the repository and install dependencies:**

```bash
git clone https://github.com/blaxel-ai/template-agentmail-docbot.git
cd template-agentmail-docbot
uv sync
```

## ⚙️ Configuration

Configure the following environment variables for your DocBot deployment:

```env
INBOX_USERNAME=      # a unique username for your DocBot's inbox
AGENTMAIL_API_KEY=   # your AgentMail API key
```

Create a `.env` file in the project root with these variables, or set them in your deployment environment.

## 🔧 Usage

### Running Locally

Start the development server with hot reloading:

```bash
bl serve --hotreload
```

For production run:

```bash
bl serve
```

_Note:_ The development server automatically restarts when you make changes to the source code.

### Testing

You can test your DocBot agent locally:

```bash
# Using the Blaxel CLI chat interface
bl chat --local template-agentmail-docbot
```

Example queries you can test:

```
How do I implement OAuth authentication in FastAPI?
```

```
What are the best practices for database migrations in Django?
```

```
Can you explain the difference between async and sync functions in Python?
```

You can also run it directly with specific input:

```bash
bl run agent docbot-agent --local --data '{"input": "How do I handle CORS in Express.js?"}'
```

### Deployment

When you are ready to deploy your DocBot:

```bash
bl deploy
```

This command uses your code and the configuration files under the `.blaxel` directory to deploy your DocBot on the Blaxel platform. Once deployed, users can email your DocBot at `{INBOX_USERNAME}@agentmail.to`.

## 📁 Project Structure

- **src/main.py** - Application entry point and FastAPI server setup
- **src/agent.py** - Core DocBot implementation with OpenAI Assistants integration
- **src/server/** - Server implementation and routing
  - **router.py** - API route definitions
  - **middleware.py** - Request/response middleware
  - **error.py** - Error handling utilities
- **pyproject.toml** - UV package manager configuration with dependencies
- **blaxel.toml** - Blaxel deployment configuration
- **.env.example** - Environment variables template
- **LICENSE** - MIT license file

## ❓ Troubleshooting

### Common Issues

1. **AgentMail Integration Issues**:
   - Verify your AgentMail API key is valid and active
   - Check that your inbox username is unique and available
   - Ensure webhook endpoints are properly configured
   - Test email delivery with the AgentMail dashboard

2. **Blaxel Platform Issues**:
   - Ensure you're logged in to your workspace: `bl login MY-WORKSPACE`
   - Verify models are available: `bl get models`
   - Check that functions exist: `bl get functions`


3. **Email Processing Problems**:
   - Check email parsing and response formatting
   - Verify email threading and conversation context
   - Monitor email delivery status and bounce rates
   - Review email content filtering and spam detection

4. **Python Environment Issues**:
   - Make sure you have Python 3.10+
   - Try `uv sync --upgrade` to update dependencies
   - Check for conflicting package versions
   - Verify virtual environment activation with UV

For more help, please [submit an issue](https://github.com/blaxel-templates/template-agentmail-docbot/issues) on GitHub.

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Submit** a Pull Request

Please make sure to update tests as appropriate and follow the code style of the project.

## 🆘 Support

If you need help with this template:

- [Submit an issue](https://github.com/blaxel-templates/template-agentmail-docbot/issues) for bug reports or feature requests
- Visit the [Blaxel Documentation](https://docs.blaxel.ai) for platform guidance
- Join our [Discord Community](https://discord.gg/G3NqzUPcHP) for real-time assistance

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
