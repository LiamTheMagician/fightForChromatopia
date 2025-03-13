import pygame
import math
import time as framerate
from pygame.locals import *
from game_math     import *
from text          import *
from menu_items    import Background

class Menu():
    def __init__(self, image_path = 'art/wallpaper.png', button_list = []):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.get_surface()

        self.wallpaper = Background((0,0), image_path)
        self.button_list   = button_list

        self.g_wallpaper = pygame.sprite.Group(self.wallpaper)
        self.g_buttons   = pygame.sprite.Group(self.button_list)

        self.prev_time = framerate.time()

    def get_button(self, button_index):
        if self.g_buttons.sprites()[button_index].get_clicked():
            return True
        return False

    def run_menu(self):
        dt = framerate.time() - self.prev_time
        self.prev_time = framerate.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        self.screen.fill((50,50,50))

        self.g_buttons.update(dt)
        self.g_wallpaper.update(True)
       
        self.g_wallpaper.draw(self.screen)
        self.g_buttons.draw(self.screen)

        pygame.display.flip()