from random import randint
import cv2
import pyautogui
import numpy as np
import time
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def findlampinf10():
    time.sleep(3)
    pyautogui.press("f10")
    time.sleep(2)
    # FindLampInF10

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread('lampinf10.png')
    large_image = image

    result = cv2.matchTemplate(small_image, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    MPx, MPy = mnLoc

    trows, tcols = small_image.shape[:2]
    win32api.SetCursorPos((MPx+tcols, MPy+trows))
    time.sleep(1)
    click(MPx+tcols+130, MPy+trows)

    time.sleep(1)
    pyautogui.press("y")
    time.sleep(1)
    # click(1731, 1057)
    time.sleep(1)


def findPartOfPost():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread('part.png')
    large_image = image

    result = cv2.matchTemplate(small_image, large_image, method)

    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    MPx, MPy = mnLoc
    trows, tcols = small_image.shape[:2]
    xRand = randint(MPx, MPx+tcols)
    yRand = randint(MPy, MPy+trows)
    click(xRand, yRand)
    click(xRand, yRand)

    time.sleep(1)


def lampInPost():
    # LAMP TO TAKE FROM POST
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread('lamptotake.png')
    large_image = image
    result = cv2.matchTemplate(small_image, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc

    trows, tcols = small_image.shape[:2]

    click(MPx, MPy)
    time.sleep(1)
    click(MPx, MPy+530)
    pyautogui.press("y")
    time.sleep(5)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("i")
    time.sleep(1)


def useLampInINV():
    # INVENTORY LAMP
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread('lamp.png')
    large_image = image
    result = cv2.matchTemplate(small_image, large_image, method)

    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    MPx, MPy = mnLoc

    trows, tcols = small_image.shape[:2]
    xRand = randint(MPx, MPx+tcols)
    yRand = randint(MPy, MPy+trows)
    click(xRand, yRand)
    click(xRand, yRand)
    click(xRand, yRand)
    click(xRand, yRand)
    time.sleep(1)
    pyautogui.press("y")
    time.sleep(7)


print("findlampinf10")
findlampinf10()

print("findPartOfPost")
findPartOfPost()

print("lampInPost")
lampInPost()

print("useLampInINV")
useLampInINV()
