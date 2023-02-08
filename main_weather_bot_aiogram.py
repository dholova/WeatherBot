import requests
import datetime
import const
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from smiles import code_to_smile

bot = Bot(token=const.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.reply('Напиши назву міста і я тобі надішлю прогноз погоди')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(const.WEATHER_URL.format(city=message.text, token=const.WEATHER_TOKEN))
        data = r.json()
        city = data['name']
        country = data['sys']['country']
        cur_weather = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Подивись у вікно, не розумію, яка зараз погода'
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\nПогода в місті: {city}, {country}\n'
              f'Температура: {cur_weather}С° {wd}\nВологість:{humidity}%\nТиск:{pressure} мм.рт.ст\n'
              f'Вітер: {wind}\nСхід сонця: {sunrise_timestamp}\n Захід сонця: {sunset_timestamp}\n'
              f'Протяжність дня {length_of_the_day}')
    except Exception as ex:
        print(ex)
        await message.reply('\U00002620 Перевірте назву міста \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
