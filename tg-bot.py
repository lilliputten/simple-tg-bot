import telebot
from telebot import types
bot = telebot.TeleBot('6213167835:AAGFNszkOHnxk03D1F7UtHsw-H_NMfb2AAo')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши "Привет"')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')

bot.infinity_polling()
#  bot.polling(none_stop=True, interval=0)
