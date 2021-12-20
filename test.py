import aiogram
from aiogram.types import reply_keyboard
import requests
import datetime
from config import tg_bot_exchange
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_exchange)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
     await reply_keyboard(row_widht=2)
     itembtn1 = aiogram.types.KeyboardButton('USD')
     itembtn2 = aiogram.types.KeyboardButton('EUR')
     itembtn3 = aiogram.types.KeyboardButton('RUR')
     itembtn4 = aiogram.types.KeyboardButton('BIT')
     

if __name__ == '__main__':
    executor.start_polling(dp)