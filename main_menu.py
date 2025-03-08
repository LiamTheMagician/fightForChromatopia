import pygame
import menu_items
from time import time

class Menu():
    def __init__(self, p_wallpaper, l_buttons):
        pygame.init()
        self.screen = pygame.display.set_mode((720,480))

        self.prev_time = time()

        self.wallpaper = menu_items.Background((0,0), p_wallpaper)

        self.g_wallpaper = pygame.sprite.Group(self.wallpaper)
        self.g_button    = pygame.sprite.Group(l_buttons)

    def run(self):
        while True:
            dt = time() - self.prev_time
            self.prev_time = time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill((50,50,50))

            self.g_wallpaper.update(True)
            self.g_button.update(dt)
            
            self.g_wallpaper.draw(self.screen)
            self.g_button.draw(self.screen)

            pygame.display.flip()
