import pygame
import time as framerate
import sys
from niveau import *
from menu import *
from elt_menu import *

ecran      = pygame.display.set_mode((3840, 2160), pygame.RESIZABLE | pygame.SCALED)
jeu_cours  = False
menu_cours = True

boutons_menu_principal = [
    Button('Play', text_color=(255,255,255), font_size= 30,position=(720/2, 480/2), size=(200, 50))
]

class Game():
    def __init__(self, chemin_niveau, vitesse_joueur):
        pygame.init()
        self.horloge = pygame.time.Clock()
        
        self.vitesse_joueur = vitesse_joueur
        self.niveau = Niveau(chemin_niveau)
        self.niveau.carto_tuile(self.vitesse_joueur)

        self.temps_precedent = framerate.time()
        self.i = 1

    def changer_niveau(self, chemin_niveau):
        self.niveau = Niveau(chemin_niveau)
        self.niveau.carto_tuile(self.vitesse_joueur)

    def verifier_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def verifier_statut(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return False
        return True

    def fps(self, dt):
        self.i -= 1*dt
        if self.i <= 0:
            print(1/dt)
            self.i = 0.5

    def lancer_jeu(self):
        dt = framerate.time() - self.temps_precedent
        self.temps_precedent = framerate.time()

        ecran.fill((67, 171, 230))

        self.verifier_event()
        self.fps(dt)
        self.niveau.lancer_niveau(dt)

        pygame.display.flip()

jeu_principal  = Game("carte/carte1.csv", 400)
menu_principal = Menu("art/fond.png", boutons_menu_principal)

running = True
while running:
    if jeu_cours and menu_cours == False:
        jeu_principal.lancer_jeu()
        jeu_cours = jeu_principal.verifier_statut()
        menu_cours = not jeu_principal.verifier_statut() #not inverses le bool

    if menu_cours and jeu_cours == False:
        menu_principal.lancer_menu()

        if menu_principal.get_bouton(0) and jeu_cours == False:
            menu_cours = False
            jeu_cours = True
            
    if not jeu_cours and not menu_cours:
        pygame.quit()
        sys.exit()