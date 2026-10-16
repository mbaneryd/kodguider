import pgzrun
from pgzero.builtins import *

# Skärmens storlek
WIDTH = 600
HEIGHT = 600

# Hur stor en ruta är, i pixlar
RUTA = 20

# Ormen är en lista med rutor. Den första är huvudet.
orm = [(10, 15), (9, 15), (8, 15)]
riktning = (1, 0)


# Ritar en ruta. x och y räknas i rutor, inte pixlar.
def rita_ruta(x, y, farg):
    screen.draw.filled_rect(Rect(x * RUTA, y * RUTA, RUTA - 1, RUTA - 1), farg)


# Ritar allt på skärmen, 60 gånger i sekunden
def draw():
    screen.fill("black")
    for bit in orm:
        rita_ruta(bit[0], bit[1], "lime")
    huvud = orm[0]
    rita_ruta(huvud[0], huvud[1], "yellow")


# Flyttar ormen en ruta
def steg():
    huvud = orm[0]
    nytt = (huvud[0] + riktning[0], huvud[1] + riktning[1])
    orm.insert(0, nytt)
    orm.pop()


# Ormen tar ett steg var 0,15 sekund
clock.schedule_interval(steg, 0.15)

# Starta spelet (alltid sist!)
pgzrun.go()
