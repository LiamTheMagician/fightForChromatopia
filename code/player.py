import pygame as pg
from settings import *
from debug import debug

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites):
        super().__init__(groups)
        self.image = pg.image.load('../graphics/test/player.png').convert_alpha()
        self.rect  = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -26)

        self.direction = pg.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacleSprites = obstacleSprites

    def input(self):
        keys = pg.key.get_pressed()
        pg.K_UP
        if keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_DOWN]:            
            self.direction.y =  1  
        else:
            self.direction.y = 0

        if keys[pg.K_LEFT]:
            self.direction.x = -1
        elif keys[pg.K_RIGHT]:
            self.direction.x =  1
        else:
            self.direction.x = 0

        # Attack Input
        if keys[pg.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pg.time.get_ticks()
            print("attack")

        # Magic Input
        if keys[pg.K_LCTRL] and not self.attacking:
            self.attacking = True
            self.attack_time = pg.time.get_ticks()
            print("magic")


    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def cooldowns(self):
        current_time = pg.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.rect.bottom
            
    def update(self):
        self.input()
        self.cooldowns()
        self.move(self.speed)