import pgzrun

# Skärmens storlek
WIDTH = 600
HEIGHT = 600

# Hur stor en ruta är, i pixlar
RUTA = 20


# Ritar en ruta. x och y räknas i rutor, inte pixlar.
def rita_ruta(x, y, farg):
    screen.draw.filled_rect(Rect(x * RUTA, y * RUTA, RUTA - 1, RUTA - 1), farg)


# Ritar allt på skärmen, 60 gånger i sekunden
def draw():
    screen.fill("black")
    rita_ruta(0, 0, "white")
    rita_ruta(10, 15, "lime")
    rita_ruta(29, 29, "red")


# Starta spelet (alltid sist!)
pgzrun.go()
