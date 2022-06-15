from aiogram import types, Dispatcher
from telegram import create_bot


async def start(message: types.Message):
    await create_bot.bot.send_message(message.chat.id, 'Hello! I will translate any massage to any language')


def reg_handlers_client(dp: Dispatcher):
    dp.message_handler(start, commands=['start', 'help'])
