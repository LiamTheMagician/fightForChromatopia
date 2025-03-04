import pygame
from pygame.locals import *
from text import *

class NPC(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        #Player Parameters
        self.image = pygame.image.load('art/npc.png').convert_alpha()
        self.rect  = self.image.get_rect(topleft = (50,50))
        self.rect = self.rect.center

    

    def update(self):
        pass