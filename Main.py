from tkinter import *
import keyboard
import time
a = 1
b = 2
while a < b:
    keyboard.press_and_release('Ctrl, s')
    print("saved")
    time.sleep(30)