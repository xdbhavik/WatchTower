"""Handler for the /photo command."""

import asyncio
import logging
from telegram import Update
from telegram.ext import ContextTypes

from app.camera.capture import capture_image
from app.security.auth import owner_only

logger = logging.getLogger(__name__)


@owner_only
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /photo Telegram command.

    Captures an image using the webcam and sends it to the user.

    Args:
        update: Incoming Telegram update.
        context: Callback context provided by python-telegram-bot.
    """
    user = update.effective_user
    user_id = user.id if user else "Unknown"
    username = user.username if user and user.username else "N/A"

    logger.info("Received /photo command from user_id=%s, username=%s", user_id, username)

    if not update.message:
        return

    try:
        image_path = await asyncio.to_thread(capture_image)
        with open(image_path, "rb") as photo_file:
            await update.message.reply_photo(photo=photo_file, caption="📷 Photo captured")
        logger.info("Successfully sent photo %s to user_id=%s", image_path, user_id)
    except Exception as e:
        logger.error("Error capturing or sending photo: %s", e, exc_info=True)
        await update.message.reply_text(f"❌ Failed to capture photo: {e}")
