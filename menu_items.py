import pygame
from game_math import *

class Button(pygame.sprite.Sprite):
    def __init__(self, init_color, hover_color, click_color,position, size = (50,50)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=position)

        self.delay = 0.2
        self.click_delay = 0.5

        self.init_color = init_color
        self.hover = hover_color
        self.click = click_color

    def color(self, delta_time):
        click = pygame.mouse.get_pressed(3)
        if self.delay >= 0:
            self.image.fill(self.init_color)
            self.delay -= 1 * delta_time

        elif self.rect.collidepoint(pygame.mouse.get_pos()) and self.delay  <= 0.1:
            self.image.fill(self.hover)
            if click[0]:
                while self.click_delay >= 0:
                    self.click_delay -= 0.01
                    self.image.fill(self.click)
                    print(self.click_delay)
                self.click_delay = 0.5
                self.delay = 2
                
        else:
            self.image.fill(self.init_color)
            

    def update(self, delta_time):
        self.color(delta_time)

class Background(pygame.sprite.Sprite):
    def __init__(self, position, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)
        self.screen = pygame.display.get_surface()

    def parallax(self):
        mouse_x = normalize(pygame.mouse.get_pos()[0], 0, self.screen.width,  0.48, 0.52)
        mouse_y = normalize(pygame.mouse.get_pos()[1], 0, self.screen.height, 0.48, 0.52)

        self.rect.centerx = -mouse_x * self.screen.width + self.screen.width
        self.rect.centery = -mouse_y * self.screen.height + self.screen.height

    def update(self, parallax):
        if parallax:
            self.parallax()