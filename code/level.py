import pygame as pg

class Level:
    def __init__(self):
        #Get current display
        self.displaySurface = pg.display.get_surface()
        #Group Setup
        self.visibleSprites  = pg.sprite.Group()
        self.obstacleSprites = pg.sprite.Group()
    
    def run(self):
        pass