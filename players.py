import pygame
from canstant import *

class player :
    dk_position = ["dk_bas", "dk_haut", "dk_gauche", "dk_droite"]
    dk_position[0] = pygame.image.load("dk_bas.png")
    dk_position[1] = pygame.image.load("dk_haut.png")
    dk_position[2] = pygame.image.load("dk_droite.png")
    dk_position[3] = pygame.image.load("dk_gauche.png")
    dkbas_rect = dk_position[0].get_rect()
    dkbas_rect.x = 30
    dkbas_rect.y = 0
#with open('fichier.txt','r') as fichier:
 #   fichier = fichier.read()
  #  print(fichier)
"""class mur :
 with open('fichier.txt', 'r') as fichier:
           structure_nuveau = []
           for ligne in fichier:
              ligne_structure = []
              for sprite in ligne:
                if sprite != '\n':
                    ligne_structure.append(sprite)
              structure_nuveau.append(ligne_structure)"""

