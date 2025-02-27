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

wallpaper_img  = pygame.image.load("art/wallpaper.png")
wallpaper_rect = wallpaper_img.get_rect(center = (0,0))

def parralax(bg_rect, ratio):
    mouse = pygame.mouse.get_pos()
    bg_rect.centerx = -mouse[0] + bg_rect.width

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

    parralax(wallpaper_rect, 0.5)
    screen.blit(wallpaper_img, wallpaper_rect)
    pygame.display.flip()
    

pygame.quit()
exit()