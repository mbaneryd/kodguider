import pgzrun

WIDTH = 600
HEIGHT = 600

skepp = Rect(275, 540, 50, 30)


def draw():
    screen.fill("black")
    screen.draw.filled_rect(skepp, "cyan")


pgzrun.go()
