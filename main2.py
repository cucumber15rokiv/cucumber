import pygame 
pygame.init()
import random
font = pygame.font.Font(None,200)
text = font.render("cucumber", True,(0,0,0))
window = pygame.display.set_mode((1370,714))

player = pygame.Rect(325,225,100,200)
player2 = pygame.Rect(525,225,100,200)
player3 = pygame.Rect(725,225,100,200)
player4 = pygame.Rect(925,225,100,200)

back_color = (25,50,0)
clock = pygame.time.Clock()
game = True

while game:
    window.fill(back_color)
    window.blit(text,(400,60))


    pygame.draw.rect(window, (255,250,0), player)
    pygame.draw.rect(window, (255,250,0), player2)
    pygame.draw.rect(window, (255,250,0), player3)
    pygame.draw.rect(window, (255,250,0), player4)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print (10)
        elif event.type == pygame.KEYDOWN:
            print (20)

    pygame.display.update()
    clock.tick(60)
