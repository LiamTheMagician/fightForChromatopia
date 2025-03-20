import pygame
from pygame.locals import *
from text import *

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

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

        #Controller set-up
        self.joy_key = [0, 0]
        
        # Constants
        self.HORIZONTAL = "horizontal"
        self.VERTICAL   = "vertical"
        self.EMPTY      = ""

        # Collisions
        self.collision_list = collision_list

        # Display
        self.screen = screen

    def movement(self, dt):
        self.keys = pygame.key.get_pressed()

        self.alignement = self.EMPTY
        self.direction.xy = (0, 0)

        if (self.keys[K_LEFT] and not self.keys[K_RIGHT]):
            self.direction.x = -1
            self.alignement = self.HORIZONTAL
        elif self.keys[K_RIGHT] and not self.keys[K_LEFT]:
            self.direction.x = 1
            self.alignement = self.HORIZONTAL

        if self.keys[K_UP] and not self.keys[K_DOWN]:
            self.direction.y = -1
            self.alignement = self.VERTICAL
        elif self.keys[K_DOWN] and not self.keys[K_UP]:
            self.direction.y = 1
            self.alignement = self.VERTICAL

        if len(joysticks) == 0:
            if self.direction.length_squared() > 0:
                self.direction = self.direction.normalize()

        for i in range(len(joysticks)):
            if joysticks[i].get_init():
                self.joy_key[0] = round(joysticks[i].get_axis(0),1)
                self.joy_key[1] = round(joysticks[i].get_axis(1),1)

                self.direction.x = self.joy_key[0]
                self.direction.y = self.joy_key[1]
                if self.direction.length_squared() >= 0.25:
                    self.direction = self.direction.normalize()
            else:
                if self.direction.length_squared() > 0:
                    self.direction = self.direction.normalize()

        self.vel = self.direction * self.acceleration * dt

        self.pos.x += self.vel.x
        self.rect.x = round(self.pos.x)
        self.collisions(self.HORIZONTAL)

        self.pos.y += self.vel.y
        self.rect.y = round(self.pos.y)
        self.collisions(self.VERTICAL)

    def is_moving(self):
        if self.direction == (0,0):
            return False
        return True

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
        text_debug = f"DirX: {self.direction.x}\nDirY: {self.direction.y}"
        text(text_debug, (255,255,255), (0,0))

    def update(self, dt):
        self.movement(dt)

