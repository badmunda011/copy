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

# Start all bots
def start_bots():
    # Start Pyrogram Bot
    print("[INFO] Starting Pyrogram bot...")
    app.start()

    # Start Telethon Bot
    print("[INFO] Starting Telethon bot...")
    bot.start()

    # Start Telegram Application
    print("[INFO] Starting Telegram Application...")
    application.run_polling()

if __name__ == "__main__":
    start_bots()
