import pygame as pg
from settings import *
from tile import *
from player import *
from debug import debug
from support import *
from random import choice

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
        layouts = {
            'boundary' : importCsvLayout('../map/map_FloorBlocks.csv'),
            'grass'    : importCsvLayout('../map/map_Grass.csv'),
            'object'   : importCsvLayout('../map/map_Objects.csv')
        }

        graphics = {
            'grass'   : importFolder('../graphics/grass'),
            'objects' : importFolder('../graphics/objects')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacleSprites], 'invisible')
                        if style == 'grass':
                            randomGrassImage = choice(graphics['grass'])
                            Tile((x,y), [self.visibleSprites, self.obstacleSprites], 'grass', randomGrassImage)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y), [self.visibleSprites, self.obstacleSprites], 'object', surf)
                """
                if col == 'x':
                    Tile((x, y), [self.visibleSprites, self.obstacleSprites])
                if col == 'p':
                """

        self.player = Player((2000, 1425), [self.visibleSprites], self.obstacleSprites)

    def run(self):
        self.visibleSprites._customDraw(self.player)
        self.visibleSprites.update()
        debug(self.player.direction)

class YSortCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pg.display.get_surface()
        self.halfWidth     = self.displaySurface.get_size()[0] // 2 
        self.halfHeight    = self.displaySurface.get_size()[1] // 2 
        self.offset = pg.math.Vector2()

        #Creating Floor
        self.floorSurf = pg.image.load('../graphics/tilemap/ground.png').convert()
        self.floorRect = self.floorSurf.get_rect(topleft = (0, 0))

    def _customDraw(self, player):

        #Getting the offset
        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight

        floorOffsetPos = self.floorRect.topleft - self.offset
        self.displaySurface.blit(self.floorSurf, floorOffsetPos)

        #Draw in order
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)