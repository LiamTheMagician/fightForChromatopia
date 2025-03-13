import csv
import pygame

GRID_SIZE = 50

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
        self.group.add(self.obstacles, self.players)
        
    def level_run(self, dt):
        self.group.update(dt)
        self.group.custom_draw(self.p)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.screen.width/2
        self.offset.y = player.rect.centery - self.screen.height/2

        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.screen.blit(sprite.image, offset_rect)
