
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import CommandStart

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Қош келдің! Бұл — қыздарға арналған мотивациялық күнделік. /kundelik деп жазып, алғашқы бетпен таныс.")

@dp.message_handler(commands=["help"])
async def send_help(message: types.Message):
    await message.reply("/start - Кіріспе\n/kundelik - Мотивациялық бет\n/gulmenkun - Гүл мен Күн айдары\n/quote - Қанатты сөз")

@dp.message_handler(commands=["quote"])
async def send_quote(message: types.Message):
    await message.reply("“Сен – өзіңнің ең үлкен тірегің!” – Фариза Оңғарсынова")

@dp.message_handler(commands=["gulmenkun"])
async def send_gulmenkun(message: types.Message):
    await message.reply("Бүгінгі Гүл: “Сен – өзіңе сенім сыйлаған жансың.”\nКүн: “Өзіңе мотивациялық хат жаз.”")

@dp.message_handler(commands=["kundelik"])
async def send_kundelik(message: types.Message):
    await message.reply("Бет 1 – “Менің ішкі әлемім”\nНазира: “Жанымды жалаңаштап, күнге жайдым...”\nТапсырма: Өз ішкі даусыңа бір сұрақ қой да, соған жауап жаз.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
