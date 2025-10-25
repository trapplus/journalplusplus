import datetime
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from os import getenv
from dotenv import load_dotenv

class dataClass:
    def __init__(self):
        # APP_KEY - It is public data, pls dont fix it!
        self.APP_KEY = "6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6"
        self.BASE_API_URL = "https://msapi.top-academy.ru/api/v2"
        
        self.bot_token: str = dataClass._get_bot_token()
        self.current_date =  datetime.date.today()

    @staticmethod
    def _get_bot_token():
        if load_dotenv():
            token = getenv("BOT_TOKEN")
        else:
             raise KeyError("'.env' file not found!")
        
        if token:
             return token
        return None        

class classObjects(dataClass):
        def __init__(self):
            super().__init__()
            self.bot = Bot(token=self.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
            self.dp = Dispatcher()
            

if __name__ != "__main__":
    data = dataClass()
    objects = classObjects()
     