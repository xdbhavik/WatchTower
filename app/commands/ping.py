"""Handler for the /ping command."""

import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.security.auth import owner_only

logger = logging.getLogger(__name__)


@owner_only
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /ping Telegram command.

    Replies with 'Pong!' and logs command details including user ID and username.

    Args:
        update: Incoming Telegram update.
        context: Callback context provided by python-telegram-bot.
    """
    user = update.effective_user
    user_id = user.id if user else "Unknown"
    username = user.username if user and user.username else "N/A"

    logger.info("Received /ping command from user_id=%s, username=%s", user_id, username)

    if update.message:
        await update.message.reply_text("Pong!")
