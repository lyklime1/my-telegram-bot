from aiogram import types, Dispatcher
from create_bot import bot


async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Hello! I will translate any massage to any language')


def reg_handlers_client(dp: Dispatcher):
    dp.message_handler(start, commands=['start', 'help'])
