from random import randint
import cv2
import pyautogui
import numpy as np
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def invSlotsOpen():
    # time.sleep(2)
    # pyautogui.press("F11")
    # time.sleep(1)

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    small_image = cv2.imread('../img/exit.png')
    # large_image = cv2.imread('../img/screen.png')
    large_image = image

    result = cv2.matchTemplate(small_image, large_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("Result ", max_val)
    if(max_val > 0.95):
        print("Player found")
    w = small_image.shape[1]
    h = small_image.shape[0]

    cv2.rectangle(large_image, max_loc,
                  (max_loc[0]+w, max_loc[1]+h), (0, 0, 255), 2)
    cv2.imshow('output', large_image)
    cv2.waitKey(0)


invSlotsOpen()
