import pyautogui
import time
import sys
import win32api
import cv2
import numpy as np
from random import randint

import modules.config as config
import modules.utilities as utilities
import modules.game as game
import modules.launcher as launcher
import modules.tele as tele


sys.path.insert(1, '/C:/Users/CL0CK/Desktop/cv-ks')


def startGame(app, currentAcc):
    failState = False
    playButtonFound = False
    app.Button.click()
    time.sleep(30)
    iterator = 0
    # Searching for PlayButton
    while iterator < config.FBS_ITER and failState == False and playButtonFound == False:
        time.sleep(0.5)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        small_image = cv2.imread('img/exit.png')
        large_image = image
        result = cv2.matchTemplate(
            small_image, large_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        iterator = iterator+1
        print("iterator = ", iterator)

        if(max_val > 0.95):
            if(config.DEBUG_MESSAGES):
                playButtonFound = True
                print("PlayButton found")
                for b in range(12):
                    pyautogui.press('enter')
                    pyautogui.press('enter')
                    time.sleep(0.3)

    if iterator == config.FBS_ITER and failState == False:
        print("Close on 1 (Searching for PlayButton)")
        if(config.TELEGRAM_MESSAGES):
            try:
                tele.bot.send_message(
                    config.TELEGRAM, "Close on 1 (Searching for PlayButton)")
            except Exception:
                if(config.DEBUG_MESSAGES):
                    print("TG_EX")
        launcher.closeApp(config.GAME_PROCESS_NAME)
        launcher.closeApp(config.LAUNCHER_PROCESS_NAME)
        return currentAcc
    iterator = 0
    # Searching player in game
    playerFound = False
    while playerFound == False and iterator < config.PIG_ITER and failState == False:
        pix = utilities.getPixelColor(config.XP_LINE_YELLOW_X_Y[0],
                                      config.XP_LINE_YELLOW_X_Y[1])
        pix2 = utilities.getPixelColor(config.XP_LINE_GREEN_X_Y[0],
                                       config.XP_LINE_GREEN_X_Y[1])
        pix3 = utilities.getPixelColor(config.XP_LINE_BLUE_X_Y[0],
                                       config.XP_LINE_BLUE_X_Y[1])
        time.sleep(0.5)
        iterator = iterator+1
        print("iterator = ", iterator)
        if ((pix[0] > config.XP_LINE_YELLOW_R_G_B[0]-10 and pix[0] < config.XP_LINE_YELLOW_R_G_B[0]+10 and pix[1] > config.XP_LINE_YELLOW_R_G_B[1]-10 and pix[1] < config.XP_LINE_YELLOW_R_G_B[1]+10 and pix[2] > config.XP_LINE_YELLOW_R_G_B[2]-10 and pix[2] < config.XP_LINE_YELLOW_R_G_B[2]+10)
            or (pix2[0] > config.XP_LINE_GREEN_R_G_B[0]-10 and pix2[0] < config.XP_LINE_GREEN_R_G_B[0]+10 and pix2[1] > config.XP_LINE_GREEN_R_G_B[1]-10 and pix2[1] < config.XP_LINE_GREEN_R_G_B[1]+10 and pix2[2] > config.XP_LINE_GREEN_R_G_B[2]-10 and pix2[2] < config.XP_LINE_GREEN_R_G_B[2]+10)
                or (pix3[0] > config.XP_LINE_BLUE_R_G_B[0]-10 and pix3[0] < config.XP_LINE_BLUE_R_G_B[0]+10 and pix3[1] > config.XP_LINE_BLUE_R_G_B[1]-10 and pix3[1] < config.XP_LINE_BLUE_R_G_B[1]+10 and pix3[2] > config.XP_LINE_BLUE_R_G_B[2]-10 and pix3[2] < config.XP_LINE_BLUE_R_G_B[2]+10)):
            playerFound = True
            print("Player in game found")
            currentAcc = currentAcc+1
            game.toDoList()
            print("currentAcc ", currentAcc)

    if iterator == config.PIG_ITER and failState == False:
        failState = True
        print("Close on 2 (Searching player in game)")
        if(config.TELEGRAM_MESSAGES):
            try:
                tele.bot.send_message(
                    config.TELEGRAM, "Close on 2 (Searching player in game)")
            except Exception:
                if(config.DEBUG_MESSAGES):
                    print("TG_EX")
        launcher.closeApp(config.GAME_PROCESS_NAME)
        launcher.closeApp(config.LAUNCHER_PROCESS_NAME)
        return currentAcc
    iterator = 0
    return currentAcc


def buyItem(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(1)
    pyautogui.click(x, y)
    time.sleep(2)
    pyautogui.press("y")
    time.sleep(2)
    pyautogui.press("y")


def expandInventory():
    pyautogui.press("i")
    time.sleep(1)
    for i in range(5):
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        method = cv2.TM_SQDIFF_NORMED

        small_image = cv2.imread('img/inventory.png')
        large_image = image

        result = cv2.matchTemplate(small_image, large_image, method)
        mn, _, mnLoc, _ = cv2.minMaxLoc(result)

        MPx, MPy = mnLoc

        trows, tcols = small_image.shape[:2]
        win32api.SetCursorPos((MPx+tcols, MPy+trows))
        time.sleep(1)
        utilities.click(MPx+tcols+130, MPy+trows)
        utilities.click(MPx+tcols+130, MPy+trows)
        time.sleep(1)
        pyautogui.press("y")
        time.sleep(1)


def findItemInF10():
    pyautogui.press("f10")
    time.sleep(2)

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread('img/lampinf10.png')
    large_image = image

    result = cv2.matchTemplate(small_image, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    MPx, MPy = mnLoc

    trows, tcols = small_image.shape[:2]
    win32api.SetCursorPos((MPx+tcols, MPy+trows))
    time.sleep(1)
    utilities.click(MPx+tcols+130, MPy+trows)

    time.sleep(1)
    pyautogui.press("y")
    time.sleep(1)
    # click(1731, 1057)
    time.sleep(1)


def findPartOfPost():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread('img/part.png')
    large_image = image

    result = cv2.matchTemplate(small_image, large_image, method)

    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    MPx, MPy = mnLoc
    trows, tcols = small_image.shape[:2]
    xRand = randint(MPx, MPx+tcols)
    yRand = randint(MPy, MPy+trows)
    utilities.click(xRand, yRand)
    utilities.click(xRand, yRand)

    time.sleep(1)


def lampInPost():
    # LAMP TO TAKE FROM POST
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread('img/lamptotake.png')
    large_image = image
    result = cv2.matchTemplate(small_image, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc

    trows, tcols = small_image.shape[:2]

    utilities.click(MPx, MPy)
    time.sleep(1)
    utilities.click(MPx, MPy+530)
    time.sleep(1)
    pyautogui.press("y")
    time.sleep(4)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("i")
    time.sleep(1)


def useInvItem():
    # INVENTORY LAMP
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("i")
    time.sleep(1)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread(config.INV_ITEM_IMG)
    large_image = image
    result = cv2.matchTemplate(small_image, large_image, method)

    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    MPx, MPy = mnLoc

    trows, tcols = small_image.shape[:2]
    xRand = randint(MPx, MPx+tcols)
    yRand = randint(MPy, MPy+trows)
    utilities.click(xRand, yRand)
    utilities.click(xRand, yRand)
    utilities.click(xRand, yRand)
    utilities.click(xRand, yRand)
    time.sleep(1)
    pyautogui.press("y")
    time.sleep(2)


def toDoList():
    time.sleep(3)

    if config.INV_EXPAND:
        print("expandInventory")
        expandInventory()

    if config.INV_ITEM_TAKE:
        print("findItemInF10")
        findItemInF10()

        print("findPartOfPost")
        findPartOfPost()

        print("lampInPost")
        lampInPost()

    if config.INV_ITEM_USE:
        print("useInvItem")
        useInvItem()

    if config.BOT_SEND_SCREENS:
        image = pyautogui.screenshot(
            r'C:\Users\CL0CK\Desktop\cv-ks\temp.png')
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        print("Sending photo")
        tele.bot.send_photo(config.TELEGRAM, photo=open('temp.png', 'rb'))
