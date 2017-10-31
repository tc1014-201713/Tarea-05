# encoding: UTF-8
# Autor: Dora Gabriela Lizárraga González - A01229599
# Con este programa se podrá seleccionar de entre varias opciones en un menú para ejecutar diferentes funciones

import pygame
from random import randint
from math import *

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Variables definidas que se usarán en varias funciones
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
x = ANCHO // 2
y = ALTO // 2

# Con esta función se pueden dibujar circulos dentro de cuadrados repetidamente
def dibujarCirculos_Cuadrados():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for separacion in range (2, ALTO, 10):
            pygame.draw.rect(ventana, NEGRO,(x - (separacion // 2), y - (separacion // 2), separacion, separacion), 1)
        for separacion in range (1, (y)+ALTO//100, 10):
            pygame.draw.circle(ventana, NEGRO, (x, y), separacion, 1)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()

# Con esta función se puede dibujar una espiral cuadrada que abarca toda la pantalla
def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for cambio in range(0, y, 10):
            pygame.draw.line(ventana, NEGRO, ((x + 5) - cambio, y + cambio), ((x + 5) + cambio, y + cambio), 1)
            pygame.draw.line(ventana, NEGRO, ((x + 5) + cambio, y + cambio), ((x + 5) + cambio, (y - 5) - cambio), 1)
            pygame.draw.line(ventana, NEGRO, ((x + 5) + cambio, (y - 5) - cambio), ((x - 5) - cambio, (y - 5) - cambio), 1)
            pygame.draw.line(ventana, NEGRO, ((x - 5) - cambio, (y - 5) - cambio), ((x - 5) - cambio, (y + 10) + cambio), 1)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()

# Con esta función se pueden dibujar 12 círculos con una separación equivalente
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for separacion in range(0, 12):
            radio = 150
            angulo = (pi / 6) * separacion
            xCirc = int((cos(angulo)) * 150)
            yCirc = int((sin(angulo)) * 150)
            pygame.draw.circle(ventana, NEGRO, (x + xCirc, y + yCirc), radio, 1)
        pygame.display.flip()
        reloj.tick(5)
    pygame.quit()

# Con esta función se pueden dibujar lineas que simulen una estrella colorida
def dibujarParabolas_Color():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for cambio in range(0, y, 10):
            COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, COLOR, (cambio, y),(x, y + cambio))
            pygame.draw.line(ventana, COLOR, (ANCHO - cambio, y),(x, y + cambio))
            pygame.draw.line(ventana, COLOR, (ANCHO - cambio, y),(x, y - cambio))
            pygame.draw.line(ventana, COLOR, (cambio, y),(x, y - cambio))
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

# Con esta función se puede calcular un valor aproximado a pi
def calcularPi(numero):
    acumulador = 0
    for x in range(1, numero + 1):
        acumulador += 1 / (x ** 2)
    pi = (acumulador * 6) ** 0.5
    return pi

# Con esta función se calculan cuantos números divisibles entre 19 de 4 cifras existen
def calcularNumeros_Divisibles():
    acumulador = 0
    for contador in range (1000, 10000):
        if contador%19 == 0:
            acumulador+= 1
    return acumulador

# Con esta función se calculan los valores para imprimir dos piramides de valores
def calcularPiramides():
    acumulador = 0
    for contador in range(9):
        contador += 1
        acumulador = (acumulador * 10) + contador
        print(acumulador, "* 8 +", contador, "=", (acumulador * 8 + contador))
    print("")
    acumulador = 1
    for contador in range(9):
        print(acumulador, "*", acumulador, "=", acumulador**2)
        acumulador = acumulador * 10 + 1

# Función principal; en esta se leen valores y se ejecutan otras funciones
def main():
    print("Seleccione qué quiere hacer.""\n"
                "1. Dibujar cuadrados y circulos ""\n"
                "2. Dibujar espiral""\n"
                "3. Dibujar círculos""\n"
                "4. Dibujar parábolas ""\n"
                "5. Aproximar PI ""\n"
                "6. Contar divisibles entre 19""\n"
                "7. Imprimir pirámides de números ""\n"
                "0. Salir""\n")
    opcion = 1
    while opcion > 0:
        opcion = int(input("Intoduzca opción: "))
        if opcion == 1:
            dibujarCirculos_Cuadrados()
            print(" ")
        elif opcion == 2:
            dibujarEspiral()
            print(" ")
        elif opcion == 3:
            dibujarCirculos()
            print(" ")
        elif opcion == 4:
            dibujarParabolas_Color()
            print(" ")
        elif opcion == 5:
            numero = int(input("Introduzca un número para acercar a pi: "))
            calcularPi(numero)
            print("El aproximado a pi da: ", calcularPi(numero))
            print(" ")
        elif opcion == 6:
            acumulador = calcularNumeros_Divisibles()
            print("Hay", acumulador, "números de cuatro cifras divisibles entre 19.")
            print(" ")
        elif opcion == 7:
            calcularPiramides()
            print(" ")
        elif opcion > 7:
            print("Elija un número válido.")
            print(" ")
    print("El programa ha sido terminado.")

main()