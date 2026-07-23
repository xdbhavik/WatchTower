"""Application entry point for WatchTower."""

import logging

from app.bot.telegram_bot import create_application, register_handlers
from app.config.settings import settings
from app.utils.logger import configure_logging


def main() -> None:
    """Initialize WatchTower and run the Telegram bot polling loop.

    Raises:
        Exception: Re-raises unexpected startup or runtime failures after logging them.
    """
    configure_logging(settings.log_level)
    logger = logging.getLogger(__name__)
    logger.info("Starting WatchTower.")

    try:
        application = create_application(settings.bot_token)
        register_handlers(application)
        application.run_polling()
    except KeyboardInterrupt:
        logger.info("Shutdown requested by user.")
    except Exception:
        logger.exception("WatchTower encountered an unexpected error.")
        raise
    finally:
        logger.info("WatchTower shutdown complete.")


if __name__ == "__main__":
    main()
