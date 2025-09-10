import asyncio
import logging
import logging.config
import sys
import time
from os import getenv

import httpx
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers.dev.dev_commutator import commutator as dev_cm
from handlers.main.main_commutator import commutator as main_cm
from config import LOGGING_CONFIG

load_dotenv()

# Bot token 
TOKEN = getenv("botapikey")

# All handlers should be attached to the Router 
dp = Dispatcher()

#include_commutator
dp.include_router(main_cm)
dp.include_router(dev_cm)


async def main() -> None:
    # Initialize Bot instance 
    bot = Bot(
        token=TOKEN,  # type: ignore
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.config.dictConfig(LOGGING_CONFIG)
    logging.debug("AIOGRAM::Hi! Log write in log.app and stdout!")
    asyncio.run(main())
    
