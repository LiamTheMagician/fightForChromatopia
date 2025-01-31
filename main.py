import pygame
from player import *
from map import *
from object import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

M=[['O', 'X', 'O'],
   ['O', 'X', 'X'],
   ['X', 'O', 'O'],
   ['X', 'X', 'O'],
   ['O', 'X', 'O'],
   ['O', 'X', 'X'],
   ['X', 'O', 'O'],
   ['X', 'X', 'O'],
]

o_group = pygame.sprite.Group()
matrice_ecran(M, o_group)

p1 = Player(3, o_group, screen)
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

    o_group.draw(screen)
    o_group.update()
    pygame.display.flip()
    
    clock.tick(60)