import pygame
from player import *
from map    import *
from object import *
from animation import *
from npc import *
pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

p1 = Player(3, [], screen)
p_group = pygame.sprite.Group(p1)


while True:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((50,50,50))


    #Draw
    p_group.draw(screen)
    p_group.update()

    pygame.display.flip()
    
    clock.tick(60)