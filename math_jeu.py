def lerp(a: int, b:int , t: float) -> float:
    """lerp(a, b, t)\n
    a: position de départ\n
    b: position d'arrivée\n
    t: valeur entre 0 et 1\n
    
    lerp renvoie une valeur entre a et b en fonction de t"""
    return a + (b - a) * t

def normaliser(x: float, min_value: float, max_value: float, min_range: float = 0.0, max_range: float = 1.0):
    """normaliser(a, b, t)
    x: valeur à normaliser
    min_value: valeur minimale possible
    max_value: valeur maximale possible
    
    normalise la valeur d'entrée entre 0 et 1 c'est à dire trouver un quotient d'une valeur sur une valeur maximale choisie"""
    if min_range == 0.0 and max_range == 1.0:
        return (x - min_value) / (max_value - min_value)
    else:
        return ((x - min_value) / (max_value - min_value)) * (max_range - min_range) + min_range

def exemple(rect):
    """
    en gros ici si tu veux partir d'un point A à un point B sans osciller entre les deux tu fais ça:
    1) tu trouves l'id de l'image du temps actuelle (donc 500 si c'est la 500e image créée par le programme)
    2) tu normalise une fonction sinusoidale en fonction du temps, le temps actuel est divisé par 100 pour éviter que ça causes des crises épileptiques
    3) tu fais l'interpolation de la dernière position de rectangle et ici 400. la valeur en temps est choisie au hasard (c'est pas en seconde du coup jsp)
    """
    import math
    import pygame
    current_time = pygame.time.get_ticks()
    t = normaliser(math.sin(current_time / 100), -1, 1)
    rect.x = lerp(rect.x, 400, 0.1)

def distance(pos1 = (0,0), pos2 = (0,0)):
    from math import sqrt
    return sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)