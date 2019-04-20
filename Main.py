from tkinter import *
import keyboard
import time
a = 1
b = 2
while a < b:
    keyboard.press_and_release('Ctrl+s')
    print("saved")

window = Tk()
label = label(window, font="Arial 16 italic")
label.pack()
window.mainloop()