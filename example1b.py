#!python3
# Demonstration of how to use special keys on the keyboard
# using the hotkey command

import pyautogui
import time

print("Move your mouse over the word on line 8 before the countdown completes!")
print("         word           ")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print("I'm going to doubleclick the word!")
time.sleep(1)
pyautogui.click(clicks=2)

print("Now I'm going to copy the word using ctrl-c!")
time.sleep(1)
pyautogui.hotkey('ctrl','c')

print("Now I'm going to paste and press enter")
time.sleep(1)
pyautogui.hotkey('ctrl','v')
pyautogui.press("tab")
pyautogui.press("enter")








