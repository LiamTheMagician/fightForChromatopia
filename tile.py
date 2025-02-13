import pygame
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("art/object.png")
        self.rect  = self.image.get_rect(topleft = (pos))
