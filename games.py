import pygame
from pygame.locals import *
from players import *
from canstant import *
pygame.init()
window = pygame.display.set_mode((450,450))
title = pygame.display.set_caption("DK Labyrinthe")
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play()


with open('fichier.txt', 'r') as fichier:
    structure_niveau = []
    for ligne in fichier:
        ligne_structure = []
        for sprite in ligne:
            if sprite != '\n':
               ligne_structure.append(sprite)
        structure_niveau.append(ligne_structure)
i = 0
running = True
while running:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and player.dkbas_rect.y < 420 and structure_niveau[case_y + 1][case_x] != 'm':
                player.dkbas_rect = player.dkbas_rect.move(0,30)
                case_y += 1

                i =0
            if event.key == pygame.K_UP and player.dkbas_rect.y > 0 and structure_niveau[case_y - 1][case_x] != 'm':
                    player.dkbas_rect = player.dkbas_rect.move(0,-30)
                    case_y -= 1
                    i =1
            if event.key == pygame.K_RIGHT and player.dkbas_rect.x < 420 and structure_niveau[case_y][case_x + 1] != 'm':
                    player.dkbas_rect = player.dkbas_rect.move(30,0)
                    case_x += 1
                    i = 2
            if event.key == pygame.K_LEFT and player.dkbas_rect.x > 0 and structure_niveau[case_y][case_x - 1] != 'm':
                    player.dkbas_rect = player.dkbas_rect.move(-30,0)
                    case_x -= 1
                    i = 3
    window.blit(font, (0, 0))
    y_taille = 0
    for ligne in structure_niveau:
        x_taille = 0
        for sprit in ligne:
            if sprit == 'd':
                x = x_taille * taille_sprit
                y = y_taille * taille_sprit
                window.blit(depart, (x, y))
            elif sprit == 'm':
                x = x_taille * taille_sprit
                y = y_taille * taille_sprit
                window.blit(mur, (x, y))
            elif sprit == 'a':
                x = x_taille * taille_sprit
                y = y_taille * taille_sprit
                window.blit(arrive, (x, y))
            x_taille += 1
        y_taille += 1
    window.blit(player.dk_position[i], player.dkbas_rect)
    if player.dkbas_rect.x == 420 and player.dkbas_rect.y == 420:
        window.blit(gagne,(0,0))
        pygame.mixer.music.stop()
    pygame.display.flip()
quit()