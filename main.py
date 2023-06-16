from tkinter import *
import time
import random


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr StickHands wanna out!")
        self.tk.resizable(False, False)
        self.tk.wm_attributes("-topmost", True)
        self.canvas = Canvas(self.tk, width=500, height=500,
                             highlightthickness=0)
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
        self.sprites = []  # sprites - game objects
        self.running = True

    def mainloop(self):
        while True:
            if self.running:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


class Sprites:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates


class PlatformSprite(Sprites):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprites.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y,
                                              image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def within_x(co1, co2):
    if (co2.x1 < co1.x1 < co2.x2) \
            or (co2.x1 < co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x2 < co1.x2) \
            or (co1.x1 < co2.x2 < co1.x2):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co1.y2 > co2.y1 and co1.y1 < co2.y2) \
            or (co2.y1 < co1.y2 < co2.y2) \
            or (co1.y1 < co2.y1 < co1.y2) \
            or (co1.y1 < co2.y2 < co1.y2):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co2.x2 >= co1.x1 >= co2.x1:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co2.x1 <= co1.x2 <= co2.x2:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co2.y2 >= co1.y1 >= co2.y1:
            return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if co2.y1 <= y_calc <= co2.y2:
            return True
    return False


g = Game()

platform1 = PlatformSprite(g, PhotoImage(file="platforms/large-platform.gif"),
                           0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file="platforms/large-platform.gif"),
                           150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file="platforms/large-platform.gif"),
                           300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file="platforms/large-platform.gif"),
                           300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file="platforms/medium-platform.gif"),
                           175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file="platforms/medium-platform.gif"),
                           50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file="platforms/medium-platform.gif"),
                           170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file="platforms/medium-platform.gif"),
                           40, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file="platforms/low-platform.gif"),
                           170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file="platforms/low-platform.gif"),
                            230, 200, 32, 10)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)

g.mainloop()
