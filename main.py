import logging
from aiogram import executor
from create_bot import dp
from handlers import client, other

logging.basicConfig(level=logging.INFO)


client.reg_handlers_client(dp)
other.reg_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
