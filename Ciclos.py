#encode: UTF-8
# Autor: David Ramírez Ríos, A01338802
# Descripción: Acciones múltiples elegidas por un menú.

import pygame
from random import randint
import math
ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

def dibujarA():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for coordenadas in range(395, -1, -10):
            pygame.draw.rect(ventana, NEGRO, (coordenadas, coordenadas, (400 - coordenadas)*2, (400-coordenadas)*2), 1)
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), (400 - coordenadas), 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujarB():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        x0 = 400
        y0 = 400
        xf = 400
        yf = 400
        for c in range(1, 40):
            if c%2 != 0:
                xf = 400 + 10*c
                pygame.draw.line(ventana, NEGRO, (x0, y0), (xf, yf), 1)
                x0 = xf
                yf = 400 - 10*c
                pygame.draw.line(ventana, NEGRO, (x0, y0), (xf, yf), 1)
                y0 = yf
            else:
                xf = 400 - 10 * c
                pygame.draw.line(ventana, NEGRO, (x0, y0), (xf, yf), 1)
                x0 = xf
                yf = 400 + 10 * c
                pygame.draw.line(ventana, NEGRO, (x0, y0), (xf, yf), 1)
                y0 = yf

        pygame.display.flip()
        reloj.tick(10)
    pygame.quit()

def dibujarC():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for angulo in range(30, 360, 30):
            x = int (150 * math.cos(math.radians(angulo)))
            y = int (150 * math.sin(math.radians(angulo)))
            pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), 150, 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujarD():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for c in range (0, 41):
            x = c*10 +400
            y = 800 - c*10
            pygame.draw.line(ventana, (randint(0,255), randint(0, 255), randint(0, 255)), (x, 400), (400, c*10), 1)
            pygame.draw.line(ventana, (randint(0,255), randint(0, 255), randint(0, 255)), (x, 400), (400, y), 1)
            pygame.draw.line(ventana, (randint(0,255), randint(0, 255), randint(0, 255)), (400 - c*10, 400), (400, y), 1)
            pygame.draw.line(ventana, (randint(0,255), randint(0, 255), randint(0, 255)), (400 - c*10, 400), (400, c*10), 1)

        pygame.display.flip()
        reloj.tick(10)
    pygame.quit()

def aproximarPI (n):
    denominadorPI = 0
    suma = 0
    for n in range (1,n+1):
        denominadorPI += 1
        suma += 1/denominadorPI**2
    aproximacionPI = (suma * 6) ** .5
    return aproximacionPI


def calcularDivisibles():
    contador = 0
    for c in range (1000, 10000):
        if c % 29 == 0:
            contador += 1

    return contador


def calcularPiramide():
    acumulador = 0
    sumatoria = 0
    for c in range(1,10):
        acumulador = acumulador * 10 + c
        suma = acumulador * 8 + c
        print("%d * 8 + %d"% (acumulador,c),suma )
    for c in range(1,10):
        #contador
        sumatoria = sumatoria * 10 + 1
        producto = sumatoria**2
        print("%d * %d = %d"%(sumatoria, sumatoria, producto))


def main ():
    print("Tarea 05: Ciclos")
    opcion = (""" 
    1. Dibujar cuadros y círculos
    2. Dibujar espiral
    3. Dinujar círculos
    4. Dibujar parábolas
    5. Aproximar PI
    6. Contar divisibles entre 29
    7. Imprimir prámides de números
    0. Salir""")
    menu = int(input("¿Qué deseas hacer?" + opcion))
    if menu>=0 and menu<=7:
        while menu > 0 and menu <= 7:
            if menu == 1:
                dibujarA()
                menu = int(input("¿Qué deseas hacer? " + opcion))
            elif menu == 2:
                dibujarB()
                menu = int(input("¿Qué deseas hacer? " + opcion))
            elif menu == 3:
                dibujarC()
                menu = int(input("¿Qué deseas hacer? " + opcion))
            elif menu == 4:
                dibujarD()
                menu = int(input("¿Qué deseas hacer? " + opcion))
            elif menu == 5:
                n = int(input("n: "))
                if n < 1:
                    print("ERROR")
                else:
                    print(aproximarPI(n))
                menu = int(input("¿Qué deseas hacer? " + opcion))
            elif menu == 6:
                print(calcularDivisibles())
                menu = int(input("¿Qué deseas hacer? " + opcion))
            elif menu == 7:
                calcularPiramide()
                menu = int(input("¿Qué deseas hacer? " + opcion))
        if menu != 0:
            print("ERROR")
        else:
            print("END")
    else:
        print("ERROR")






main()