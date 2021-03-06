import pygame
import random
import math


pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('space invaders')

# background
background = pygame.image.load('aaa.png')

pygame.display.set_icon(pygame.image.load('ufo.png'))

# ship
shipimage = pygame.image.load('space-invaders.png')
shipx = 600
shipy = 500
posx = 0
enemyimage = []
enemyx = []
enemyy = []
enemy_posx = []
enemy_posy = []
noofenemyship = 5
# enemyship
for i in range(noofenemyship):
    enemyimage.append(pygame.image.load('ufo2.png'))
    enemyx.append(random.randint(0, 850))
    enemyy.append(random.randint(0, 250))
    enemy_posx.append(0.5)
    enemy_posy.append(0.5)

# bullet

class bullets():
    def __init__(self,bulletimage,bulletx,bullety,bullet_posx,bullet_posy,bullet_state):
        self.bulletimage = bulletimage
        self.bulletx = bulletx
        self.bullety =bullety
        self.bullet_posx = bullet_posx
        self.bullet_posy = bullet_posy
        self.bullet_state = bullet_state

    def projection(self,x,y):
        global bullet_state
        self.bullet_state = "fire"
        self.x=x
        self.y=y
        screen.blit(self.bulletimage, ((self.x) + 24, self.y))


obj=bullets(pygame.image.load('bullet.png'),0,500,0,1,"ready")
obj1=bullets(pygame.image.load('bullet.png'),0,500,0,1,"ready")
obj2=bullets(pygame.image.load('bullet.png'),0,500,0,1,"ready")

# score
totalscore = 0
font = pygame.font.Font('freesansbold.ttf', 32)
X = 10
Y = 10
gameoverfont = pygame.font.Font('freesansbold.ttf', 70)

displayfont= pygame.font.Font('freesansbold.ttf', 70)


def display():
    display = font.render("NICE JOB YOUR SCORE IS : " + str(totalscore), True, (0, 255, 0))
    screen.blit(display, (220,250))
def game_over():
    gameover = gameoverfont.render("GAME OVER!", True, (185, 28, 20))
    screen.blit(gameover, (222, 150))

def score(x, y):
    score = font.render("score : " + str(totalscore), True, (255, 0, 0))
    screen.blit(score, (x,y))


def player(x, y):
    screen.blit(shipimage, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimage[i], (x, y))

def bullet_border():
    if obj.bullety <= 0:
        obj.bullety = 500
        obj.bullet_state = "ready"
    if obj1.bullety <= 0:
        obj1.bullety = 500
        obj1.bullet_state = "ready"
    if obj2.bullety <= 0:
        obj2.bullety = 500
        obj2.bullet_state = "ready"

condition=False
condition1=False
def is_collision(bulletx, bullety, enemyx, enemyy):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 25:
        return True
    else:
        return False

def bullet_fire():
    if obj.bullet_state == "fire":
        obj.projection(obj.bulletx, obj.bullety)
        obj.bullety -= obj.bullet_posy
    if obj1.bullet_state == "fire":
        obj1.projection(obj1.bulletx, obj1.bullety)
        obj1.bullety -= obj1.bullet_posy
    if obj2.bullet_state == "fire":
        obj2.projection(obj2.bulletx, obj2.bullety)
        obj2.bullety -= obj2.bullet_posy
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                posx += 0.5
            if event.key == pygame.K_LEFT:
                posx -= 0.5
            if event.key == pygame.K_SPACE:
                if obj.bullet_state == "ready" :
                    obj.bulletx = shipx
                    obj.projection(obj.bulletx, obj.bullety)
                elif obj1.bullet_state == "ready":
                    obj1.bulletx = shipx
                    obj1.projection(obj1.bulletx, obj1.bullety)
                elif obj2.bullet_state == "ready":
                    obj2.bulletx = shipx
                    obj2.projection(obj2.bulletx, obj2.bullety)
            if event.key == pygame.K_ESCAPE:
                condition=True
                condition1 = True
            if event.key == pygame.K_BACKSPACE:
                quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                posx = 0

    shipx += posx
    # player ship
    if shipx <= 0:
        shipx = 0
    elif shipx >= 850:
        shipx = 850

    # enemy ship(1)
    for i in range(noofenemyship):
        enemyx[i] += enemy_posx[i]
        if enemyx[i] <= 0:
            enemy_posx[i] = 0.5
            enemyy[i] += 15
        elif enemyx[i] >= 850:
            enemy_posx[i] = -0.5
            enemyy[i] += 15
        collision = is_collision(obj.bulletx, obj.bullety, enemyx[i], enemyy[i])
        collision1 = is_collision(obj1.bulletx, obj1.bullety, enemyx[i], enemyy[i])
        collision2 = is_collision(obj2.bulletx, obj2.bullety, enemyx[i], enemyy[i])
        if collision == True:
            obj.bullety = 500
            obj.bullet_state = "ready"
            enemyx[i] = random.randint(0, 850)
            enemyy[i] = random.randint(0, 250)
            totalscore += 1
        if collision1 == True:
            obj1.bullety = 500
            obj1.bullet_state = "ready"
            enemyx[i] = random.randint(0, 850)
            enemyy[i] = random.randint(0, 250)
            totalscore += 1
        if collision2 == True:
            obj2.bullety = 500
            obj2.bullet_state = "ready"
            enemyx[i] = random.randint(0, 850)
            enemyy[i] = random.randint(0, 250)
            totalscore += 1
        enemy(enemyx[i], enemyy[i], i)
        if condition == True:
            for a in range(noofenemyship):
                enemyy[a] = 5000
                shipx=3000
            display()
        for i in range(noofenemyship):
            if enemyy[i]>465:
                for j in range(noofenemyship):
                    enemyy[j]=3000
                    shipx=3000
                game_over()
                break

    bullet_border()
    bullet_fire()
    player(shipx, shipy)
    score(X, Y)
    pygame.display.update()
