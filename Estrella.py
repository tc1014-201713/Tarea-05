#Javier Pascal Flores
#Encoding:UTF -8

import pygame
from random import *
from math import *

def dibujar_Estrella():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)
            for y in range(0, 400, 10):
                pygame.draw.line (ventana,(randint(0,255), randint(0,255), randint(0,255)) ,(400, y), (400 + y, 400),
                                 1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, y), (400 - y, 400),1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, 800 - y),(400 + y, 400), 1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, 800 - y),(400 - y, 400), 1)

            pygame.display.flip()
            reloj.tick(40)
    pygame.quit()

dibujar_Estrella()