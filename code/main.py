import sys, pygame as pg
from pygame.locals import *
from settings import *
from level import Level

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Fight for CHROMATOPIA')
        self.clock = pg.time.Clock()

        self.level = Level()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.handleEvents()

            self.window.fill("black")
            self.level.run()

            pg.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()