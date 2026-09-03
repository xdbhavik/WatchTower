# WatchTower

WatchTower is a self-hosted, privacy-first remote monitoring and home security system written in Python.

It runs as a local agent on a laptop and is controlled through Telegram. The system is designed around modularity, security, asynchronous operations, and easy extensibility.

## Features

- 🤖 Telegram bot control
- 🔐 Owner-only command authorization
- 📷 Remote webcam capture
- 📊 System status monitoring
- 📝 Configurable application logging
- ⚙️ Environment-based configuration
- 🧩 Modular and extensible architecture

## Tech Stack

- Python 3.12+
- python-telegram-bot
- python-dotenv
- psutil
- OpenCV

## Project Structure

```text
WatchTower/
├── app/
│   ├── bot/          # Telegram bot
│   ├── commands/     # Bot commands
│   ├── camera/       # Camera functionality
│   ├── config/       # Configuration
│   ├── security/     # Authentication
│   ├── utils/        # Utilities
│   └── main.py       # Entry point
├── tests/            # Tests
├── logs/             # Application logs
├── .env.example      # Environment template
├── requirements.txt  # Dependencies
├── PROJECT_SPEC.md   # Project specification
└── README.md