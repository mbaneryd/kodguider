import pgzrun
from pgzero.builtins import *

WIDTH = 600
HEIGHT = 600

skepp = Rect(275, 540, 50, 30)


def draw():
    screen.fill("black")
    screen.draw.filled_rect(skepp, "cyan")


def update():
    if keyboard.left and skepp.left > 0:
        skepp.x = skepp.x - 6
    if keyboard.right and skepp.right < WIDTH:
        skepp.x = skepp.x + 6


pgzrun.go()
