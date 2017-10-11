
import pygame
from math import *

def Dibujar_Circulos():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    NEGRO= (0,0,0)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)

        x=0
        radio=150
        angulo=0

        for i in range (1,13):
            angulo+= pi/6
            x=int(150*(cos(angulo)))
            y=int(150*(sin(angulo)))
            pygame.draw.circle(ventana, NEGRO,(x+400, y+400), radio, 1 )




        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()
Dibujar_Circulos()