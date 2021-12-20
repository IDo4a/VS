import requests
import datetime
from config import tg_bot_exchange
from aiogram import Bot, types, Dispatcher, executor


bot = Bot(token=tg_bot_exchange)
dp = Dispatcher(bot)

@dp.message_handler(commands=["Start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю тебе сводку погоды!")

@dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.text)

if __name__ == '__main__':
  executor.start_polling(dp)
