import pygame
from pygame.locals import *


def deplacement(b, pos_x, pos_y):
    b.move_ip(pos_x, pos_y)

def taille(b, largeur, hauteur):
    b.size = (largeur, hauteur)

