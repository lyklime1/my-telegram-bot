from aiogram import Bot, Dispatcher
from os import getenv


bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)
