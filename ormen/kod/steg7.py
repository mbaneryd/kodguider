import pgzrun
import random

# Skärmens storlek
WIDTH = 600
HEIGHT = 600

# Hur stor en ruta är, i pixlar
RUTA = 20

# Ormen är en lista med rutor. Den första är huvudet.
orm = [(10, 15), (9, 15), (8, 15)]
riktning = (1, 0)
mat = (20, 15)
game_over = False


# Ritar en ruta. x och y räknas i rutor, inte pixlar.
def rita_ruta(x, y, farg):
    screen.draw.filled_rect(Rect(x * RUTA, y * RUTA, RUTA - 1, RUTA - 1), farg)


# Väljer en slumpad ruta och skickar tillbaka den
def slumpa_mat():
    return (random.randint(0, 29), random.randint(0, 29))


# Svarar True om rutan är utanför skärmen eller i ormen
def krockar(ruta):
    if ruta[0] < 0 or ruta[0] > 29 or ruta[1] < 0 or ruta[1] > 29:
        return True
    if ruta in orm:
        return True
    return False


# Ritar allt på skärmen, 60 gånger i sekunden
def draw():
    screen.fill("black")
    rita_ruta(mat[0], mat[1], "red")
    for bit in orm:
        rita_ruta(bit[0], bit[1], "lime")
    huvud = orm[0]
    rita_ruta(huvud[0], huvud[1], "yellow")
    poang = len(orm) - 3
    screen.draw.text("Poäng: " + str(poang), (10, 10), fontsize=40)
    if game_over:
        screen.draw.text("GAME OVER", center=(300, 280), fontsize=80, color="red")
        screen.draw.text("Tryck R för att börja om", center=(300, 350), fontsize=40)


# Flyttar ormen en ruta
def steg():
    global mat, game_over
    if game_over:
        return
    huvud = orm[0]
    nytt = (huvud[0] + riktning[0], huvud[1] + riktning[1])
    if krockar(nytt):
        game_over = True
        return
    orm.insert(0, nytt)
    if nytt == mat:
        mat = slumpa_mat()
    else:
        orm.pop()


# Byter riktning, men bara om ormen inte svänger in i sin egen hals
def svang(ny):
    global riktning
    huvud = orm[0]
    nasta = (huvud[0] + ny[0], huvud[1] + ny[1])
    if nasta != orm[1]:
        riktning = ny


# Ställer tillbaka allt som det var i början
def starta_om():
    global orm, riktning, mat, game_over
    orm = [(10, 15), (9, 15), (8, 15)]
    riktning = (1, 0)
    mat = (20, 15)
    game_over = False


# Körs när man trycker på en tangent
def on_key_down(key):
    if key == keys.LEFT:
        svang((-1, 0))
    if key == keys.RIGHT:
        svang((1, 0))
    if key == keys.UP:
        svang((0, -1))
    if key == keys.DOWN:
        svang((0, 1))
    if key == keys.R and game_over:
        starta_om()


# Ormen tar ett steg var 0,15 sekund
clock.schedule_interval(steg, 0.15)

# Starta spelet (alltid sist!)
pgzrun.go()
