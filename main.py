import sys, pygame as pg
from pygame.locals import *
from settings import *
from debug import debug

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.handleEvents()
            self.window.fill("black")
            debug('Hello :)')
            pg.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()