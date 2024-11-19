from dotenv import load_dotenv, dotenv_values
import telebot
from telebot import types
import os
import logging

load_dotenv()

# @see https://habr.com/ru/companies/wunderfund/articles/683880/
logging.basicConfig(
        level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    #  filename="py_log.log", filemode="w",
)
#  logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
#  logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
#                      format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger('tg-bot')

#  logger.setLevel(logging.DEBUG)
#  console = logging.StreamHandler()
#  console.setLevel(level=logging.DEBUG)
#  formatter =  logging.Formatter('%(levelname)s : %(message)s')
#  console.setFormatter(formatter)
#  logger.addHandler(console)

logger.debug('An INFO')

# @see https://pypi.org/project/python-dotenv/
config = dotenv_values('.env')

test = os.environ.get('DOMAIN')
test2 = os.getenv('DOMAIN')

bot = telebot.TeleBot('6213167835:AAGFNszkOHnxk03D1F7UtHsw-H_NMfb2AAo')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(
            message.from_user.id, 'Привет, чем я могу тебе помочь?'
        )
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши "Привет"')
    else:
        bot.send_message(
            message.from_user.id, 'Я тебя не понимаю. Напиши /help.'
        )


bot.infinity_polling()
#  bot.polling(none_stop=True, interval=0)
