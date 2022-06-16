import pytesseract
import translators as ts
from PIL import Image
from create_bot import bot
from os import remove
from aiogram import types, Dispatcher


async def get_text_messages(message: types.message):
    await message.answer(ts.google(message.text, from_language='auto', to_language='ru'))


async def get_photo_messages(message: types.message):
    file_id = message.photo[-1].file_id
    name = file_id + ".jpg"
    file = await bot.get_file(file_id)
    await bot.download_file(file_path=file.file_path, destination=name)
    img = Image.open(name)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lida_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    result = pytesseract.image_to_string(img)
    await message.answer(result)
    await message.answer(ts.google(result, from_language='auto', to_language='ru'))
    remove(name)


def reg_handlers_other(dp: Dispatcher):
    dp.register_message_handler(get_text_messages, content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(get_photo_messages, content_types=types.ContentTypes.PHOTO)
