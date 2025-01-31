import pygame
from object import *

TAILLE_GRILLE = 64
#'O' = ouvert
#'X' = fermé

def matrice_ecran(mat,group):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'X':
               o = Object((mat[j]*TAILLE_GRILLE, mat[i]*TAILLE_GRILLE))
               group.add(o)