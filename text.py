import pygame
from pygame.locals import *
from game_math     import *

class Text(pygame.sprite.Sprite):
    def __init__(self, string, screen, color, pos):
        super().__init__()
        pygame.font.init()
        self.string = string
        self.font   = pygame.font.SysFont('Comic Sans MS', 30)
        self.image = self.font.render(self.string, False, color)
        self.rect  = self.image.get_rect(topleft = (pos))

    def move(self, final_pos, time):
        self.movex = lerp_single(self.rect.x, final_pos[0], time)
        self.movey = lerp_single(self.rect.y, final_pos[1], time)
        self.rect.x = round(self.movex)
        self.rect.y = round(self.movey)

    def color(self, new_color):
        self.image = self.font.render(self.string, False, new_color)