import sys, pygame as pg
from pygame.locals import *

SCREEN_SIZE = (1280, 720)

class Game:
    def __init__(self):
        self.window = pg.display.set_mode(SCREEN_SIZE)
        self.running = True

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
                running = False

    def run(self):
        running = True
        while self.running:
            self.handleEvents()
            
game = Game()
game.run()