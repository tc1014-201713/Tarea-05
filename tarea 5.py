# encoding UTF-8
# Autor: Andrea Montero Rivas, A01374496
# Descripción: tarea pygame
import pygame
from random import randint
from math import pi
from math import sin
from math import cos


#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

#colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)

#circulo
radio = 400

def dibujarCuadrosyCirculos():
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        ventana.fill(BLANCO)
        reloj.tick(40)
        radio = 400
        lado = 800
        coordenadas = 0
        while radio>0 and lado>0:
            # Dibujar, aquí haces todos los trazos que requieras.
            pygame.draw.rect(ventana, NEGRO, (coordenadas, coordenadas, lado, lado), 2)
            lado -= 20
            coordenadas += 10
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2, ALTO//2),radio, 2)
            radio -= 10

        pygame.display.flip()   # Actualiza trazos
                     # 40 fps

    pygame.quit()   # termina pygame

def dibujarEspiral():
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  #Bandera para saber si termina la ejecución
    while not termina:
        #Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  #El usuario hizo click en el botón de salir
                termina = True
        ventana.fill(BLANCO)  # Borrar pantalla

        # Dibujar, aquí haces todos los trazos que requieras
        a = 790
        b = 10
        while a > 400 and b < 800:
            pygame.draw.line(ventana, NEGRO, (a, a), (b, a), 2)
            pygame.draw.line(ventana, NEGRO, (b, a), (b, b), 2)
            a -= 10
            pygame.draw.line(ventana, NEGRO, (b, b), (a, b), 2)
            pygame.draw.line(ventana, NEGRO, (a, b), (a, a), 2)
            b += 10

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def dibujarCirculos():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        ventana.fill(BLANCO) # Borrar pantalla

        # Dibujar, aquí haces todos los trazos que requieras

        radio = 150
        pygame.draw.circle(ventana, NEGRO, [250, 400], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [270, 325], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [325, 270], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [400, 250], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [475, 270], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [529, 325], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [550, 400], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [529, 475], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [475, 529], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [400, 550], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [325, 529], radio, 1)
        pygame.draw.circle(ventana, NEGRO, [269, 476], radio, 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

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
        pm = 400
        x1 = 0
        y1 = 400
        x2 = 800
        y2 = 400
        while x1 < 400 and y1 > 0 and x2>400 and y2<800:
            aleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana,aleatorio,(x1,pm),(pm,y1), 2)
            pygame.draw.line(ventana, aleatorio, (x2, pm), (pm, y1), 2)
            pygame.draw.line(ventana, aleatorio, (x1, pm), (pm, y2), 2)
            pygame.draw.line(ventana, aleatorio, (x2, pm), (pm, y2), 2)
            x1 += 10
            y1 -= 10
            x2 -= 10
            y2 += 10

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

def aproximarPI(n):
    suma = 0
    for d in range(1, n+1, 1):
        suma = suma + 1 / d**2
        suma2 = (6 * suma) ** 0.5
    return suma2

def contarDivisiblesEntre29():
    contador = 0
    d = 1000
    while d < 10000:
        if d % 29 == 0:
            contador += 1
        d += 1
    print(contador)

def imprimirPirámidesDeNúmeros():
    a = 1
    b = 1
    while a <= 123456789 and b < 10:
        print("%d * %d + %d = %d" % (a, 8, b, (a * 8 + b)))
        b += 1
        a = a * 10 + b
    print("")
    i = 1
    while i <= 11111111:
        print("%d * %d = %d" % (i, i, (i*i)))
        i = i * 10 + 1


def hacerSeleccion():
    seleccion = -1
    while seleccion != 0:
        print("""MENU:
        1. Dibujar cuadros y círculos
        2. Dibujar espiral
        3. Dibujar círculos
        4. Dibujar parábolas
        5. Aproximar PI
        6. Contar divisibles entre 29
        7. Imprimir pirámides de números
        0. Salir""", )
        seleccion = int(input("¿Qué desea hacer?", ))
        if (seleccion==1):
            dibujarCuadrosyCirculos()
        elif (seleccion==2):
            dibujarEspiral()
        elif (seleccion==3):
            dibujarCirculos()
        elif (seleccion == 4):
            dibujarParabolas()
        elif (seleccion == 5):
            n = int(input("Numero a aproximar:"))
            aproximarPI(n)
        elif (seleccion==6):
            print(contarDivisiblesEntre29())
        elif (seleccion == 7):
            imprimirPirámidesDeNúmeros()
        else:
            exit()

def main():
    hacerSeleccion()

main()