"""Logging configuration for WatchTower."""

import logging


def configure_logging(log_level: str) -> None:
    """Configure application logging with the requested severity level.

    Args:
        log_level: Valid Python logging level name from application settings.
    """
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
