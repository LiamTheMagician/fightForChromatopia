import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, groups, spriteType, surface = pg.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.spriteType = spriteType
        self.image  = surface
        if self.spriteType == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)