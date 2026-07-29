"""Telegram application construction and handler registration."""

from telegram.ext import Application, ApplicationBuilder, CommandHandler

from app.commands.photo import photo
from app.commands.ping import ping
from app.commands.status import status


def create_application(bot_token: str) -> Application:
    """Create the Telegram application for the supplied bot token.

    Args:
        bot_token: Telegram bot API token.

    Returns:
        The configured Telegram application instance.
    """
    return ApplicationBuilder().token(bot_token).build()


def register_handlers(application: Application) -> None:
    """Register Telegram handlers with the application.

    Args:
        application: Telegram application receiving the handlers.
    """
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("photo", photo))

