import pygame
import random

pygame.font.init()
print(pygame.font.get_default_font())
WIDTH = 750
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
velocities = [-1,1]
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 30)
lScore = 0
rScore = 0
score1 = font.render(str(lScore), True, (255,255,255))
score2 = font.render(str(lScore), True, (255,255,255))

class paddle:
    def __init__(self,x):
        self.y = 220
        self.x = x
        self.height = 60
        self.width = 10
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        pygame.draw.rect(window, (255,255,255), self.hitbox)
        
    def update(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self,num):
        self.y -= num*4

class ball:
    def __init__(self):
        self.x = 370
        self.y = 245
        self.width = 10
        self.height = 10
        self.vx = 0
        self.vy = 0
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def start(self):
        self.vx = velocities[random.randint(0,1)]
        self.vy = velocities[random.randint(0,1)]
        self.x = 370
        self.y = 245
    
    def move(self):
        self.x += self.vx * 2
        self.y += self.vy * 2

    def draw(self):
        pygame.draw.rect(window, (255,255,255), self.hitbox)

    def update(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def getHit(self):
        if self.y < 0:
            self.vy *= -1
        if self.y + self.height > 500:
            self.vy *= -1

p1 = paddle(40)
p2 = paddle(700)
b = ball()
b.start()

def checkCollision(ball,leftPaddle,rightPaddle):
    if ball.hitbox.colliderect(leftPaddle.hitbox):
            ball.vx *= -1
            ball.vy = (ball.y+ball.height/2 - leftPaddle.y+leftPaddle.height/2)/leftPaddle.height
    if ball.hitbox.colliderect(rightPaddle.hitbox):
        ball.vx *= -1
        ball.vy = (ball.y+ball.height/2 - rightPaddle.y+rightPaddle.height/2)/rightPaddle.height

def draw():
    window.fill((0,0,0))
    p1.draw()
    p2.draw()
    for i in range(50):
        pygame.draw.rect(window, (255,255,255), (372, i*10+1,5,9))
    b.draw()
    score1Rect = score1.get_rect()
    score2Rect = score2.get_rect()
    score1Rect.center = (300,30)
    score2Rect.center = (450,30)
    window.blit(score1,score1Rect)
    window.blit(score2,score2Rect)
    pygame.display.update()

def update():
    global lScore, rScore, score1, score2
    b.move()
    b.update()
    p1.update()
    p2.update()
    b.getHit()
    if b.x < 0 or b.x+b.width > 750:
        if b.x<0:
            rScore += 1
        else:
            lScore += 1
        b.start()
    score1 = font.render(str(lScore), True, (255,255,255))
    score2 = font.render(str(rScore), True, (255,255,255))
        
    checkCollision(b,p1,p2)

while run:
    clock.tick(40)
    draw()
    update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and p1.y > 0:
        p1.move(1)
    if keys[pygame.K_s] and p1.y+p1.height<500:
        p1.move(-1)
    if keys[pygame.K_UP] and p2.y > 0:
        p2.move(1)
    if keys[pygame.K_DOWN] and p2.y+p2.height<500:
        p2.move(-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()