import pygame
from player    import *
from level     import *
from tile      import *
from math      import *
from game_math import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

rect = pygame.Rect(-100, 200, 50, 50)

l1 = Level('map/map1.csv')
l1.tile_mapping()

while True:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if pygame.key == pygame.K_UP:
                initial_time = pygame.time.get_ticks()
    
    screen.fill((50,50,50))

    example(rect)

    pygame.draw.rect(screen,(20,20,20),rect)
    pygame.display.flip()
    
    clock.tick(60)