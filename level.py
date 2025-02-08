import pygame
from object import *

GRID_SIZE = 50

class Level():
    def __init__(self, id, level_matrix, group):
        self.id = id
        for i in range(len(level_matrix)):
            for j in range(len(level_matrix[i])):
                if level_matrix[i][j] == 'X':
                    o = Object((j*GRID_SIZE, i*GRID_SIZE))
                    group.add(o)