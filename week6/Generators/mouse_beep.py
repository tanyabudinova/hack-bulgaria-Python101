from pyautogui import position
# from os import system


def mouse_position():
    while True:
        yield position()


def beep():
    mouse = mouse_position()
    for i in mouse:
        if i == (0, 0):
            print('\a')
            # system("beep -f 555 -l 460")


beep()
