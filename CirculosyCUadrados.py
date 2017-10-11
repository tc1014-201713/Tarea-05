import pygame
from math import *

def Dibujar_CirculosC():
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

        for i in range(10,400,10):
            pygame.draw.circle(ventana, NEGRO,((400),(400)),i,1 )

            pygame.draw.rect(ventana, NEGRO,(i,i,800-2*i,800-2*i),1)





        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()
Dibujar_CirculosC()