import asyncio
import logging
import sys
import bot_events

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
router = Router()

bot_events.init(router)

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")