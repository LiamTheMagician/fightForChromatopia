import pygame
from pygame.locals import *
from text import *

class Player(pygame.sprite.Sprite):
    def __init__(self, speed, collision_list, screen):
        super().__init__()
        #Player Parameters
        self.image = pygame.image.load('art/player.png').convert_alpha()
        self.rect  = self.image.get_rect()
        self.pos   = self.rect.center
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

    def movement(self):
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
            self.alignement = self.EMPTY

        if keys[K_LEFT]:
            self.direction.x = -1
            self.alignement = self.HORIZONTAL
        elif keys[K_RIGHT]:
            self.direction.x =  1
            self.alignement = self.HORIZONTAL
        else:
            self.direction.x = 0
            self.alignement = self.EMPTY
            
        if self.direction.length() >= 1:
            self.direction.normalize_ip() 
        self.vel = self.direction * self.acceleration
        self.rect.move_ip(self.vel.x, self.vel.y)

    def collisions(self):
        if self.alignement == self.HORIZONTAL:
            for objects in self.collision_list:
                if self.rect.colliderect(objects.rect):

    def player_debug(self):
        text(str(self.direction), self.screen, (255,255,255), (0,0))
        text(str(self.direction.length()), self.screen, (255,255,255), (0,100))

    def update(self):
        self.movement()
        self.collisions()
        #self.player_debug()