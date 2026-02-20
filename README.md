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

## Secrets
1. Create a .env file with:
```
BUS_SLACK_WEBHOOK=
CTA_BUS_API_KEY=
NOTIFY_RT=
NOTIFY_STOP_NAME=
NOTIFY_STPID=
```
