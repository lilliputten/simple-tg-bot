import os
from background import keep_alive
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time

bot = telebot.TeleBot('6213167835:AAGFNszkOHnxk03D1F7UtHsw-H_NMfb2AAo')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши "Привет"')
    elif message.text == '/echo':
        bot.send_message(message.from_user.id,message.text)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')

keep_alive()

bot.infinity_polling()
#  bot.polling(none_stop=True, interval=0)
