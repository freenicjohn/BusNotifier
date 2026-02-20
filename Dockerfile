FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app

# Set timezone to Central Time (America/Chicago)
RUN apk add --no-cache tzdata && \
	cp /usr/share/zoneinfo/America/Chicago /etc/localtime && \
	echo "America/Chicago" > /etc/timezone && \
	apk del tzdata

# Copy all project files
COPY . .

# Install dependencies using uv
RUN uv sync

# Run the app using uv, as in the README
CMD ["uv", "run", "main.py"]
