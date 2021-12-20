from requests.api import get
from config import open_weather_token
from pprint import pprint
import requests
import datetime

def get_weather(city,open_weather_token):

@dp.message_handler()
   async def get_exchange(message: types.Message):
     code_to_smile = {
         "Euro": "EUR \U0001F4B6",
         "Dollar": "USD \U0001F4B5",
         "RUB": "RUR \U000020BD",
         "Bitcoin": "BIT \U000020BF",
    }

   try:
      r = requests.get(
         f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
      )
      data = r.json()
      pprint(data)

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

      print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
      f"Погода в городе: {city}\nТемпература: {cur_weathet}C° {wd}\n"
      f"Влажность: {humidity}%\nДавление: {pressure}\nСкорость ветра: {wind}м/с\n"
      f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}")

   except Exception as ex:
      print(ex)
      print("Проверьте название города")
      

def main():
   city = input("Введите город: ")
   get_weather(city,open_weather_token)

if __name__ == '__main__':
   main()
