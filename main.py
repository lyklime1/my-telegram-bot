import telebot
import translators as ts

bot = telebot.TeleBot('5414940662:AAHldK9P55Wn4HR60-pM2J04VlvYEutgMHY')


@bot.message_handler(content_types=['text', 'document'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, ts.google(message.text, from_language='auto', to_language='ru'))


bot.polling(none_stop=True, interval=0)
