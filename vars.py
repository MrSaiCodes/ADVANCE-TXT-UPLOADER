
from os import environ

API_ID = int(environ.get("API_ID", "22410340"))  # API ID
API_HASH = environ.get("API_HASH", "633122e0c3b0100c2ec829e8a52e6a51")  # API HASH
BOT_TOKEN = environ.get("BOT_TOKEN", "7921256918:AAEswo_iUwYYvJFaRK-rcVXgU8youFWc7b4")  # Bot Token
OWNER_ID = int(environ.get("OWNER_ID", "662494886"))  # Telegram User ID
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./downloads")  # Default download location
TG_MAX_FILE_SIZE = int(environ.get("TG_MAX_FILE_SIZE", "2000000000"))  # Max file size for Telegram uploads
