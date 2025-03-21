import pygame
import math
import time as framerate
from pygame.locals import *
from math_jeu     import *
from texte          import *
from elt_menu    import Background

class Menu():
    def __init__(self, chemins_image = 'art/fond.png', liste_bouton = []):
        pygame.init()
        pygame.font.init()
        self.ecran = pygame.display.get_surface()

        self.fond = Background((0,0), chemins_image)
        self.liste_bouton   = liste_bouton

        self.g_fond    = pygame.sprite.Group(self.fond)
        self.g_boutons = pygame.sprite.Group(self.liste_bouton)

        self.i = 0.5
        self.temps_precedent = framerate.time()

    def get_bouton(self, index_bouton):
        if self.g_boutons.sprites()[index_bouton].get_clicked():
            return True
        return False

    def fps(self, dt):
        self.i -= 1*dt
        if self.i <= 0:
            print(1/dt)
            self.i = 0.5

    def lancer_menu(self):
        dt = framerate.time() - self.temps_precedent
        self.temps_precedent = framerate.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        self.ecran.fill((50,50,50))
        self.fps(dt)

        self.g_boutons.update(dt)
        self.g_fond.update(True)
       
        self.g_fond.draw(self.ecran)
        self.g_boutons.draw(self.ecran)

        pygame.display.flip()