# Message Sender Script

This Python script allows you to send messages to a specific URL endpoint via HTTP POST requests. The script includes a simple method for sending a single message and a commented-out section for spamming the endpoint with continuous messages. It uses the `requests` library for making HTTP requests and the `terminut` logging module for logging success or failure of the message delivery.

---

## Features

- **Single Message Sending**: Send a single, customized message to the desired endpoint.
- **Spam Messages**: (Optional) Enable repeated sending of messages by uncommenting the spam block.
- **Customizable Content**: Easily configure the message content, authorization headers, and target URL.
- **Logging Support**: Logs success and failure of message delivery for better monitoring.

---

## Requirements

- Python 3.6 or later
- Libraries:
  - `requests`: For sending HTTP POST requests.
  - `terminut`: For logging messages.

Install the required libraries using:
```bash
pip install requests terminut

