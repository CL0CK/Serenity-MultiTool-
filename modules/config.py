# ------Telegram BOT------
TELEGRAM_MESSAGES = True

# MY TELEGRAM BOT TOKEN
TOKEN = '444444444:AAEv0JWFbpbcSlWqk7ELEj4p4WgvFAN2L5I'
TELEGRAM = 444444444
GREETING_MESSAGE = "Привет, зайка ;3 \nЯ буду оповещать тебя обо всём, что произойдёт во время выполнения ks.py, и напишу тебе, если случится что-то плохое <3"
BOT_WELCOME_STICKER = open('sticks/welcome.webp', 'rb')
BOT_PROBLEM_STICKER = open('sticks/problem.webp', 'rb')
BOT_GOODBYE_STICKER = open('sticks/goodbye.webp', 'rb')
BOT_BREAK_STICKER = open('sticks/break.webp', 'rb')


# ------Debug------
DEBUG_MESSAGES = True  # Writes debug messages in cmd
BOT_SEND_SCREENS = True  # Send screens in Telegram

# ------Pauses------
SHORT_PAUSES = False  # Makes short pauses
LONG_PAUSE = True  # Makes long pauses
LONG_PAUSE_ACCS = 40  # Makes long every X accounts

# -----4game------
LAUNCHER_PROCESS_NAME = "Innova.Launcher.exe"
GAME_PROCESS_NAME = "BNSR.exe"
LAUCNHER_PATH = "C:/Program Files (x86)/Innova/4game2.0/4game.exe"
NUMBER_OF_ACCOUNTS = 200
START_FROM = 0
LAPS = 3  # number of laps
PASSWORD = "PASSWORD"  # Accounts password
SELECT_BNS_IN_4GAME = True  # Clicks on hyperlink0
CLICK_CENTER_IN_4GAME = True  # Clicks on 4game
SCREEN_CENTER_X_Y = [963, 173]  # Coordinates of your screen center

# ------Loginer Settings------
INV_EXPAND = False  # Expand character inventory to full
INV_ITEM_USE = False  # Uses item in inventory. INV_ITEM_IMG must be set
INV_ITEM_IMG = 'img/lamp.png'  # Item to search in inventory
INV_ITEM_TAKE = False  # Buy item from F10 and takes it to inventory


XP_LINE_YELLOW_X_Y = [18, 1077]  # Coordinates for Yellow XP Line in x,y
XP_LINE_YELLOW_R_G_B = [193, 127, 3]  # Color for Yellow XP Line in r,g,b

XP_LINE_GREEN_X_Y = [11, 1077]  # Coordinates for Green XP Line in x,y
XP_LINE_GREEN_R_G_B = [0, 206, 3]  # Color for Green XP Line in r,g,b

XP_LINE_BLUE_X_Y = [1558, 1076]  # Coordinates for Blue XP Line in x,y
XP_LINE_BLUE_R_G_B = [0, 31, 50]  # Color for Blue XP Line in r,g,b


# Divide by 2 to get the time in seconds. Ex: 80 - means 40 seconds
FBS_ITER = 80  # FirstBlackScreen Iterator (Close 1)
PIG_ITER = 40  # Player in game Iterator (Close on 3 (Searching player in game)
