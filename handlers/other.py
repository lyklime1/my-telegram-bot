import pytesseract
import translators as ts
from PIL import Image
from create_bot import bot
from os import remove
from aiogram import types, Dispatcher


async def get_text_messages(message: types.message):
    await bot.send_message(message.chat.id, ts.google(message.text, from_language='auto', to_language='ru'))


async def get_photo_messages(message: types.message):
    raw = message.photo[2].file_id
    name = raw + ".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = Image.open(name)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lida_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    result = pytesseract.image_to_string(img)
    await bot.send_message(message.from_user.id, result)
    await bot.send_message(message.from_user.id, ts.google(result, from_language='auto', to_language='ru'))
    remove(name)


def reg_handlers_other(dp: Dispatcher):
    dp.message_handler(get_text_messages, content_types=['text'], commands=[])
    dp.message_handler(get_photo_messages, content_types=['photo'])
