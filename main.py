import telebot

bot = telebot.TeleBot('5414940662:AAHldK9P55Wn4HR60-pM2J04VlvYEutgMHY')


@bot.message_handler(content_types=['text', 'document'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
