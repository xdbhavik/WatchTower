"""Authentication module for WatchTower command handlers."""

from functools import wraps
import logging
from typing import Any, Callable, Coroutine

from telegram import Update
from telegram.ext import ContextTypes

from app.config.settings import settings

logger = logging.getLogger(__name__)

# Type alias for async Telegram command handler functions
CommandHandlerType = Callable[[Update, ContextTypes.DEFAULT_TYPE], Coroutine[Any, Any, Any]]


def owner_only(func: CommandHandlerType) -> CommandHandlerType:
    """Decorator to enforce that only the configured owner can execute a command.

    Args:
        func: Async command handler function to wrap.

    Returns:
        Wrapped command handler function.
    """
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Any:
        user = update.effective_user
        user_id = user.id if user else None
        username = user.username if user and user.username else "N/A"

        if user_id != settings.owner_id:
            logger.warning(
                "Unauthorized command execution attempt by user_id=%s, username=%s",
                user_id,
                username,
            )
            if update.message:
                await update.message.reply_text("Unauthorized.")
            return None

        return await func(update, context)

    return wrapper
