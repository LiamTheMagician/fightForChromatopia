import pygame
from pygame.locals import *
from text import *

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        super().__init__()
        self.image = pygame.image.load('art/npc.png').convert_alpha()
        self.rect  = self.image.get_frect(topleft=pos)
        self.pos   = pygame.math.Vector2(self.rect.topleft)
        self.screen = screen

    def player_debug(self):
        pass

    def update(self, dt):
        pass