import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, speed, pos, collision_list, screen):
        super().__init__()
        # Player Parameters
        self.image = pygame.image.load('art/player.png').convert_alpha()
        self.rect  = self.image.get_frect(topleft=pos)
        self.pos   = pygame.math.Vector2(self.rect.topleft)
        self.vel   = pygame.math.Vector2(0, 0)
        self.acceleration = speed
        self.direction    = pygame.math.Vector2(0, 0)

        # Constants
        self.HORIZONTAL = "horizontal"
        self.VERTICAL   = "vertical"
        self.EMPTY      = ""

        # Collisions
        self.collision_list = collision_list

        # Display
        self.screen = screen

    def movement(self, dt):
        keys = pygame.key.get_pressed()
        self.alignement = self.EMPTY

        self.direction.xy = (0, 0)

        if keys[K_LEFT]:
            self.direction.x = -1
            self.alignement = self.HORIZONTAL
        elif keys[K_RIGHT]:
            self.direction.x = 1
            self.alignement = self.HORIZONTAL

        if keys[K_UP]:
            self.direction.y = -1
            self.alignement = self.VERTICAL
        elif keys[K_DOWN]:
            self.direction.y = 1
            self.alignement = self.VERTICAL

        if self.direction.length_squared() > 0:
            self.direction = self.direction.normalize()

        self.vel = self.direction * self.acceleration * dt

        self.pos.x += self.vel.x
        self.rect.x = round(self.pos.x)
        self.collisions(self.HORIZONTAL)

        self.pos.y += self.vel.y
        self.rect.y = round(self.pos.y)
        self.collisions(self.VERTICAL)

    def collisions(self, alignement):
        if alignement == self.HORIZONTAL:
            for sprite in self.collision_list:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    elif self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x
                    self.vel.x = 0
        
        if alignement == self.VERTICAL:
            for sprite in self.collision_list:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y
                    self.vel.y = 0

    def player_debug(self):
        print(f"Pos: {self.pos}, Vel: {self.vel}, Dir: {self.direction}")

    def update(self, dt):
        self.movement(dt)
