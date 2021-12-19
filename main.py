import pyautogui
import datetime
import time
from os import X_OK
from random import randint

import modules.config as config
import modules.launcher as launcher
import modules.utilities as utilities
import modules.tele as tele


@tele.bot.message_handler(commands=['start'])
def welcome(message):
    if(config.TELEGRAM_MESSAGES):
        try:
            tele.bot.send_message(
                message.chat.id, config.GREETING_MESSAGE)
        except Exception:
            if(config.DEBUG_MESSAGES):
                print("TG_EX")


if __name__ == "__main__":
    for i in range(config.LAPS):
        pyautogui.FAILSAFE = False
        currentAcc = config.START_FROM
        failCounter = 0
        pauseAcc = -1

        # Welcome message in tg bot
        startTime = tele.welcomeMessage()

        app = launcher.openApp()

        loginsFile = open('logins.txt', 'r')
        logins = [line.strip() for line in loginsFile]

        while currentAcc < config.NUMBER_OF_ACCOUNTS:
            print(logins[currentAcc])
            if(config.TELEGRAM_MESSAGES):
                try:
                    tele.bot.send_message(config.TELEGRAM, "Захожу на " +
                                          logins[currentAcc])
                except Exception:
                    if(config.DEBUG_MESSAGES):
                        print("TG_EX")

            # Click in ScreenCenter
            if(config.CLICK_CENTER_IN_4GAME):
                try:
                    pyautogui.getWindowsWithTitle("4game")[0].maximize()
                except Exception:
                    print("Can't Maximize (")
                utilities.click(
                    config.SCREEN_CENTER_X_Y[0], config.SCREEN_CENTER_X_Y[1])
                pyautogui.hotkey("alt", "q")
            # Check with 1sec
            time.sleep(2)

            try:
                launcher.inputLogin(app, logins[currentAcc])
            except Exception:
                launcher.closeApp(config.GAME_PROCESS_NAME)
                launcher.closeApp(config.LAUNCHER_PROCESS_NAME)
                app = launcher.openApp()
                continue
            try:
                launcher.inputPassword(app)
            except Exception:
                if(config.DEBUG_MESSAGES):
                    print("inputPassword Fail")
                if(config.TELEGRAM_MESSAGES):
                    try:
                        tele.bot.send_message(
                            config.TELEGRAM, "inputPassword Fail")
                    except Exception:
                        if(config.DEBUG_MESSAGES):
                            print("TG_EX")
                launcher.closeApp(config.GAME_PROCESS_NAME)
                launcher.closeApp(config.LAUNCHER_PROCESS_NAME)
                app = launcher.openApp()
                continue

            try:
                launcher.pressSignIn(app)
            except Exception:
                if(config.DEBUG_MESSAGES):
                    print("pressSignIn Fail")
                if(config.TELEGRAM_MESSAGES):
                    try:
                        tele.bot.send_message(
                            config.TELEGRAM, "pressSignIn Fail")
                    except Exception:
                        if(config.DEBUG_MESSAGES):
                            print("TG_EX")
                launcher.closeApp(config.GAME_PROCESS_NAME)
                launcher.closeApp(config.LAUNCHER_PROCESS_NAME)
                app = launcher.openApp()
                continue

            # Select BNS in 4game (hypelink0)
            if(config.SELECT_BNS_IN_4GAME):
                try:
                    app.Hyperlink0.click_input()
                except Exception:
                    print("EXCEPTION HYPERLINK0")
                    launcher.closeApp(config.GAME_PROCESS_NAME)
                    launcher.closeApp(config.LAUNCHER_PROCESS_NAME)
                    continue
            try:
                currentAcc = launcher.startGame(app, currentAcc)
            except Exception:
                if(config.DEBUG_MESSAGES):
                    print("startGame Fail")
                if(config.TELEGRAM_MESSAGES):
                    try:
                        tele.bot.send_message(
                            config.TELEGRAM, "startGame Fail")
                    except Exception:
                        if(config.DEBUG_MESSAGES):
                            print("TG_EX")
                launcher.closeApp(config.GAME_PROCESS_NAME)
                launcher.closeApp(config.LAUNCHER_PROCESS_NAME)
                app = launcher.openApp()
                continue

            launcher.closeApp(config.GAME_PROCESS_NAME)
            pyautogui.hotkey("alt", "q")
            time.sleep(1)
            # Short PAUSE
            if(config.SHORT_PAUSES):
                if (randint(1, 5) == 5):
                    pauseTime = (randint(63, 134))
                    if(config.DEBUG_MESSAGES):
                        print("Делаю короткую паузу после " + logins[currentAcc-1] +
                              " на " + str(pauseTime) + " секунд")
                    if(config.TELEGRAM_MESSAGES):
                        try:
                            tele.bot.send_message(config.TELEGRAM, "Делаю короткую паузу после " + logins[currentAcc-1] +
                                                  " на " + str(pauseTime) + " секунд")
                        except Exception:
                            if(config.DEBUG_MESSAGES):
                                print("TG_EX")
                    time.sleep(pauseTime)
            # Long PAUSE
            if(config.LONG_PAUSE):
                if (currentAcc+1) % config.LONG_PAUSE_ACCS == 0:
                    pauseAcc = randint(1, 5)
                if pauseAcc > 0:
                    pauseAcc = pauseAcc-1
                elif pauseAcc == 0:
                    pauseTime = (randint(240, 720))
                    if(config.DEBUG_MESSAGES):
                        print("Делаю паузу после " + logins[currentAcc-1] +
                              " на " + str(pauseTime) + " секунд")
                    if(config.TELEGRAM_MESSAGES):
                        try:
                            tele.bot.send_message(config.TELEGRAM, "Делаю паузу после " + logins[currentAcc-1] +
                                                  " на " + str(pauseTime) + " секунд")
                        except Exception:
                            if(config.DEBUG_MESSAGES):
                                print("TG_EX")
                    time.sleep(pauseTime)
                    pauseAcc = -1
        # Send Ending info in tg bot
        if(config.TELEGRAM_MESSAGES):
            endTime = datetime.datetime.now()
            difference = endTime - startTime
            seconds_in_day = 24 * 60 * 60
            datetime.timedelta(0, 8, 562000)
            try:
                tele.bot.send_message(config.TELEGRAM, "Вход в аккаунты успешно завершён\n" + endTime.strftime("%d/%m/%Y в %X за ") +
                                      str(difference.days * seconds_in_day + difference.seconds) + " секунд <3")
                tele.bot.send_sticker(
                    config.TELEGRAM, config.BOT_GOODBYE_STICKER)
            except Exception:
                if(config.DEBUG_MESSAGES):
                    print("TG_EX")
            tele.bot.polling(none_stop=True)
