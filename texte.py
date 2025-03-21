import pygame
from pygame.locals import *
from math_jeu     import *

def texte(string, couleur, pos):
    ecran  = pygame.display.get_surface()
    string = string
    police = pygame.font.SysFont('Comic Sans MS', 30)
    image  = police.render(string, False, couleur)
    rect   = image.get_frect(topleft = (pos))
    ecran.blit(image, rect)
