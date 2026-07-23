# WatchTower

## Overview

WatchTower is a self-hosted, privacy-first remote monitoring and home security system written in Python.

The project runs as a local agent on a laptop. It is controlled exclusively through Telegram. The laptop never relies on cloud services other than Telegram for messaging.

The owner can remotely send authenticated commands to the laptop. Depending on the command, the laptop may capture images, stream video, send system status, transfer files, or perform other monitoring tasks.

The project is designed for maintainability, security, modularity, and extensibility rather than quick implementation.

---

# Goals

Primary goals:

- Modular architecture
- Strong separation of concerns
- Easy to extend
- Secure command execution
- Async-first design
- Production-quality code
- Type hints everywhere
- Good logging
- Minimal global state

---

# Current Phase

We are currently implementing Phase 1.

Only implement the features requested.

Do NOT implement future phases unless explicitly asked.

---

# Technology Stack

Language:
- Python 3.12+

Libraries:
- python-telegram-bot
- python-dotenv
- psutil

Future libraries will be introduced later.

---

# Architecture

watchtower/

app/

bot/
- Telegram connection
- Register handlers
- Receive updates

commands/
- Individual command implementations
- One file per command when appropriate

config/
- Environment loading
- Validation
- Configuration classes

security/
- Authentication
- Authorization
- Future encryption

utils/
- Logging
- Helper functions

main.py
- Application entry point

logs/

tests/

requirements.txt

README.md

.env

---

# Design Rules

Follow these rules strictly.

## 1.

Business logic must never exist inside Telegram handlers.

Handlers should only:

- validate request
- call command
- send response

Nothing more.

---

## 2.

Configuration must only come from config/settings.py.

Never hardcode:

- tokens
- owner IDs
- paths
- constants

---

## 3.

Everything should be asynchronous whenever supported.

Prefer async/await.

Do not introduce blocking operations unless necessary.

---

## 4.

Use Python logging.

Never use print() for application logs.

---

## 5.

Write code that is easy to test.

Avoid hidden dependencies.

---

## 6.

Every public function should include:

- type hints
- docstrings

---

## 7.

Keep files focused.

Avoid giant files.

---

## Phase 1 Features

Implement only:

- Telegram bot initialization
- Config loading
- Logging
- Authentication using OWNER_ID
- /ping command
- /status command

Do NOT implement:

- Webcam
- Screenshots
- Streaming
- Audio
- Encryption
- Scheduling
- AI
- Motion detection

unless explicitly requested.

---

# Authentication

Every command must verify

effective_user.id == OWNER_ID

before execution.

Unauthorized users must receive an appropriate message or be ignored.

---

# Logging

Log:

- startup
- shutdown
- every command
- authentication failures
- errors

---

# Coding Style

Prefer:

small functions

clear naming

single responsibility

composition over inheritance

no unnecessary abstraction

---

# Responses

When implementing code:

- Explain architecture briefly.
- Write complete production-quality code.
- Preserve existing project structure.
- Avoid unnecessary dependencies.
- Do not rewrite unrelated files.