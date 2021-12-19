import telebot
import datetime
import modules.config as config

bot = telebot.TeleBot(config.TOKEN)


def welcomeMessage():
    # Welcome message in tg bot
    if(config.TELEGRAM_MESSAGES):
        startTime = datetime.datetime.now()
        try:
            bot.send_message(config.TELEGRAM, "Привет <3\nНачинаю вход на " + str(config.NUMBER_OF_ACCOUNTS) + " аккаунтов\n" +
                             startTime.strftime("%d/%m/%Y в %X"))
            bot.send_sticker(
                config.TELEGRAM, config.BOT_WELCOME_STICKER)
        except Exception:
            if(config.DEBUG_MESSAGES):
                print("TG_EX")
        return startTime
