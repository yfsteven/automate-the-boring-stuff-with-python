#! python3
# looking_busy.py - nudges the mouse cursor every 10 second

import pyautogui

while True:
    pyautogui.sleep(10)
    pyautogui.move(1,0)
    print(pyautogui.position())
    pyautogui.sleep(10)
    pyautogui.move(-1,0)
    print(pyautogui.position())
