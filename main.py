import pygame
from player    import *
from level     import *
from tile      import *
from game_math import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

rect = pygame.Rect(100, 200, 50, 50)

l1 = Level('map/map1.csv')
l1.tile_mapping()

while True:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((50,50,50))

    l1.level_run()
    pygame.display.flip()
    
    clock.tick(60)