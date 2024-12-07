import pygame as pg
from settings import *
from tile import *
from player import *
from debug import debug

class Level:
    def __init__(self):
        #Get current display
        self.displaySurface  = pg.display.get_surface()

        #Group Setup
        self.visibleSprites  = YSortCameraGroup()
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
                    self.player = Player((x, y), [self.visibleSprites], self.obstacleSprites)

    def run(self):
        self.visibleSprites.customDraw(self.player)
        self.visibleSprites.update()
        debug(self.player.direction)

class YSortCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pg.display.get_surface()
        self.half_width     = self.displaySurface.get_size()[0] // 2 
        self.half_height    = self.displaySurface.get_size()[1] // 2 
        self.offset = pg.math.Vector2()

    def customDraw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)