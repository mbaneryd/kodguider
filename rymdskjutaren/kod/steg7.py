import pgzrun
import random
from pgzero.builtins import *

# Skärmens storlek
WIDTH = 600
HEIGHT = 600

# Spelets saker och variabler
skepp = Rect(275, 540, 50, 30)
skott = []
fiender = []
poang = 0
game_over = False


# Ritar allt på skärmen, 60 gånger i sekunden
def draw():
    screen.fill("black")
    screen.draw.filled_rect(skepp, "cyan")
    for s in skott:
        screen.draw.filled_rect(s, "yellow")
    for f in fiender:
        screen.draw.filled_circle(f.center, 20, "lime")
    screen.draw.text("Poäng: " + str(poang), (10, 10), fontsize=40)
    if game_over:
        screen.draw.text("GAME OVER", center=(300, 280), fontsize=80, color="red")
        screen.draw.text("Tryck R för att börja om", center=(300, 350), fontsize=40)


# Flyttar allt, 60 gånger i sekunden
def update():
    global poang, game_over
    if game_over:
        return

    # Styr skeppet med piltangenterna
    if keyboard.left and skepp.left > 0:
        skepp.x = skepp.x - 6
    if keyboard.right and skepp.right < WIDTH:
        skepp.x = skepp.x + 6

    # Skotten flyger uppåt
    for s in skott[:]:
        s.y = s.y - 10
        if s.bottom < 0:
            skott.remove(s)

    # Blobbarna faller nedåt
    for f in fiender[:]:
        f.y = f.y + 3
        if f.top > HEIGHT or skepp.colliderect(f):
            game_over = True

    # Träffade ett skott en blobb?
    for f in fiender[:]:
        for s in skott[:]:
            if f.colliderect(s):
                fiender.remove(f)
                skott.remove(s)
                poang = poang + 1
                break


# Körs när man trycker på en tangent
def on_key_down(key):
    global poang, game_over
    # Mellanslag = skjut
    if key == keys.SPACE and not game_over:
        skott.append(Rect(skepp.centerx - 3, skepp.top - 15, 6, 15))
    # R = börja om
    if key == keys.R and game_over:
        skott.clear()
        fiender.clear()
        poang = 0
        skepp.x = 275
        game_over = False


# Skapar en ny blobb på ett slumpat ställe
def ny_fiende():
    if not game_over:
        fiender.append(Rect(random.randint(0, WIDTH - 40), -40, 40, 40))


# En ny blobb varje sekund
clock.schedule_interval(ny_fiende, 1.0)

# Starta spelet (alltid sist!)
pgzrun.go()
