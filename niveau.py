import pygame
import csv
from math_jeu import *
from joueur   import *
from carreau  import *

TAILLE_GRILLE = 50
#'O' = ouvert
#'X' = fermé

class Niveau():
    def __init__(self, matrice_chemin):
        self.matrice = []
        self.obstacles = []
        self.joueurs = []
        self.groupe = GroupeCamera()
        self.ecran = pygame.display.get_surface().convert_alpha()

        with open(matrice_chemin, 'r') as csvfile:
            lire = csv.reader(csvfile)
            self.matrice = [ligne for ligne in lire]

    def carto_tuile(self, vitesse_joueur):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] == 'X':
                    o = Carreau((j*TAILLE_GRILLE, i*TAILLE_GRILLE))
                    self.obstacles.append(o)
                if self.matrice[i][j] == 'P':
                    self.p = Joueur(vitesse_joueur, (j*TAILLE_GRILLE,i*TAILLE_GRILLE),self.obstacles, self.ecran)
                    self.joueurs.append(self.p)
        self.groupe.add(self.joueurs, self.obstacles)
        
    def lancer_niveau(self, dt):
        self.groupe.update(dt)
        self.groupe.rendu_custom(self.p, dt)


class GroupeCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        import math
        self.ecran = pygame.display.get_surface()
        self.decalage = pygame.math.Vector2()

        self.delimitation = [
            300, #Left and Right
            150, #Top  and Bottom
        ]
        gauche   = self.delimitation[0]
        haut     = self.delimitation[1]
        largeur  = self.ecran.width  - (self.delimitation[0]*2) #Because left + right is same
        hauteur  = self.ecran.height - (self.delimitation[1]*2)
        self.rect_camera = pygame.Rect(gauche, haut, largeur, hauteur)

    def camera_boite(self, cible):
        if cible.is_moving():
            if cible.rect.left < self.rect_camera.left:
                self.rect_camera.left = cible.rect.left
            if cible.rect.right > self.rect_camera.right:
                self.rect_camera.right = cible.rect.right
            if cible.rect.top < self.rect_camera.top:
                self.rect_camera.top = cible.rect.top
            if cible.rect.bottom > self.rect_camera.bottom:
                self.rect_camera.bottom = cible.rect.bottom
        
        self.decalage.x = self.rect_camera.left - self.delimitation[0]
        self.decalage.y = self.rect_camera.top  - self.delimitation[1]

        return (self.decalage.x, self.decalage.y)

    def camera_centre(self, joueur, dt):
            import math
            self.decalage.x = lerp(self.decalage.x, joueur.rect.centerx - self.ecran.width/2,  1 - math.exp(-6*dt))
            self.decalage.y = lerp(self.decalage.y, joueur.rect.centery - self.ecran.height/2, 1 - math.exp(-6*dt))
            self.rect_camera.centerx = joueur.rect.centerx
            self.rect_camera.centery = joueur.rect.centery

    def rendu_custom(self, joueur, dt):
        self.camera_centre(joueur, dt)

        for sprite in self.sprites():
            rect_decalage = sprite.rect.topleft - self.decalage
            self.ecran.blit(sprite.image, rect_decalage)
