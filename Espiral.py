import pygame
from math import *

def Dibujar_Espiral():
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

        x=400
        y=400
        for i in range (0,159):
            a = i % 4
            counter = (((i % 2) + i) // 2) * 10
            if a == 1:
                pygame.draw.line(ventana,NEGRO,(x,y),(x+counter,y+0),1)
                x+=counter
            elif a==2:
                pygame.draw.line(ventana, NEGRO, (x, y), (x +0, y - counter), 1)
                y-=counter
            elif a==3:
                pygame.draw.line(ventana, NEGRO, (x, y), (x -counter, y +0), 1)
                x-=counter
            else:
                pygame.draw.line(ventana, NEGRO, (x, y), (x + 0, y + counter), 1)
                y+=counter


        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()
Dibujar_Espiral()