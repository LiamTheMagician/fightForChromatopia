import pygame
from pygame.locals import *
from text import *

class Player(pygame.sprite.Sprite):
    def __init__(self, speed, collision_list, screen):
        super().__init__()
        #Player Parameters
        self.image = pygame.image.load('art/player.png').convert_alpha()
        self.rect  = self.image.get_rect(topleft = (50,50))
        self.pos   = pygame.math.Vector2(self.rect.topleft)
        self.vel   = pygame.math.Vector2()
        self.acceleration = speed
        self.direction    = pygame.math.Vector2()

        #Constants
        self.HORIZONTAL = "horizontal"
        self.VERTICAL   = "vertical"
        self.EMPTY      = ""

        #Collisions
        self.collision_list = collision_list

        #Display
        self.screen = screen

    def movement(self,dt):
        keys = pygame.key.get_pressed()
        self.alignement = ""

        if keys[K_UP]:
            self.direction.y = -1
            self.alignement = self.VERTICAL
        elif keys[K_DOWN]:
            self.direction.y =  1
            self.alignement = self.VERTICAL
        else:
            self.direction.y = 0

        if keys[K_LEFT]:
            self.direction.x = -1
            self.alignement = self.HORIZONTAL
        elif keys[K_RIGHT]:
            self.direction.x =  1
            self.alignement = self.HORIZONTAL
        else:
            self.direction.x = 0
            
        if self.direction.length() >= 1:
            self.direction.normalize_ip() 


        self.pos.x += self.direction.x * self.acceleration * dt
        self.pos.y += self.direction.y * self.acceleration * dt

        self.rect.x = self.pos.x
        self.collisions(self.HORIZONTAL)
        self.rect.y = self.pos.y
        self.collisions(self.VERTICAL)
        
    def collisions(self, alignement):
        if alignement == self.HORIZONTAL:
            for sprite in self.collision_list:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right
        
        if alignement == self.VERTICAL:
            for sprite in self.collision_list:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # Moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def player_debug(self):
        pass

    def update(self, dt):
        self.movement(dt)