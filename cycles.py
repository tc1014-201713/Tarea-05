#encoding: utf-8
#coded by: Jordan
#multile option menu, described in pdf

import pygame
from random import randint
from math import *

#screen dimensions
screenWidth = 800
screenHeight = 800
#colors
black = (0, 0, 0)
white = (255, 255, 255)

def drawSquareCircle():
    pygame.init()
    window = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    quitGame = False

    while not quitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True

        window.fill(white)
        height = screenHeight
        width = screenWidth
        for i in range(10,800,10):
            width = (width - 20)
            height = (height - 20)
            pygame.draw.rect(window, black, (i, i, width, height), 2)
        for i in range(10, 400, 10):
            pygame.draw.circle(window, black, (screenWidth // 2, screenHeight // 2), i, 2)

        pygame.display.flip()
        clock.tick(1)

    pygame.quit()

def drawParable():
    pygame.init()
    window = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    quitGame = False

    while not quitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True

        window.fill(white)
        b = 0
        a = 800

        for i in range(400, 0, -10):
            pygame.draw.line(window, (randint(0,255), randint(0,255), randint(0,255)), (b, 400), (400, i), 2)
            b = b + 10
        for i in range(400, 0, -10):
            pygame.draw.line(window, (randint(0,255), randint(0,255), randint(0,255)), (a, 400), (400, i), 2)
            a = a - 10
        b = 0
        for i in range(400, 800, 10):
            pygame.draw.line(window, (randint(0,255), randint(0,255), randint(0,255)), (b, 400), (400, i), 2)
            b = b + 10
        a = 800
        for i in range(400, 800, 10):
            pygame.draw.line(window, (randint(0,255), randint(0,255), randint(0,255)), (a, 400), (400, i), 2)
            a = a - 10

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

def drawLabyrinth():
    pygame.init()
    window = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    quitGame = False

    while not quitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True

        window.fill(white)

        x = 400
        y = 400
        for i in range(0, 200, 5):
            ay = y - (i * 2)
            bx = x - (i * 2)
            by = y + (i * 2)
            ady = y + (i * 2)
            bdx = x + (i * 2) + 5
            bdy = y - (i * 2) - 10
            pygame.draw.line(window, black, (bx, ady), (bdx, ady), 1)
            pygame.draw.line(window, black, (bdx, ady), (bdx, bdy), 1)
            pygame.draw.line(window, black, (bdx-10, ay), (bx, ay), 1)
            pygame.draw.line(window, black, (bx, ay), (bx, by), 1)

        pygame.display.flip()
        clock.tick(1)
    pygame.quit()
    
def drawCircles():
    pygame.init()
    window = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    quitGame = False

    while not quitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True

        window.fill(white)
        r = 150
        angle = 0
        for i in range(12):
            x = int(400 + r * cos(angle))
            y = int(400 + r * sin(angle))
            pygame.draw.circle(window, black, (x, y), r, 1)
            angle += pi/6

        pygame.display.flip()
        clock.tick(1)
    pygame.quit()

def getNearPi(number):
    acum = 0
    for i in range(1, number + 1):
        acum += (1 / (i*i))
    acum = sqrt((acum * 6))
    return acum

def countDivisibleBy29():
    count = 0
    for i in range(1000, 9999, 1):
        if i % 29 == 0:
            count += 1
    return count

def builtPyramid():
    a = 1
    c = 2
    d = 1
    pyramid = ""
    for i in range(1, 10, 1):
        b = a * 8 + i
        pyramid += ("%d * 8 + %d = %d\n" % (a, i, b))
        a = a * 10 + c
        c += 1

    pyramid += "\n"

    for i in range(9):
        b = d * d
        pyramid += ("%d * %d = %d\n" % (d, d, b))
        d = d * 10 + 1

    return pyramid

def main():
    print("""
Tarea 5. Seleccione qué quiere hacer.
--------------------------------------
1. Dibujar cuadros y círculos
2. Dibujar espiral
3. Dibujar círculos
4. Dibujar parábolas
5. Aproximar π
6. Contar divisibles entre 29
7. Imprimir pirámides de números
0. Salir
--------------------------------------""")
    while 1:
        opt = int(input("¿Qué desea hacer? : "))
        if opt < 0 or opt > 7:
            print("El número %d no es una opción válida. " % opt)
        elif opt == 0:
            print("Finalizando. ")
            break
        else:
            if opt == 1:
                drawSquareCircle()
            if opt == 2:
                drawLabyrinth()
            if opt == 3:
                drawCircles()
            if opt == 4:
                drawParable()
            if opt == 5:
                number = getNearPi(int(input("Ingresa un número : ")))
                print("La aproximación a π sería : %.8f" % number)
            if opt == 6:
                number = countDivisibleBy29()
                print("%d números de 4 dígitos son divisibles entre 29." % number)
            if opt == 7:
                pyramid = builtPyramid()
                print(pyramid)
            if opt == 0:
                break
main()
