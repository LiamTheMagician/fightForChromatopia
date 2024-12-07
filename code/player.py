import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load('../graphics/test/player.png').convert_alpha()
        self.rect  = self.image.get_rect(topleft = pos)

        self.direction = pg.math.Vector2()

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_z]:
            self.direction.y = -1
        elif keys[pg.K_s]:            
            self.direction.y =  1
        else:
            self.direction.y = 0

        if keys[pg.K_q]:
            self.direction.x = -1
        elif keys[pg.K_d]:
            self.direction.x =  1
        else:
            self.direction.x = 0

        def update(self):
            self.input()