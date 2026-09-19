import telegram
import asyncio
import os
from telegram.ext import Application

from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

TOKEN = os.getenv("TOKEN")
USER_ID = os.getenv("USER_ID")

async def sendIP(ipAddr):
    application = Application.builder().token(TOKEN).build()

    await application.initialize()
    await application.bot.send_message(
        chat_id=USER_ID,
        text=ipAddr
    )
    await application.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
