from aiogram import Bot, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from os import getenv
from dotenv import load_dotenv


class dataClass:
    def __init__(self):
        self.bot_token: str = dataClass._get_bot_token()
        self.APP_KEY  : str = "6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6"
    
    @staticmethod
    def _get_bot_token():
        load_dotenv()
        token = getenv("BOT_TOKEN")
        if token:
             return token
        return None        

data = dataClass()


class classObjects(dataClass):
        def __init__(self):
            super().__init__()
            self.bot = Bot(token=self.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

objects = classObjects()
