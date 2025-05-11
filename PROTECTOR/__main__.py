import logging
import asyncio
import importlib
from PROTECTOR.modules import ALL_MODULES
from PROTECTOR import app, bot, application
from pyrogram import idle
import Config
import nest_asyncio

# Apply nest_asyncio to handle nested event loops
nest_asyncio.apply()

# Logger Handler
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Main Function
async def main():
    await app.start()
    await bot.start()
    await application.run_polling()
    await application.initialize()  # Initialize the Application
    await application.start()  # Start Telegram (python-telegram-bot) Client

    for all_module in ALL_MODULES:
        importlib.import_module("PROTECTOR.modules." + all_module)

    LOGGER("PROTECTOR.modules").info("Successfully Imported Modules...")
    LOGGER("PROTECTOR").info("Bot Started Successfully...")

    # Send message to Logger group
    try:
        await app.send_message(Config.LOGGER_ID, "✅ **Bot Started Successfully!**")
        LOGGER("PROTECTOR").info("Start message sent to LOGGER_ID.")
    except Exception as e:
        LOGGER("PROTECTOR").error(f"Failed to send start message: {e}")

    await idle()

    # Stop all clients properly
    await app.stop()
    await bot.disconnect()
    await application.shutdown()  # Shutdown Telegram (python-telegram-bot) Client

    LOGGER("PROTECTOR").info("Stopping Bot...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    
