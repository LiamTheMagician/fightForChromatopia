import pygame
import math
import time as timing
from pygame.locals import *
from game_math     import *
from text          import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()
prev_time = timing.time() 

main_title = Text("Chromatopia", screen, (255,255,255), (screen.get_width()/2, 580))
text_group = pygame.sprite.Group(main_title)

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    dt = timing.time() - prev_time
    prev_time = timing.time()
    event_handler()
    
    screen.fill((50,50,50))

    current_time = pygame.time.get_ticks() /1000
    new_color = (normalize(math.sin(current_time), -1, 1) * 255,
                 normalize(math.sin(current_time + 2), -1, 1) * 255,
                 normalize(math.sin(current_time + 4), -1, 1) * 255)
                 
    main_title.move((main_title.rect.x, screen.get_height()/2), 1)
    main_title.color(new_color)
    print(main_title.rect.center)

    text_group.update()
    text_group.draw(screen)
    pygame.display.flip()
    

pygame.quit()
exit()