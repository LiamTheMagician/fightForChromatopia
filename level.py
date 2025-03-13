import pygame
import csv
from game_math import *
from player    import *
from tile      import *


GRID_SIZE = 50
#'O' = ouvert
#'X' = fermé

class Level():
    def __init__(self, matrix_path):
        self.matrix = []
        self.obstacles = []
        self.players = []
        self.group = CameraGroup()
        self.screen = pygame.display.get_surface()

        with open(matrix_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            self.matrix = [row for row in reader]

    def tile_mapping(self, player_speed):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 'X':
                    o = Tile((j*GRID_SIZE, i*GRID_SIZE))
                    self.obstacles.append(o)
                if self.matrix[i][j] == 'P':
                    self.p = Player(player_speed, (j*GRID_SIZE,i*GRID_SIZE),self.obstacles, self.screen)
                    self.players.append(self.p)
        self.group.add(self.players, self.obstacles)
        
    def level_run(self, dt):
        self.group.update(dt)
        self.group.custom_draw(self.p)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        import math

        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

        self.bounding_box = [
            300, #Left and Right
            150, #Top  and Bottom
        ]
        left   = self.bounding_box[0]
        top    = self.bounding_box[1]
        width  = self.screen.width  - (self.bounding_box[0]*2) #Because left + right is same
        height = self.screen.height - (self.bounding_box[1]*2)
        self.camera_box = pygame.Rect(left, top, width, height)

    def box_camera(self, target):
        if target.is_moving():
            if target.rect.left < self.camera_box.left:
                self.camera_box.left = target.rect.left
            if target.rect.right > self.camera_box.right:
                self.camera_box.right = target.rect.right
            if target.rect.top < self.camera_box.top:
                self.camera_box.top = target.rect.top
            if target.rect.bottom > self.camera_box.bottom:
                self.camera_box.bottom = target.rect.bottom
        
        self.offset.x = self.camera_box.left - self.bounding_box[0]
        self.offset.y = self.camera_box.top  - self.bounding_box[1]

        return (self.offset.x, self.offset.y)

    def center_camera(self, player):
            self.offset.x = lerp_single(self.offset.x, player.rect.centerx - self.screen.width/2,  0.007)
            self.offset.y = lerp_single(self.offset.y, player.rect.centery - self.screen.height/2, 0.007)
            self.camera_box.centerx = player.rect.centerx
            self.camera_box.centery = player.rect.centery

    def custom_draw(self, player):
        self.center_camera(player)

        for sprite in self.sprites():
            offset_rect = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_rect)
