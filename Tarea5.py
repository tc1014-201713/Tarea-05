#encoding: UTF-8
#Autor: Joaquin Rios Corvera A01375441
#Muestra un menú con opciones de qué quiere hacer el usuario

import pygame
import random
import math

#Dimensiones
ANCHO = 800
ALTO = 800

#Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)

#Funcion que dibuja cuadrados y circulos con una separacion de 10px
def dibujarCuadradosCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        #Borra pantalla
        ventana.fill(BLANCO)

        #Dibujos
        esquina1 = 0
        esquina2 = 800
        radio = 10
        while esquina1 <= ANCHO/2:
            pygame.draw.rect(ventana, NEGRO, ((esquina1, esquina1), (esquina2, esquina2)), 1)
            esquina1 += 10
            esquina2 -= 20

        while radio <= 400:
            pygame.draw.circle(ventana, NEGRO, (400, 400), radio, 1)
            radio += 10
        pygame.display.update()
        reloj.tick(60)

#Dibuja muchas lineas en los 4 cuadrantes de una gráfica para simular parábolas
def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        # Borra pantalla
        ventana.fill(BLANCO)
        #Dibuja lineas de x a y con diferencia de 10
        for x in range (0, ANCHO//2+1, 10):
            color = (random.randint(0,255), random.randint(0,255), random.randint(0, 255))
            #Primer cuadrante
            pygame.draw.line(ventana, color, (400, x), (400+x, 400))
            #Segundo cuadrante
            pygame.draw.line(ventana, color, (400, x), (400-x, 400))
            #Tercer cuadrante
            pygame.draw.line(ventana, color, (400, 800-x), (400-x, 400))
            #Cuarto cuadrante
            pygame.draw.line(ventana, color, (400, 800-x), (400+x, 400))
        pygame.display.flip()
        reloj.tick(1)

#Dibuja lineas de largo creciente para crear una espiral cuadrada
def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        # Borra pantalla
        ventana.fill(BLANCO)

        # Dibujos
        coordenadas = []
        x = 400
        y = 400
        counter = 1

        while 0<x<800:
            coordenadas.append((x,y))
            if counter % 4 == 0:
                x = x + (5 * counter)
            elif counter % 4 == 1:
                y = y - (5 * counter)
            elif counter % 4 == 2:
                x = x - (5 * counter)
            else:
                y = y + (5 * counter)
            counter += 1
        pygame.draw.lines(ventana, NEGRO, False, coordenadas, 1)
        pygame.display.update()
        reloj.tick(1)

#Dibuja círculos de radio 150 tal que todos sus centros forman otro círculo
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        # Borra pantalla
        ventana.fill(BLANCO)

        # Dibujos
        for angulo in range (0, 360, 30):
            pygame.draw.circle(ventana, NEGRO, ((int(400+150*math.cos(math.radians(angulo)))), int((400+150*math.sin(math.radians(angulo))))), 150, 1)
        pygame.display.update()
        reloj.tick(1)


#Aproxima PI utilizando el valor dado por el usuario para el mayor denominador
def calcularPi(denominador):
    resultado = 0
    for i in range (1, denominador+1):
        resultado += 1/(i**2)
    pi = (6*resultado)**.5
    return pi

#Calcula la cantidad de números de 4 dígitos divisibles entre 29
def contarDivisible():
    contador = 0
    for i in range (1000, 10000):
        if i % 29 == 0:
            contador += 1
    return contador

#Realiza operaciones e imprime las píramides de números formadas con estas
def realizarPiramides():
    x = 0
    for i in range (1, 10):
        for y in range (0, i):
            x += 10**y
        resultado = ((x * 8) + i)
        print("%d * 8 + %d = %d" %(x, i, resultado))

    print("")

    x = 0
    for i in range (1,10):
        x += 10**(i-1)
        resultado = (x**2)
        print("%d * %d = %d"  %(x, x, resultado))

#Hace un menú para que el usuario pueda escoger qué acción quiere tomar
def main():
    correrMenu = 1
    while correrMenu:
        x = int(input('''
        Tarea 5. Seleccione qué quiere hacer:
        1. Dibujar cuadros y círculos
        2. Dibujar espiral
        3. Dibujar círculos
        4. Dibujar parábolas
        5. Aproximar PI
        6. Contar divisibles entre 29
        7. Imprimir pirámides de números
        0. Salir
        ¿Qué desea hacer? '''))
        print("")

        if x == 0:
            correrMenu = False
        elif x == 1:
            dibujarCuadradosCirculos()
        elif x == 2:
            dibujarEspiral()
        elif x == 3:
            dibujarCirculos()
        elif x == 4:
            dibujarParabolas()
        elif x == 5:
            denominador = int(input("Teclee el valor del divisor más grande: "))
            print("Valor aproximado de PI: ", calcularPi(denominador))
        elif x == 6:
            print("Hay %d números de 4 dígitos divisibles entre 29" %(contarDivisible()))
        elif x == 7:
            realizarPiramides()
        else:
            print("El número tiene que ser entre 0 y 7")
main()