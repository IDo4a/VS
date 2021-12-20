import requests
import datetime
from config import tg_bot_weather, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_weather)
dp = Dispatcher(bot)

@dp.message_handler(commands=["Start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю тебе сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
         "Clear": "Ясно \U00002600",
         "Clouds": "Облачно \U00002601",
         "Rain": "Дождь \U00002614",
         "Drizzle": "Дождь \U00002614",
         "Thunderstone": "Гроза \U000026A1",
         "Snow": "Снег \U0001F328",
         "Mist": "Туман \U0001F32B"
   }

    try:
      r = requests.get(
         f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
      )
      data = r.json()

      city = data["name"]
      cur_weathet = data["main"]["temp"]

      weather_description = data["weather"][0]["main"]
      if weather_description in code_to_smile:
         wd = code_to_smile[weather_description]
      else:
         wd = "Посмотри в окно."   

      humidity = data["main"]["humidity"]
      pressure = data["main"]["pressure"]
      wind = data["wind"]["speed"]
      sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
      sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

      await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
      f"Погода в городе: {city}\nТемпература: {cur_weathet}C° {wd}\n"
      f"Влажность: {humidity}%\nДавление: {pressure}\nСкорость ветра: {wind}м/с\n"
      f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}")

    except:
      await message.reply("\U0001F914 Проверьте название города \U0001F914")

if __name__ == '__main__':
    executor.start_polling(dp)