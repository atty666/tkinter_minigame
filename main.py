from tkinter import *
import time
import random


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr StickHands wanna out!")
        self.tk.resizable(False, False)
        self.tk.wm_attributes("-topmost", True,
                              "-alpha", 0.5)
        self.canvas = Canvas(self.tk, width=500, height=500)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
