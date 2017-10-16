# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González A01745998
# Descripción: Menú que da opciones para distintas funciones

import pygame
from random import randint


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

def dibujarCuadrosYCirculos():
    # círculo & cuadrado
    x = ANCHO // 2
    y = ALTO // 2
    r = 10 # radio
    l = r * 2 # longitud
    xC = ANCHO // 2 - r # x del cuadrado
    yC = ALTO // 2 - r # y del cuadrado

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for factor in range (1,ANCHO//20):
            pygame.draw.circle(ventana, NEGRO, (x, y), r * factor, 1)

        for factor in range (0,ANCHO//20):
            pygame.draw.rect(ventana, NEGRO,(xC - r*factor, yC - r*factor, l + 2*r*factor, l + 2*r*factor), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

def dibujarParabolas():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for separacion in range (0,ALTO // 2,10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, separacion), ((ANCHO//2) - separacion, ALTO//2), 1)
        for separacion in range(0, ALTO // 2, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO//2, separacion), ((ANCHO // 2) + separacion, ALTO // 2), 1)
        for separacion in range(0, ALTO // 2, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - separacion), ((ANCHO // 2) + separacion, ALTO // 2), 1)
        for separacion in range(0, ALTO // 2, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - separacion), ((ANCHO // 2) - separacion, ALTO // 2), 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps
    pygame.quit()   # termina pygame

def dibujarEspiral():
    x = ANCHO // 2
    y = ALTO // 2
    sep = 10
    dx = 0
    dy = 0

    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for trazo in range(1, 41):
            if trazo % 2 != 0:
                dx = trazo * sep
            elif trazo % 2 == 0:
                dy = trazo * sep

            pygame.draw.line(ventana, NEGRO, (x, y), (x + dx, y + dy))
            x += dx
            y += dy

        '''pygame.draw.line(ventana, NEGRO, (x+1*sep,y), (x+1*sep,y-1*sep))
        pygame.draw.line(ventana, NEGRO, (x+1*sep,y-1*sep), (x-1*sep,y-1*sep))
        pygame.draw.line(ventana, NEGRO, (x-1*sep,y-1*sep), (x-1*sep,y+1*sep))
        pygame.draw.line(ventana, NEGRO, (x-1*sep,y+1*sep), (x+2*sep,y+1*sep))
        pygame.draw.line(ventana, NEGRO, (x+2*sep,y+1*sep), (x+2*sep,y-2*sep))
        pygame.draw.line(ventana, NEGRO, (x+2*sep,y-2*sep), (x-2*sep,y-2*sep))
        pygame.draw.line(ventana, NEGRO, (x-2*sep,y-2*sep), (x-2*sep,y+2*sep))
        pygame.draw.line(ventana, NEGRO, (x-2*sep,y+2*sep), (x+3*sep,y+2*sep))
        pygame.draw.line(ventana, NEGRO, (x+3*sep,y+2*sep), (x+3*sep,y-3*sep))'''

        '''dx = contador * 10
        dy = contador * 10
        contador += 1
        if contador % 4 == 2:
            x += dx  # x = x + dx
        elif contador % 4 == 0:
            y += dy # y = y + dy'''
        '''pygame.draw.line(ventana,NEGRO, (400,400), (410,400)) #1
        pygame.draw.line(ventana,NEGRO, (410,400), (410,390)) #2
        pygame.draw.line(ventana,NEGRO, (410,390), (390,390)) #3
        pygame.draw.line(ventana,NEGRO, (390,390), (390,410)) #4
        pygame.draw.line(ventana,NEGRO, (390,410), (420,410)) #5
        pygame.draw.line(ventana,NEGRO, (420,410), (420,380)) #6'''

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(1)  # 40 fps
    pygame.quit()  # termina pygame

def dibujar12Circulos():
    x = 400
    y = 400
    radio = 150
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        for x in range (250,551):
            if x == 250:
                pygame.draw.circle(ventana,NEGRO,(x-125,y),radio,1)
            '''pygame.draw.circle(ventana, NEGRO, (475, 270), 150, 1)  # 1
            pygame.draw.circle(ventana, NEGRO, (475, 270), 150, 1) # 1
            pygame.draw.circle(ventana, NEGRO, (530, 325), 150, 1) # 2
            pygame.draw.circle(ventana, NEGRO, (550, 400), 150, 1) # 3
            pygame.draw.circle(ventana, NEGRO, (530, 475), 150, 1) # 4
            pygame.draw.circle(ventana, NEGRO, (475, 530), 150, 1) # 5
            pygame.draw.circle(ventana, NEGRO, (400, 550), 150, 1) # 6
            pygame.draw.circle(ventana, NEGRO, (325, 530), 150, 1) # 7
            pygame.draw.circle(ventana, NEGRO, (270, 475), 150, 1) # 8
            pygame.draw.circle(ventana, NEGRO, (250, 400), 150, 1) # 9
            pygame.draw.circle(ventana, NEGRO, (270, 325), 150, 1) # 10
            pygame.draw.circle(ventana, NEGRO, (325, 270), 150, 1) # 11
            pygame.draw.circle(ventana, NEGRO, (400, 250), 150, 1) # 12'''

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def aproximarPI(n):
    suma = 0
    contador = 0
    for d in range(1,n+1):
        contador += 1
        suma = suma + 1/(d**2)
    return (6*suma)**0.5

def main():
    #dibujarCuadrosYCirculos()
    #dibujarParabolas()
    #dibujarEspiral()
    dibujar12Circulos()
    #n = int(input("Inserte el número de divisores para hacer la aproximación: "))
    #print(aproximarPI(n))

main()