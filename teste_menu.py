import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640,480))

inventaire = pygame.Rect(200,120,50,50)
pygame.draw.rect(fenetre,(50,50,50),inventaire)


continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        
        if event.type == KEYDOWN:
            if event.key == K_m:
                inventaire = pygame.Rect(300,220,50,50)

    pygame.draw.rect(fenetre,(50,50,50),inventaire)
    pygame.display.flip()

pygame.quit()