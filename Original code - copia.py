import pygame
import random

# Ventana de juego
cell = Actor('border1')
cell1 = Actor('floor')
cell2 = Actor("grass")
cell3 = Actor("grass_flower")
level1 = Actor('numero1')
level2 = Actor('numero2')
level3 = Actor('numero3')
size_w = 9 # Anchura del campo en celdas
size_h = 10 # Altura del campo en celdas
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

mode = "menu"
win = 0

TITLE = "The Rabbit Hole" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

my_menu = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 5, 0, 6, 0, 7, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]]

my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Fila de poder de ataque y salud

my_map2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 3, 3, 3, 3, 3, 3, 3, 0],
          [0, 3, 3, 2, 3, 3, 3, 2, 0],
          [0, 3, 3, 3, 2, 3, 3, 3, 0],
          [0, 3, 2, 2, 3, 3, 2, 3, 0],
          [0, 3, 3, 3, 3, 2, 3, 3, 0],
          [0, 3, 2, 3, 3, 3, 2, 3, 0],
          [0, 3, 3, 3, 3, 3, 3, 3, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Fila de poder de ataque y salud

my_map3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 3, 3, 1, 3, 3, 1, 0],
          [0, 3, 3, 3, 3, 3, 3, 3, 0],
          [0, 3, 3, 3, 3, 3, 3, 3, 0],
          [0, 1, 3, 3, 3, 3, 3, 1, 0],
          [0, 1, 1, 3, 3, 3, 1, 1, 0],
          [0, 1, 1, 1, 3, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Fila de poder de ataque y salud


# Protagonista
char = Actor('alicedown')
char.top = cell.height
char.left = cell.width
char.health = 100
char.attack = 5

# Generando enemigos
enemies = []
for i in range(5):
    x = random.randint(1, 7) * cell.width
    y = random.randint(1, 7) * cell.height
    enemy = Actor("heart-knight", topleft = (x, y))
    enemy.health = random.randint(10, 20)
    enemy.attack = random.randint(5, 10)
    enemy.bonus = random.randint(0, 2)
    enemies.append(enemy)

# Bonificaciones
hearts = []
swords = []

def menu_draw():
    for i in range(len(my_menu)):
        for j in range(len(my_menu[0])):
            if my_menu[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_menu[i][j] == 5:
                level1.left = cell.width*j
                level1.top = cell.height*i
                level1.draw()
            elif my_menu[i][j] == 6:
                level2.left = cell.width*j
                level2.top = cell.height*i
                level2.draw()
            elif my_menu[i][j] == 7:
                level3.left = cell.width*j
                level3.top = cell.height*i
                level3.draw()
            elif my_menu[i][j] == 8:
                level4.left = cell.width*j
                level4.top = cell.height*i
                level4.draw()

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()
            elif my_map[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw()

def map2_draw():
    for i in range(len(my_map2)):
        for j in range(len(my_map2[0])):
            if my_map2[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map2[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map2[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()
            elif my_map2[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw()

def map3_draw():
    for i in range(len(my_map3)):
        for j in range(len(my_map3[0])):
            if my_map3[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map3[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map3[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()
            elif my_map3[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw()


def draw():
    if mode == 'menu':
        screen.fill('#2f3542')
        menu_draw()
        screen.draw.text("Welcome to The Rabbit Hole", center=(WIDTH/2, 80), color = 'white', fontsize = 30)
        screen.draw.text('Select a level', center=(144, HEIGHT/2), color = 'white', fontsize = 26)
        screen.draw.text('Level 1 \nPress "q"', center=(72, 240), color = 'white', fontsize = 26)
        screen.draw.text('Level 2 \nPress "w"', center=(144, 240), color = 'white', fontsize = 26)
        screen.draw.text('Level 3 \nPress "e"', center=(216, 240), color = 'white', fontsize = 26)

    elif mode == "Level1":
        screen.fill("#2f3542")
        map_draw()
        char.draw()
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
        screen.draw.text(char.health, center=(75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
        screen.draw.text(char.attack, center=(425, 475), color = 'white', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(swords)):
            swords[i].draw()

    elif mode == "Level2":
        screen.fill("#2f3542")
        map2_draw()
        char.draw()
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
        screen.draw.text(char.health, center=(75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
        screen.draw.text(char.attack, center=(425, 475), color = 'white', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(swords)):
            swords[i].draw()

    elif mode == "Level3":
        screen.fill("#2f3542")
        map3_draw()
        char.draw()
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
        screen.draw.text(char.health, center=(75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
        screen.draw.text(char.attack, center=(425, 475), color = 'white', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(swords)):
            swords[i].draw()

    elif mode == "end":
        screen.fill("#2f3542")
        if win == 1:
            screen.draw.text("¡Ganaste!", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)
        else:
            screen.draw.text("¡Perdiste!", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)

def on_key_down(key):
    global mode
    if event.type == pygame.K_a
        mode = 'level1'
    elif keyboard.w:
        mode = 'level2'
    elif keyboard.e:
        mode = 'level3'

    old_x = char.x
    old_y = char.y
    if keyboard.right and char.x + cell.width < WIDTH - cell.width:
        char.x += cell.width
        char.image = 'AliceR'
    elif keyboard.left and char.x - cell.width > cell.width:
        char.x -= cell.width
        char.image = 'AliceL'
    elif keyboard.down and char.y + cell.height < HEIGHT - cell.height*2:
        char.y += cell.height
        char.image = 'AliceDown'
    elif keyboard.up and char.y - cell.height > cell.height:
        char.y -= cell.height
        char.image = 'AliceUp'

    enemy_index = char.collidelist(enemies)
    if enemy_index != -1:
        char.x = old_x
        char.y = old_y
        enemy = enemies[enemy_index]
        enemy.health -= char.attack
        char.health -= enemy.attack
        if enemy.health <= 0:
            if enemy.bonus == 1:
                heart = Actor('eat_me_cake')
                heart.pos = enemy.pos
                hearts.append(heart)
            elif enemy.bonus == 2:
                sword = Actor('drink_me_bottle')
                sword.pos = enemy.pos
                swords.append(sword)
            enemies.pop(enemy_index)

def victory():
    global mode, win
    if enemies == [] and char.health > 0:
        mode = "end"
        win = 1
    elif char.health <= 0:
        mode = "end"
        win = -1

def update(dt):
    victory()
    for i in range(len(hearts)):
        if char.colliderect(hearts[i]):
            char.health += 5
            hearts.pop(i)
            break

    for i in range(len(swords)):
        if char.colliderect(swords[i]):
            char.attack += 5
            swords.pop(i)
            break
