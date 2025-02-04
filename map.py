import pygame
from object import *
from player import *

GRID_SIZE = 50
#'O' = ouvert
#'X' = fermé

def object_mapping(mat,collision_group, player_group):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'X':
                o = Object((j*GRID_SIZE, i*GRID_SIZE))
                group.add(o)
            