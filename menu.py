import pygame
import math
import time as framerate
from pygame.locals import *
from game_math     import *
from text          import *
from button        import *

pygame.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()

prev_time = framerate.time()

wallpaper_img  = pygame.image.load("art/wallpaper.png")
wallpaper_rect = wallpaper_img.get_rect(center = (screen.width/2,screen.height/2))

def parralax(bg_rect, dt):
    mouse_x = normalize(pygame.mouse.get_pos()[0], 0, screen.width, 0.0, 1.0)
    mouse_y = normalize(pygame.mouse.get_pos()[1], 0, screen.height, 0.0, 1.0)

    bg_rect.centerx = lerp_single(bg_rect.centerx, mouse_trunc, mouse_x)
    print(mouse_trunc)

button = Button((720/2, 480/2))
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

    parralax(wallpaper_rect, dt)
    screen.blit(wallpaper_img, wallpaper_rect)
    pygame.display.flip()
    

pygame.quit()
exit()