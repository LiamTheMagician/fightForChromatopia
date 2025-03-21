import pygame
from math_jeu import *
from niveau     import *
import time as framerate

class Button(pygame.sprite.Sprite):
    def __init__(self, text = 'Stupid shit', text_color = (0,0,0), font_size = 50, init_color = (120,120,120), hover_color = (0,0,0), click_color = (255,255,255), position = (0,0), size = (50,50)):
        super().__init__()
        pygame.font.init()
        
        self.screen = pygame.display.get_surface()
        self.prev_time = framerate.time()

        self.image = pygame.Surface(size).convert_alpha()
        self.rect  = self.image.get_rect(center=position)
        
        self.font = pygame.font.SysFont('Comic Sans MS', font_size)
        self.text = text
        self.text_color = text_color
        self.text_surface = self.font.render(text, True, text_color).convert_alpha()
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

        self.delay   = 0.5
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

        if click[0] and self.delay <= 0.0:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image.fill(self.click_color)
                self.clicked = True

        elif not click[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image.fill(self.hover_color)
        
        if self.delay >= 0.0:
            self.delay -= 1*dt

        self.image.blit(self.text_surface, self.text_surface.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2)))

    def get_clicked(self):
        if self.clicked:
            self.clicked = False
            self.delay = 0.5
            return True
        return False
            
    def update(self, delta_time):
        self.color(delta_time)

class Background(pygame.sprite.Sprite):
    def __init__(self, position, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.screen = pygame.display.get_surface()

    def parallax(self):
        mouse_x = normaliser(pygame.mouse.get_pos()[0], 0, self.screen.width,  0.48, 0.52)
        mouse_y = normaliser(pygame.mouse.get_pos()[1], 0, self.screen.height, 0.48, 0.52)

        self.rect.centerx = -mouse_x * self.screen.width + self.screen.width
        self.rect.centery = -mouse_y * self.screen.height + self.screen.height

    def update(self, parallax):
        if parallax:
            self.parallax()