from aiogram import types, Dispatcher


async def start(message: types.Message):
    await message.answer('Hello! I will translate any message to any language')


def reg_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
