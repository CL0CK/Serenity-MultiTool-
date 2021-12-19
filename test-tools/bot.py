import modules.config as config
import telebot
import sys
sys.path.insert(1, '/C:/Users/CL0CK/Desktop/cv-ks')

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, message.chat.id)


bot.polling(none_stop=True)
