import pygame
import math
import time as timing
from pygame.locals import *
from game_math     import *
from text          import *
from button        import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

button = Button((720/2, 480/2))
g_button = pygame.sprite.Group(button)

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    event_handler()
    screen.fill((50,50,50))

    g_button.draw(screen)
    g_button.update()
    pygame.display.flip()
    

pygame.quit()
exit()