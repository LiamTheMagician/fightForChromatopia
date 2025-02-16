import pygame
import time as framerate
from player    import *
from level     import *
from tile      import *
from game_math import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

prev_time = framerate.time()

l1 = Level('map/map1.csv')
l1.tile_mapping(500)

while True:
    dt = framerate.time() - prev_time
    prev_time = framerate.time()

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((50,50,50))

    l1.level_run(dt)
    pygame.display.flip()

