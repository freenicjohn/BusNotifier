# BusNotifier
Posts upcoming bus times to Slack

## Requirements
- Python 3.8+
- Slack API token
- OpenAI API key (or other LLM provider)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/tldr-slack.git
   cd tldr-slack
   ```
2. Install dependencies:
   ```sh
   uv sync
   ```

## Usage
1. Set your environment variables:
   - `TLDR_SLACK_WEBHOOK`
   - `OPENAI_API_KEY`
2. Run notifier:
   ```sh
   uv run --env-file=../.env main.py
   ```
