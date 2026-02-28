# BusNotifier
Posts upcoming bus times to Slack

## Usage
### Run locally
```
uv run --env-file=.env main.py
```

### Run with Docker
```
docker build -t bus-notifier .
docker run --rm --env-file .env bus-notifier
```

## Environment Variables
1. Copy the example env file and fill in your values:
```
cp .env.example .env
```
2. Update the variables in `.env` with your values.
