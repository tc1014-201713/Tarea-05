#encoding: utf-8
#Autor: Diego Armando Pérez González
#descripcción: Este es un programa funciones diferentes que tiene como objetivo que el usuario interactue con un menú para que pueda ver el resultado de cada función

import pygame

import math

import random

#dimensiones de la pantalla
Ancho = 800
Alto = 800

#colores
Blanco = (255,255,255)
Negro = (0,0,0)


def dibujarCuadradosyCirculos():

    pygame.init() #inicializa pygame
    ventana = pygame.display.set_mode((Ancho,Alto)) #Crea la ventana de dibujo
    reloj = pygame.time.Clock() #limita los fps. se debe de bajar para reducir la sobrecarga de la pc
    termina = False #para saber que se termina la ejecución

    while not termina:
        # procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # dieron click en el boton salir
                termina = True

        # borra la pantalla
        ventana.fill(Blanco)

        for t in range(1, 400, 10):
            pygame.draw.circle(ventana, Negro, (Ancho//2, Alto//2), t, 1) #dibuja al circulo
            pygame.draw.rect(ventana, Negro, (t, t, Ancho - t * 2, Alto - t * 2), 1) #dibuja rectangulo

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(40)  # 40fps

    pygame.quit()  # termina pygame

def dibujarEspiral():

    pygame.init() #inicializa pygame
    ventana = pygame.display.set_mode((Ancho, Alto)) #Crea la ventana de dibujo
    reloj = pygame.time.Clock() #limita los fps. se debe de bajar para reducir la sobrecarga de la pc
    termina = False #para sabepygame.draw.line(ventana, Negro, (0 + u, 10 + u), (0 + u, 10 + u), 1)  # líneas vetricalesr que se termina la ejecución

    while not termina:
        #procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #dieron click en el boton salir
                termina = True

        #borra la pantalla
        ventana.fill(Blanco)

        for u in range(0, 400, 10):

            pygame.draw.line(ventana, Negro, (Ancho-u, Alto-u), (0+u, Alto-u), 1) #líneas Horizontales hacia abajo
            pygame.draw.line(ventana, Negro, (0 + u, 10 + u), (Ancho-(u + 10), 10 + u), 1)  #líneas Horizontales hacia arriba
            pygame.draw.line(ventana, Negro, (0 + u, Alto - u), (0 + u, 10 + u), 1) #líneas vetricales hacia la izquierda
            pygame.draw.line(ventana, Negro, (Ancho-u, Alto-u), (Ancho-u, 10 + u - 10),1) #líneas verticales hacia la derecha

        pygame.display.flip() #Actualiza los trazos
        reloj.tick(40)  #40fps

    pygame.quit() #termina pygame

def dibujarCirculosMandala():

    pygame.init()  # inicializa pygame
    ventana = pygame.display.set_mode((Ancho, Alto))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # limita los fps. se debe de bajar para reducir la sobrecarga de la pc
    termina = False  # para sabepygame.draw.line(ventana, Negro, (0 + u, 10 + u), (0 + u, 10 + u), 1)  # líneas vetricalesr que se termina la ejecución

    while not termina:
        # procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # dieron click en el boton salir
                termina = True

        # borra la pantalla
        ventana.fill(Blanco)

        for v in range(0, 330, 32): #angulo max de 330 poque el 360 que se toma en cuenta en (0,0). ademas queremos: 360/11 =32.72
            pygame.draw.circle(ventana, Negro, (int(math.cos(v) * 150 + Ancho//2), int((math.sin(v) * 150) + Alto//2)), 150, 1)

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(40)  # 40fps

    pygame.quit()  # termina pygame

def dibujarParabolas():

    pygame.init()  # inicializa pygame
    ventana = pygame.display.set_mode((Ancho, Alto))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # limita los fps. se debe de bajar para reducir la sobrecarga de la pc
    termina = False  # para sabepygame.draw.line(ventana, Negro, (0 + u, 10 + u), (0 + u, 10 + u), 1)  # líneas vetricalesr que se termina la ejecución

    while not termina:
        # procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # dieron click en el boton salir
                termina = True

        # borra la pantalla
        ventana.fill(Blanco)

        for w in range(0, 400, 10):  # es una separación de 10 pix por 40 lineas que genera
            Random = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

            pygame.draw.line(ventana, Random, (Ancho//2 + w, Alto//2), (Alto//2, w), 1) #primer cuadrante
            pygame.draw.line(ventana, Random, (Ancho // 2 - w, Alto // 2), (Alto // 2, w), 1) #segundo cuadrante
            pygame.draw.line(ventana, Random, (Ancho // 2, Alto - w), (Ancho // 2 - w, Alto//2), 1) #terer cuadrante
            pygame.draw.line(ventana, Random, (Ancho // 2, Alto - w), (Ancho // 2 + w, Alto//2), 1) #cuarto cuadrante

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(40)  # 40fps

    pygame.quit()  # termina pygame

def aproximarPi():

    incremento = 0
    valor =(int(input("Dame el valor que deseas:  ")))

    for x in range (1, valor+1):
        incremento = incremento +(1/x**2)

    pi=(incremento*6) ** (1/2)

    return pi

def contarDivisiblesEntre29():

    n = 0

    for y in range(1000, 10000, 1):

        if y % 29 == 0:
            n += 1

    return n

def imprimirPiramides():

    incremento1 = 1

    for z in range (1, 10,1): #Primera columna
        resultado = incremento1 * 8 + z
        print(incremento1, "* 8 +", z, "=", resultado)

        incremento1 = (incremento1 * 10) + (z +1)

    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    incremento2 = 1

    for a in range (1, 10, 1): #Segunda columna
        resultado2 = incremento2 * incremento2
        print(incremento2, "*", incremento2, "=", resultado2)

        incremento2 = (incremento2 * 10) + (1)

def main():
    print("Tarea 5. Seleccione que quiere hacer.")

    print('''
    1  Dibujar cuadros y círculos
    2  Dibujar espiral
    3  Dibujar círculos
    4  Dibujar parábolas
    5  Aproximar PI
    6  Contar divisibles entre 29
    7  Imprimir pirámides de números
    0. Salir''')

    print("")

    eleccion = int(input("¿Qué deseas hacer?: "))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    while eleccion >= 0:

        if eleccion == 1:
            dibujarCuadradosyCirculos()
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion == 2:
            dibujarEspiral()
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion == 3:
            dibujarCirculosMandala()
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion == 4:
            dibujarParabolas()
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion == 5:
            print(aproximarPi())
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion == 6:
            print("Los números divisibles entre 29 son: ", contarDivisiblesEntre29())
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion == 7:
            imprimirPiramides()
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion >= 8:
            print("Solo se puede del 1 al 7")
            print("")
            eleccion = int(input("¿Qué deseas hacer?: "))
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        elif eleccion == 0:
            print("Programa Terminado")
            break


main()