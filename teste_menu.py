import pygame
from pygame.locals import *
from animation import *
from bouton import *

pygame.init()

fenetre = pygame.display.set_mode((640,480))


inventaire = pygame.Rect(-200, 120, 50, 50)
pygame.draw.rect(fenetre,(50, 50, 50),inventaire)


""""  
bouton1 = Bouton((200,200), (50,50), "")
group_bouton = pygame.sprite.Group(bouton1)
"""

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        """
        if event.type == KEYDOWN:
            if event.key == K_m:   
                animation = True

                posx = lerp_single(inventaire.x, 200, 0.01)
                inventaire.x = posx
                posy = lerp_single(inventaire.y, 300, 0.01)
                inventaire.y = posy"""
    """
    fenetre.fill((0, 0, 0))
    group_bouton.update()
    group_bouton.draw(fenetre)
    """
    
    pygame.draw.rect(fenetre,(50, 50, 50),inventaire)
    pygame.display.flip()

pygame.quit()