from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("25742938"))
API_HASH = getenv("b35b715fe8dc0a58e8048988286fc5b6")
BOT_TOKEN = getenv("7332934706:AAHke648XmOaIoqv-7gigzzmGrkp8acaff0")
BOT_USERNAME = getenv("Gcopyright_Bot")
OWNER_ID = int(getenv("7588172591"))
LOGGER_ID = int(getenv("-1002625181470"))
MONGO_URL = getenv("mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/")

SUDOERS = filters.user([443809517])
