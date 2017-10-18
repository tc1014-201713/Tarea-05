#encoding: UTF-8
#autor: Juan Sebastián Lozano Derbez
#Programa con menu

import pygame
import sys
from math import *


def hacercuarcir():  # Función para hacer círculos y cuadrados
    colorr = (155, 255, 229)
    FPS = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 0, 255))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        for radio in range(10, 390, 10):
            pygame.draw.circle(screen, colorr, (400, 400), radio, 2)

        for width in range(10, 390, 10):
            pygame.draw.rect(screen, colorr, (width, width, 800 - width * 2, 800 - width * 2), 2)

        FPS.tick(60)
        pygame.display.flip()


def hacerparabolas():  # función para hacer parábolas
    FPS = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 0, 255))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        for x in range(0, 400, 10):
            blu = (41, 253, 253)
            grin = (172, 242, 207)
            porpol = (176, 78, 233)
            darcgrin = (78, 233, 150)

            pygame.draw.line(screen, blu, (400, x), (400 - x, 400), 1)
            pygame.draw.line(screen, porpol, (400, x), (400 + x, 400), 1)
            pygame.draw.line(screen, grin, (400, 800 - x), (400 - x, 400), 1)
            pygame.draw.line(screen, darcgrin, (400, 800 - x), (400 + x, 400), 1)

        pygame.display.flip()
        FPS.tick(60)


def hacerlaberinto():
    colorr = (155, 255, 229)
    FPS = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 0, 255))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        posx = 400
        posy = 400

        for wub in range(1, 159):
            lub = wub % 4
            correr = (((wub % 2) + wub) // 2) * 10

            if lub == 1:
                pygame.draw.line(screen, colorr, (posx, posy), (correr + posx, posy), 2)
                posx += correr

            elif lub == 2:
                pygame.draw.line(screen, colorr, (posx, posy), (posx, posy - correr), 1)
                posy -= correr

            elif lub == 3:
                pygame.draw.line(screen, colorr, (posx, posy), (posx - correr, posy), 2)
                posx -= correr

            else:
                pygame.draw.line(screen, colorr, (posx, posy), (posx, correr + posx), 1)
                posy += correr

        pygame.display.flip()
        FPS.tick(60)


def hacercirculos():  # Función para hacer 12 círculos
    colorr = (155, 255, 229)
    FPS = pygame.time.Clock()

    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 0, 255))

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            grados = 0
            for varios in range(1, 13):
                ancho = cos(grados) * 150
                largo = sin(grados) * 150

                pygame.draw.circle(screen, colorr, (400 + int(ancho), int(largo) + 400), 150, 2)
                grados += pi / 6

        pygame.display.flip()
        FPS.tick(60)


def aproximarpi(numero):
    total = 0

    for valor in range(1, numero):
        total += (-1) ** (valor + 1) * ((1.0 / (valor * 2 + 1)))
    aprox = 4 * (1 - total)

    return aprox


def sacarveinteynueve():
    divible = 0
    for valor in range(1000, 9999):
        if valor % 29 == 0:
            divible += 1

    return divible


def hacerpiramides():
    numero = 0
    for valor1 in range(1, 10, 1):
        for valor2 in range(valor1, 1, -1):
            numero += (10 ** valor2 // 100)
        print("%d * 8 + %d = %d" % (numero, valor1, numero * 8 + valor1))

    for valor3 in range(0, 9, 1):
        numeroo = 0
        for valor4 in range(1, valor3 + 1, 1):
            numeroo += 10 ** valor4
        numeroo += 1
        print("%d * %d = %d" % (numeroo, numeroo, numeroo * numeroo))


def main():  # Función main donde se hace la selección de programa
    while True:
        selection = int(input("""Tarea 5. Seleccione qué quiere hacer:
          
1) Círculos y cuadrados
2) Parábolas
3) Laberinto
4) Círculos
5) Aproximación de Pi
6) Divisibles entre 29
7) Pirámides
8) Salir

Selección: """))

        if selection == 1:
            hacercuarcir()
        elif selection == 2:
            hacerparabolas()
        elif selection == 3:
            hacerlaberinto()
        elif selection == 4:
            hacercirculos()
        elif selection == 5:
            numero = int(input("Último divisor? :"))
            print("Valor aproximado de Pi: ", aproximarpi(numero))
        elif selection == 6:
            print("Hay", sacarveinteynueve(), "números que se pueden dividir entre 29")
        elif selection == 7:
            hacerpiramides()
        elif selection == 8:
            break


main()
