import pygame
from pygame.locals import *

def text(debug_text, screen, color, pos):
    pygame.font.init()
    my_font   = pygame.font.SysFont('Arial', 30)
    text_surf = my_font.render(debug_text, False, color)
    screen.blit(text_surf, pos)