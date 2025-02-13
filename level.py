import pygame
import csv
from player import *
from tile import *

GRID_SIZE = 50
#'O' = ouvert
#'X' = fermé

class Level():
    def __init__(self, matrix_path):
        self.matrix = []
        self.obstacles = []
        self.players = []
        self.group = pygame.sprite.Group()
        self.surf = pygame.display.get_surface()

        with open(matrix_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            self.matrix = [row for row in reader]

    def tile_mapping(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 'X':
                    o = Tile((j*GRID_SIZE, i*GRID_SIZE))
                    self.obstacles.append(o)
                if self.matrix[i][j] == 'P':
                    p = Player(5, self.obstacles, self.surf)
                    self.players.append(p)
        self.group.add(self.obstacles, self.players)
        
    def level_run(self):
        self.group.update()
        self.group.draw(self.surf)
        