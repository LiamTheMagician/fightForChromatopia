import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640,480))

inventaire = pygame.Rect(200,120,50,50)
pygame.draw.rect(fenetre,(50,50,50),inventaire)
position_inventaire = (200,120)
fenetre.blit(inventaire,position_inventaire)


continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        
        if event.type == KEYDOWN:
            if event.key == K_m:
                position_inventaire = position_inventaire(300,220)

    fenetre.blit(inventaire,position_inventaire)
    pygame.draw.rect(fenetre,(50,50,50),inventaire)
    pygame.display.flip()

pygame.quit()