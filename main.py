import pygame 
pygame.init()
import random

window = pygame.display.set_mode((1370,714))
back_color = (255,0,0)
game = True
clock = pygame.time.Clock()
player1 = pygame.Rect(250,250,20,20)
bullets = []
bullets2 = []
while game:

    window.fill(back_color)
    pygame.draw.rect(window, (0,0,255), player1)

    if random.randint(0,200) < 170:
        x = random.randint(0,1350)
        y = -10
        bullets.append(pygame.Rect(x, y, 20, 20))

    for b in bullets:
        pygame.draw.rect(window, (0,0,0), b)

    for b in bullets:
        b.y += 5
        if b.colliderect(player1):
            game = False



    if random.randint(0,200) < 170:
        x = -10
        y = random.randint(0,1350)
        bullets2.append(pygame.Rect(x, y, 20, 20))

    for b in bullets2:
        pygame.draw.rect(window, (0,0,0), b)

    for b in bullets2:
        b.x += 5
        if b.colliderect(player1):
            game = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1.x >0:
        player1.x -= 6
    if keys[pygame.K_d] and player1.x <1315:
        player1.x += 6
    if keys[pygame.K_s] and player1.y <646:
        player1.y += 6
    if keys[pygame.K_w] and player1.y >0:
        player1.y -= 6

    pygame.display.update()

    clock.tick(60)
