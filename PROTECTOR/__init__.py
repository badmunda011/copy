from pyrogram import Client
from telethon import TelegramClient
from telegram.ext import Application
import config

# Pyrogram Bot Client (With Bot Token)
app = Client(
    name="PROTECTOR1", 
    api_id=config.API_ID, 
    api_hash=config.API_HASH, 
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="PROTECTOR.Modules")
)

# Telethon Bot Client (With Bot Token)
bot = TelegramClient(
             session="PROTECTOR2", 
             api_id=config.API_ID, 
             api_hash=config.API_HASH
             ).start(bot_token=config.BOT_TOKEN)


# Telegram (python-telegram-bot) Client
application = Application.builder().token(config.BOT_TOKEN).build()

plugins = dict(root="PROTECTOR.Modules")
