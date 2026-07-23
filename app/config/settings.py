"""Application configuration loading and validation for WatchTower."""

import os
from pathlib import Path

from dotenv import load_dotenv


class Settings:
    """Load and validate WatchTower configuration from environment variables."""

    def __init__(self) -> None:
        """Load the project environment file and initialize configuration values."""
        dotenv_path = Path(__file__).resolve().parents[2] / ".env"
        load_dotenv(dotenv_path=dotenv_path)

        self.bot_token: str = self._get_required_value("BOT_TOKEN")
        self.owner_id: int = self._get_owner_id()
        self.log_level: str = self._get_log_level()

    @staticmethod
    def _get_required_value(name: str) -> str:
        """Return a required non-empty environment value.

        Args:
            name: Name of the required environment variable.

        Raises:
            ValueError: If the environment variable is missing or empty.
        """
        value = os.getenv(name)
        if not value:
            raise ValueError(f"Required configuration variable {name} is missing.")
        return value

    def _get_owner_id(self) -> int:
        """Load OWNER_ID and convert it to an integer.

        Raises:
            ValueError: If OWNER_ID is missing or cannot be converted to an integer.
        """
        owner_id = self._get_required_value("OWNER_ID")
        try:
            return int(owner_id)
        except ValueError as error:
            raise ValueError("Configuration variable OWNER_ID must be an integer.") from error

    @staticmethod
    def _get_log_level() -> str:
        """Load and validate LOG_LEVEL, defaulting to INFO.

        Raises:
            ValueError: If LOG_LEVEL is not a supported Python logging level.
        """
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        valid_levels = {
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        }
        if log_level not in valid_levels:
            raise ValueError(
                "Configuration variable LOG_LEVEL must be one of: "
                "DEBUG, INFO, WARNING, ERROR, CRITICAL."
            )
        return log_level


settings = Settings()
