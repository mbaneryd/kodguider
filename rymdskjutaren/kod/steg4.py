import pgzrun

WIDTH = 600
HEIGHT = 600

skepp = Rect(275, 540, 50, 30)
skott = []


def draw():
    screen.fill("black")
    screen.draw.filled_rect(skepp, "cyan")
    for s in skott:
        screen.draw.filled_rect(s, "yellow")


def update():
    if keyboard.left and skepp.left > 0:
        skepp.x = skepp.x - 6
    if keyboard.right and skepp.right < WIDTH:
        skepp.x = skepp.x + 6
    for s in skott[:]:
        s.y = s.y - 10
        if s.bottom < 0:
            skott.remove(s)


def on_key_down(key):
    if key == keys.SPACE:
        skott.append(Rect(skepp.centerx - 3, skepp.top - 15, 6, 15))


pgzrun.go()
