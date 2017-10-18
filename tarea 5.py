# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
from math import radians
from math import cos
from math import sin
import random

ANCHO = 800
ALTO = 800
BLANCO = (255,255,255)
NEGRO = (0,0,0)
def trazarParabola():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(NEGRO)

        for altura in range(0, 401, 10):
            pygame.draw.line(ventana,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(ANCHO//2,altura),(ALTO//2+altura,ANCHO//2),1)
            pygame.draw.line(ventana,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(ANCHO//2,altura),(ALTO//2-altura,ANCHO//2),1)
            pygame.draw.line(ventana,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(ANCHO//2,ALTO-altura),(ALTO//2-altura,ANCHO//2),1)
            pygame.draw.line(ventana,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(ANCHO//2,ALTO-altura),(ALTO//2+altura,ANCHO//2),1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def trazarCirculo1():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        for i in range(1, 401, 10):
            pygame.draw.circle(ventana,(NEGRO),(ALTO//2,ANCHO//2),i,1)
            pygame.draw.rect(ventana,(NEGRO),(i,i,(ANCHO)-2*i,(ALTO)-2*i),1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def trazarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        x = ANCHO/2
        y1 = ALTO/2
        a = ANCHO/2+10
        y2 = ALTO/2
        c = 20
        for i in range(0,401,10):
            pygame.draw.line(ventana,NEGRO,(x,y1),(a,y2),2)
            x = a
            y1 = y2
            a = x
            y2 = y1 - c
            c += 5

            pygame.draw.line(ventana, NEGRO, (x, y1), (a, y2), 2)
            x = a
            y1 = y2
            a = x - c
            y2 = y1
            c +=5

            pygame.draw.line(ventana, NEGRO, (x, y1), (a, y2), 2)
            x = a
            y1 = y2
            a = x
            y2 = y1 + c
            c +=5

            pygame.draw.line(ventana, NEGRO, (x, y1), (a, y2), 2)
            x = a
            y1 = y2
            a = x +c
            y2 = y1


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def trazarCirculo2():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for i in range(0, 360, 30):
            pygame.draw.circle(ventana,NEGRO,(int(ANCHO//2+150*(cos(radians(i)))),int(ALTO//2-150*(sin(radians(i))))),150,2)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def calcularPi(n):
    suma = 0
    for i in range(1,n+1):
        suma = suma + 1/(i**2)
        Total = (suma*6)**.5
    return Total

def calcularNumerosEntre29():
    cn = 0
    for i in range(1000, 10000, 1):
        if i % 29 == 0:
            cn += 1
    print(cn)

def calcularPiramides():
    x = 1
    n = 1
    for i in range(9):
        print(x, "* 8 +",n,"=", (x*8+n))
        n = n + 1
        x = x * 10 + n

    x = 1
    for i in range(9):
        print(x,"*",x,"=", x **2)
        x = x * 10 + 1

def main():
    opcion = -1
    while opcion != 0:
        print("0. Salir")
        print("1. Dibujar cuadros y circulos")
        print("2. Dibujar espiral")
        print("3. Dibujar círculos")
        print("4. Dibujar parábolas")
        print("5. Aproximar Pi")
        print("6. Contar divisibles entre 29")
        print("7. Imprimir pirámides de números")
        opcion = int(input("¿Qué desea hacer? "))
        if opcion == 1:
            trazarCirculo1()
        elif opcion == 2:
            trazarEspiral()
        elif opcion == 3:
            trazarCirculo2()
        elif opcion == 4:
            trazarParabola()
        elif opcion == 5:
            n = int(input("Valor del denominador: "))
            print(calcularPi(n))
        elif opcion == 6:
            calcularNumerosEntre29()
        elif opcion == 7:
            calcularPiramides()
        elif opcion == 0:
            print("Termina programa")

main()