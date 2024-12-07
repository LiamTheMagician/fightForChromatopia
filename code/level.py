import pygame as pg
from settings import *
from tile import *
from player import *

class Level:
    def __init__(self):
        #Get current display
        self.displaySurface = pg.display.get_surface()

        #Group Setup
        self.visibleSprites  = pg.sprite.Group()
        self.obstacleSprites = pg.sprite.Group()

        #Sprite setup
        self.createMap()
    
    def createMap(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visibleSprites, self.obstacleSprites])
                if col == 'p':
                    Player((x, y), [self.visibleSprites])

    def run(self):
        self.visibleSprites.draw(self.displaySurface)
        self.visibleSprites.update()