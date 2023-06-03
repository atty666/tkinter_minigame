from tkinter import *
import time
import random


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr StickHands wanna out!")
        self.tk.resizable(False, False)
        self.tk.wm_attributes("-topmost", True)
        self.canvas = Canvas(self.tk, width=500, height=500)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.background = PhotoImage(file="background.gif")
        w = self.background.width()
        h = self.background.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h,
                                         image=self.background,
                                         anchor="nw")
        self.sprites = []       # sprites - game objects
        self.running = True

    def mainloop(self):
        while True:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


g = Game()
g.mainloop()