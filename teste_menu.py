import pygame
from pygame.locals import *
from object import *


pygame.init()

fenetre = pygame.display.set_mode((640,480))


inventair = pygame.Rect(200, 120, 50, 50)
pygame.draw.rect(fenetre,(50, 50, 50),inventair)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        
        if event.type == KEYDOWN:
            if event.key == K_m:
                if inventair.x == 200 and inventair.y == 120:
                    inventair.move_ip(100, 100)
                elif inventair.x == 300 and inventair.y == 220:
                    inventair.move_ip(-100, -100)

    fenetre.fill((0, 0, 0))
    pygame.draw.rect(fenetre,(50, 50, 50),inventair)
    pygame.display.flip()

pygame.quit()