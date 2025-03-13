import pygame
from pygame.locals import *
from game_math     import *

def text(string, color, pos):
    screen = pygame.display.get_surface()
    string = string
    font   = pygame.font.SysFont('Comic Sans MS', 30)
    image  = font.render(string, False, color)
    rect   = image.get_frect(topleft = (pos))
    screen.blit(image, rect)
