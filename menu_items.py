import pygame
from game_math import *
from level     import *
import time as framerate

class Button(pygame.sprite.Sprite):
    def __init__(self, init_color = (120,120,120), hover_color = (0,0,0), click_color = (255,255,255), position = (0,0), size = (50,50)):
        super().__init__()

        self.screen = pygame.display.get_surface()
        self.prev_time = framerate.time()

        self.image = pygame.Surface(size)
        self.rect  = self.image.get_rect(center=position)
        
        self.delay   = 0.2
        self.clicked = False

        self.init_color  = init_color
        self.hover_color = hover_color
        self.click_color = click_color

    def color(self, dt):
        click = pygame.mouse.get_pressed(3)

        self.image.fill(self.init_color)
        if click[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image.fill(self.click_color)
                self.delay = 0.5
                self.clicked = True

        elif not click[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image.fill(self.hover_color)
        
        if self.delay > 0.0:
            self.delay -= 1*dt

        elif self.delay == 0.0 and self.clicked:
            self.delay = 0.5
            self.clicked = False

    def get_clicked(self):
        if self.clicked:
            return True
        return False
            
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