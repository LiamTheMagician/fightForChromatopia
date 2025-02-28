import pygame
import math
import time as framerate
from pygame.locals import *
from game_math     import *
from text          import *
from menu_items    import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

prev_time = framerate.time()

wallpaper = Background((0,0), "art/wallpaper.png")
wp_group  = pygame.sprite.Group(wallpaper)

button = Button((120,120,120), (0,0,0), (255, 255, 255), (screen.width - 210, 480/2), (200, 50))
g_button = pygame.sprite.Group(button)

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    dt = framerate.time() - prev_time
    prev_time = framerate.time()

    event_handler()
    screen.fill((50,50,50))

    wp_group.update(True)
    g_button.update(dt)

    wp_group.draw(screen)
    g_button.draw(screen)

    pygame.display.flip()
    

pygame.quit()
exit()