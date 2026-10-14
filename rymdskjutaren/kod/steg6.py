import pgzrun
import random

WIDTH = 600
HEIGHT = 600

skepp = Rect(275, 540, 50, 30)
skott = []
fiender = []
poang = 0


def draw():
    screen.fill("black")
    screen.draw.filled_rect(skepp, "cyan")
    for s in skott:
        screen.draw.filled_rect(s, "yellow")
    for f in fiender:
        screen.draw.filled_circle(f.center, 20, "lime")
    screen.draw.text("Poäng: " + str(poang), (10, 10), fontsize=40)


def update():
    global poang
    if keyboard.left and skepp.left > 0:
        skepp.x = skepp.x - 6
    if keyboard.right and skepp.right < WIDTH:
        skepp.x = skepp.x + 6
    for s in skott[:]:
        s.y = s.y - 10
        if s.bottom < 0:
            skott.remove(s)
    for f in fiender:
        f.y = f.y + 3
    for f in fiender[:]:
        for s in skott[:]:
            if f.colliderect(s):
                fiender.remove(f)
                skott.remove(s)
                poang = poang + 1
                break


def on_key_down(key):
    if key == keys.SPACE:
        skott.append(Rect(skepp.centerx - 3, skepp.top - 15, 6, 15))


def ny_fiende():
    fiender.append(Rect(random.randint(0, WIDTH - 40), -40, 40, 40))


clock.schedule_interval(ny_fiende, 1.0)

pgzrun.go()
