import pygame
from pygame.locals import *
from texte import *

pygame.joystick.init()
manettes = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

class Joueur(pygame.sprite.Sprite):
    def __init__(self, vitesse, pos, liste_collision, ecran):
        super().__init__()
        # Player Parameters
        self.image = pygame.image.load('art/joueur.png').convert_alpha()
        self.rect  = self.image.get_frect(topleft=pos)
        self.pos   = pygame.math.Vector2(self.rect.topleft)
        self.velocite   = pygame.math.Vector2(0, 0)
        self.acceleration = vitesse
        self.direction    = pygame.math.Vector2(0, 0)

        # Controller set-up
        self.joy_key = [0, 0]
        
        # Constants
        self.HORIZONTAL = "horizontal"
        self.VERTICAL   = "vertical"
        self.VIDE      = ""

        # Collisions
        self.liste_collision = liste_collision

        # Display
        self.ecran = ecran

    def mouvement(self, dt):
        self.touches = pygame.key.get_pressed()

        self.alignement = self.VIDE
        self.direction.xy = (0, 0)

        if (self.touches[K_LEFT] and not self.touches[K_RIGHT]):
            self.direction.x = -1
            self.alignement = self.HORIZONTAL
        elif self.touches[K_RIGHT] and not self.touches[K_LEFT]:
            self.direction.x = 1
            self.alignement = self.HORIZONTAL

        if self.touches[K_UP] and not self.touches[K_DOWN]:
            self.direction.y = -1
            self.alignement = self.VERTICAL
        elif self.touches[K_DOWN] and not self.touches[K_UP]:
            self.direction.y = 1
            self.alignement = self.VERTICAL

        if len(manettes) == 0:
            if self.direction.length_squared() > 0:
                self.direction = self.direction.normalize()

        for i in range(len(manettes)):
            if manettes[i].get_init():
                self.joy_key[0] = round(manettes[i].get_axis(0),1)
                self.joy_key[1] = round(manettes[i].get_axis(1),1)

                self.direction.x = self.joy_key[0]
                self.direction.y = self.joy_key[1]
                if self.direction.length_squared() >= 0.25:
                    self.direction = self.direction.normalize()
            else:
                if self.direction.length_squared() > 0:
                    self.direction = self.direction.normalize()

        self.velocite = self.direction * self.acceleration * dt

        self.pos.x += self.velocite.x
        self.rect.x = round(self.pos.x)
        self.collisions(self.HORIZONTAL)

        self.pos.y += self.velocite.y
        self.rect.y = round(self.pos.y)
        self.collisions(self.VERTICAL)

    def bouge(self):
        if self.direction == (0,0):
            return False
        return True

    def collisions(self, alignement):
        if alignement == self.HORIZONTAL:
            for sprite in self.liste_collision:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    elif self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x
                    self.velocite.x = 0
        
        if alignement == self.VERTICAL:
            for sprite in self.liste_collision:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y
                    self.velocite.y = 0

    def debug_joueur(self):
        debug_texte = f"DirX: {self.direction.x}\nDirY: {self.direction.y}"
        texte(debug_texte, (255,255,255), (0,0))

    def update(self, dt):
        self.mouvement(dt)

