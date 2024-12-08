from csv import reader
from os import walk
import pygame as pg

def importCsvLayout(path):
    terrainMap = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrainMap.append(list(row))
        return terrainMap

def importFolder(path):
    surfaceList = []
    for _,__,imgFiles in walk(path):
        for image in imgFiles:
            fullPath = path + '/' + image
            imageSurf = pg.image.load(fullPath).convert_alpha()
            surfaceList.append(imageSurf)
    return surfaceList