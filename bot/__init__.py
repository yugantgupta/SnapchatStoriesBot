import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "22233521"))
    API_HASH = os.environ.get("API_HASH", "dfad40fe3665377983903737cc05cfbc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8835044269:AAFfq38RKm7KONKwGZ9Du8cVqlG9eVgRYko")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Saveme091_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
