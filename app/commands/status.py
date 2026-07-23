"""Handler for the /status command."""

import logging
import platform
import time

import psutil
from telegram import Update
from telegram.ext import ContextTypes

import platform


from app.security.auth import owner_only

logger = logging.getLogger(__name__)


def get_system_status() -> str:
    """Collect system performance metrics and system details.

    Returns:
        Formatted multi-line status report.
    """

    cpu_percent = psutil.cpu_percent(interval=None)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    uptime_seconds = max(0, int(time.time() - psutil.boot_time()))
    uptime_hours = uptime_seconds // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60

    hostname = platform.node()
    os_name = platform.system()
    os_release = platform.release()
    python_ver = platform.python_version()

    return (
        "🟢 WatchTower Online\n\n"
        f"Host Name: {hostname}%\n"
        f"🖥 CPU Usage: {cpu_percent}%\n"
        f"🧠 Memory Usage: {ram_percent}%\n"
        f"💾 Disk Usage: {disk_percent}%\n\n"
        f"⏱ Uptime: {uptime_hours}h {uptime_minutes}m\n\n"
        f"🐍 Python: {python_ver}\n"
        f"💻 OS: {os_name} {os_release}"
    )


@owner_only
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /status Telegram command.

    Collects and replies with current system status and performance metrics.

    Args:
        update: Incoming Telegram update.
        context: Callback context provided by python-telegram-bot.
    """
    user = update.effective_user
    user_id = user.id if user else "Unknown"
    username = user.username if user and user.username else "N/A"

    logger.info("Received /status command from user_id=%s, username=%s", user_id, username)

    status_message = get_system_status()

    if update.message:
        await update.message.reply_text(status_message)
