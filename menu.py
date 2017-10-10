# encoding: UTF-8
# Autor: Luis Alfonso Alcántara

import pygame
from random import randint
from math import *

def dibujarCuadrosYCirculos():
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
        negro = (0, 0, 0)

        for x in range(10, 801, 10):
            pygame.draw.rect(ventana, negro, (x, x, 800 - 2 * x, 800 - 2 * x), 1)

        for y in range(10, 391, 10):
            pygame.draw.circle(ventana, negro, (ANCHO // 2, ALTO // 2), y, 2)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def dibujarEspiral():

    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
    ROJO = (255, 0, 0)
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        posX = 400
        posY = 400

        for x in range(1, 159):
            y = x % 4
            contador = (((x % 2) + x) // 2) * 10
            if y == 1:
                pygame.draw.line(ventana, ROJO, (posX, posY), (posX + contador, posY + 0), 1)
                posX += contador
            elif y == 2:
                pygame.draw.line(ventana, ROJO, (posX, posY), (posX + 0, posY - contador), 1)
                posY -= contador
            elif y == 3:
                pygame.draw.line(ventana, ROJO, (posX, posY), (posX - contador, posY + 0), 1)
                posX -= contador
            else:
                pygame.draw.line(ventana, ROJO, (posX, posY), (posX + 0, posY + contador), 1)
                posY += contador
            contador += 1

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
def dibujarCirculos():

    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
       for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                    termina = True
            ventana.fill(BLANCO)
            angulo = 0
            for i in range(1, 13):
                x = 150 * cos(angulo)
                y = 150 * sin(angulo)
                pygame.draw.circle(ventana, ROJO, (400 + int(x), 400 + int(y)), 150, 2)
                angulo += pi / 6

            pygame.display.flip()
            reloj.tick(40)
    pygame.quit()
def dibujarParabolas():
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
            for x in range(0, 400, 15):
                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, x), (400 + x, 400),
                                 1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, x), (400 - x, 400),
                                 1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, 800 - x),
                                 (400 + x, 400), 1)

                pygame.draw.line(ventana, (randint(0, 255), randint(0, 255), randint(0, 255)), (400, 800 - x),
                                 (400 - x, 400), 1)

            pygame.display.flip()
            reloj.tick(40)
    pygame.quit()

def calcularValorPI(ultimoDivisor):
    suma = 0
    for x in range(1, ultimoDivisor+1):
        suma += 1 / (x**2)
    pi = sqrt(6 * suma)
    return pi

def calcularDivisibles():
    numero = 0
    for x in range(1000, 10000):
        if x % 19 == 0:
            numero += 1
    return numero

def imprimirPiramides():
    suma = 0
    for x in range(1, 10, 1):
        for y in range(x+1, 1, -1):
            suma += (10 ** y)//100
        print ("%d * 8 + %d = %d" % (suma, x, suma * 8 + x))
    print("\n")
    for i in range(0, 10, 1):
        num = 0
        for j in range(1, i+1, 1):
            num += 10**j
        num += 1
        print("%d * %d = %d" %(num, num, num * num))
def main():
    salir = False
    while not salir:
        print("""Tarea 5. Seleccione qué quiere hacer.
        1. Dibujar cuadros y círculos
        2. Dibujar espiral
        3. Dibujar círculos
        4. Dibujar parábolas
        5. Aproximar PI
        6. Contar divisibles entre 19
        7. Imprimir pirámides de números
        0. Salir""")
        respuesta = int(input("¿Qué desea hacer? "))


        if respuesta == 1:
            dibujarCuadrosYCirculos()
        elif respuesta == 2:
            dibujarEspiral()
        elif respuesta == 3:
            dibujarCirculos()
        elif respuesta == 4:
            dibujarParabolas()
        elif respuesta == 5:
            ultimoDivisor = int(input("Escriba el valor del último divisor: "))
            print("El valor aproximado de PI es:", calcularValorPI(ultimoDivisor))
        elif respuesta == 6:
                print("Hay",calcularDivisibles(), "números divisibles entre 19")
        elif respuesta == 7:
                imprimirPiramides()
        elif respuesta == 0:
            salir = True
        else:
            print("Error, escriba un número del 0 al 7")
main()