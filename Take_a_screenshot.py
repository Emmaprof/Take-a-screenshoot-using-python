
import tkinter as tk
from tkinter.filedialog import *
from numpy import take
import pyautogui

root = tk.Tk()

canvas = tk.Canvas(root, width = 300, height = 300)
canvas.pack()

def take_screenshoot():
    my_screenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    my_screenshot.save(save_path + "screenshoot.png")


button_pattern = tk.Button(text = "Take screenshot", command = take_screenshoot, font = 10)
canvas.create_window(150, 150, window = button_pattern)

root.mainloop()