import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint


Mails = ['dadadada@gmail.com', 'dadadada1@gmail.com']
Password = '3131134514512'


def registerFourGameAcc():
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver")
    driver.get('https://ru.4game.com/signup/')
    time.sleep(3)

    try:
        emailInput = driver.find_elements_by_class_name("Input__input__1t40v")
        emailInput[0].send_keys(Mails[x])
    except:
        regcherezemail = driver.find_elements_by_tag_name("a")
        regcherezemail[9].click()
        emailInput = driver.find_elements_by_class_name("Input__input__1t40v")
        emailInput[0].send_keys(Mails[x])

    passwordInput = driver.find_elements_by_class_name("Input__input__1t40v")

    passwordInput[1].send_keys(Password)

    checkBox = driver.find_elements_by_class_name(
        "Checkbox__control__3382v")
    checkBox[0].click()
    time.sleep(1)

    continueButton = driver.find_elements_by_tag_name("button")
    continueButton[1].click()
    continueButton[4].click()
    time.sleep(randint(10, 20))
    driver.close


for x in range(200):
    registerFourGameAcc()
