import pyautogui
import time
from pywinauto import Desktop
from pywinauto.application import Application
import psutil
import modules.config as config


def openApp():
    app = Application(backend='uia').start(config.LAUCNHER_PATH)
    time.sleep(10)
    launcher = Desktop(backend='uia').window(title="4game")
    return launcher


def closeApp(appName):
    for proc in psutil.process_iter():
        if proc.name() == appName:
            proc.kill()


def inputLogin(app, login):
    loginField = app.Edit
    loginField.click_input()
    time.sleep(1)
    for char in login:
        print(char)
        pyautogui.press(char)


def inputPassword(app):
    passField = app.Edit2
    passField.click_input()
    for char in config.PASSWORD:
        print(char)
        pyautogui.press(char)


def pressSignIn(app):
    app.Button.click()
    time.sleep(2)
