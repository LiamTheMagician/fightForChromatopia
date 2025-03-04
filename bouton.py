import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect(center=position)
        self.is_hovered = False

    def color(self):
        click = pygame.mouse.get_pressed(3)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image.fill((20,20,100))
            if click[0]:
                self.image.fill((255,255,255))
        else:
            self.image.fill((100,20,20))

    def update(self):
        self.color()