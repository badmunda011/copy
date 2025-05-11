import asyncio
import importlib
from pyrogram import idle
from PROTECTOR import PROTECTOR, application
from PROTECTOR.modules import ALL_MODULES
import nest_asyncio

nest_asyncio.apply()

# Replace this with your actual Telegram group/channel/user ID
LOGGER_ID = -1002625181470

# Create an event loop
loop = asyncio.get_event_loop()

async def JARVIS():
    # Import all modules dynamically
    for all_module in ALL_MODULES:
        importlib.import_module("PROTECTOR.modules." + all_module)

    print("Bot Started Successfully")

    # Initialize the Telegram (python-telegram-bot) client
    await application.initialize()  # Initialize Application
    await application.start()       # Start Application

    # Notify LOGGER_ID about bot deployment
    try:
        await PROTECTOR.send_message(
            LOGGER_ID,
            "**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ ʏᴏᴜʀ ʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅ \n ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ  [JARVIS](https://github.com/badmunda011)**"
        )
    except Exception as e:
        print(f"Failed to send message to LOGGER_ID: {e}")

    # Keep the bot running
    await idle()

    print("Shutting Down Bot...")
    await application.shutdown()   # Shutdown Application
    print("Bot Shutdown Successfully")

if __name__ == "__main__":
    try:
        loop.run_until_complete(JARVIS())
    except Exception as e:
        print(f"Error starting the bot: {e}")
