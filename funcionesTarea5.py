# Encoding: UTF-8
# Autor: Roberto Téllez Perezyera
"""
Este programa permite al usuario ver figuras en pygame o imprimir algunas cosas en la consola. Todo ello partiendo de
un menú donde se selecciona la opción deseada. En el mismo menú también se puede finalizar el programa, si el usuario
ya no quiere hacer nada.
"""

import pygame
from random import randint
import math

def dibujarCuadrosCirculos():
    #Se dibujan cuadrados y círculos en una ventana de Pygame
    ANCHO = 800              #Dimensiones de la ventana de Pygame
    ALTO = 800
    BLANCO = (255, 255, 255) #Color fondo

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock() #limita FPS
    termina = False         #¿Terminó la ejecución?

    while not termina:      #Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        #En la pantalla
        ventana.fill(BLANCO)
        negro = (0,0,0)

        for x in range (10, 801, 10):
            pygame.draw.rect(ventana, negro, (x, x, 800-2 * x, 800-2 * x), 1)
        for y in range (10, 801, 10):
            pygame.draw.circle(ventana, negro, (ANCHO//2, ALTO//2), y, 2)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


def dibujarParabolas():
    #Dibuja una figura con parábolas (en realidad rectas) que cambian de color
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

        for x in range (0,401, 10):
            random = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, random, (400, x), (400+x, 400), 1)

            pygame.draw.line(ventana, random, (400, x), (400-x, 400), 1)

            pygame.draw.line(ventana, random, (400, 800-x), (400+x, 400), 1)

            pygame.draw.line(ventana, random, (400, 800-x), (400-x, 400), 1)

        pygame.display.flip()
        reloj.tick(5)

    pygame.quit()


def dibujarEspiral():
    #Dibuja un 'espiral cuadrado'
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


def dibujarCirculos():
    #Dibuja una figura hecha con círculos
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)

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
        for n in range (1, 13):
            x = 150*math.cos(angulo)
            y = 150*math.sin(angulo)
            pygame.draw.circle(ventana, NEGRO, (400 + int(x), 400 + int(y)), 150, 2)
            angulo += math.pi/6

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


def aproximarPi(ultimoDiv):
    #Aproxima a pi con un divisor dado por el usuario. Cuando más grande, más cercana la aproximación
    n = 0
    for x in range (1, ultimoDiv+1):
        n += 1/(x**2)
    ans = math.sqrt(6 * n)
    return ans


def contarDivisibles():
    #Regresa cualquier número de cuatro dígitos que sea divisible entre 29
    n = 0
    for x in range (1000, 10000):
        if x % 29 == 0:
            n += 1
            return n


def imprimirPiramides():
    #Imprime operaciones que forman 'pirámides de números'
    suma = 0
    for x in range (1, 10, 1):
        for y in range (x+1, 1, -1):
            suma += (10**y) // 100
        print(suma, "* 8 + ", x, " = ", suma * 8 + x)
    print("----------------------------")

    for n in range (0, 9, 1):
        numero = 0
        for i in range (1, n+1, 1):
            numero += 10**i
        numero += 1
        print(numero, " * ", numero, " = ", numero*numero)


def main():
    #Menú principal de la tarea. Aquí se puede correr todos los programas (ejercicios). Termina hasta que el usuario lo
    #indica
    termina = False
    while not termina:

        print("""Bienvenido a mi tarea 5. Seleccione qué quiere hacer:
    1. Dibujar cuadros y círculos
    2. Dibujar parábolas
    3. Dibujar espiral
    4. Dibujar círculos
    5. Aproximar PI
    6. Contar divisibles entre 29
    7. Imprimir pirámides de números
    0. Salir
    """)

        respuestaUsuario = int(input("¿Qué desea hacer? "))

        if respuestaUsuario == 0:
            termina = True
        elif respuestaUsuario == 1:
            dibujarCuadrosCirculos()
        elif respuestaUsuario == 2:
            dibujarParabolas()
        elif respuestaUsuario == 3:
            dibujarEspiral()
        elif respuestaUsuario == 4:
            dibujarCirculos()
        elif respuestaUsuario == 5: #Aproximar pi
            ultimoDiv = int(input("¿Cuál es el último divisor?"))
            print ("Pi es aproximadamente", aproximarPi(ultimoDiv))
        elif respuestaUsuario == 6:
            print(contarDivisibles(), "números de cuatro dígitos son divisibles entre 29")
        elif respuestaUsuario == 7:
            imprimirPiramides()
        else:
            print("Escriba un número válido, por favor")


main()
