import asyncio
import logging
import os
import signal

from aiogram import Router, types
from aiogram.filters import Command

from config import ADMIN_ID

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command("stop"))
async def cmd_stop(message: types.Message):
    """
    Команда для остановки бота с проверкой ключа\n
    Использование: /stop ваш_секретный_ключ
    """
        
    if message.from_user.id not in ADMIN_ID:
        await message.answer("Вы не являетесь авторизованным пользователем!")
        logging.warning(f"Попытка остановки от не авторизованного пользователя: {message.from_user.id}") 
        return
    
    elif message.from_user.id in ADMIN_ID:
        logging.info(f"Бот останавливается по команде пользователя: {message.from_user.id}") 
        try:
            await message.answer("Бот останавливается...")

            # Время на отправку сообщения
            await asyncio.sleep(1)

            # Завершаем процесс
            logging.info("Завершение работы...")
            os.kill(os.getpid(), signal.SIGTERM)
            
        except Exception as e:
            logging.error(f"Ошибка при остановке: {e}")
            await message.answer(f"Ошибка при остановке: {e}")
