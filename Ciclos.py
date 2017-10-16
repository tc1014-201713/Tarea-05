#encoding: UTF-8
#Autor: Leonardo Castillejos Vite
#Programa en el que el usuario selecciona una de 7 opciones para dibujar figuras u otras funciones

import pygame
from random import randint
from math import pi
from math import cos
from math import sin
Ancho = 800
Alto = 800
Blanco = (255,255,255)

#Sirve como menu para las demás funciones
def main():
    decision = 8
    while decision != 0:
        print("""Tarea 5. Seleccione qué quiere hacer.
             1. Dibujar cuadros y círculos
             2. Dibujar espiral
             3. Dibujar círculos
             4. Dibujar parábolas
             5. Aproximar PI
             6. Contar divisibles entre 19
             7. Imprimir pirámides de números
             0. Salir""")
        decision = int(input("¿Qué desea hacer?"))
        if decision == 1:
            dibujarCuadradosyCirculos()
        elif decision == 2:
            dibujarEspiral()
        elif decision == 3:
            dibujarCirculos()
        elif decision == 4:
            dibujarParabolas()
        elif decision == 5:
            divisiones = int(input("Teclea el último divisor: "))
            aproxPi = aproximarPi(divisiones)
            print("El valor aproximado de pi es: ", aproxPi)
        elif decision == 6:
            cuenta = contarDivisibles()
            print("La cantidad de números de 4 dígitos divisibles entre 19 es: ", cuenta)
        elif decision == 7:
            imprimirPiramide()



# Dibuja cuadrados con 10 pixeles de separación y círculos dentro de esos cuadrados
def dibujarCuadradosyCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((Ancho,Alto))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)

        x = 0
        contador = 0
        while contador <= 390:
            x += 1
            pygame.draw.rect(ventana,(0,0,0),(399 - (10*x-1),399 - (10*x-1),(20*x),(20*x)),1)
            pygame.draw.circle(ventana,(0,0,0),(400, 400), (10*x), 1)
            contador = 10*x
            pygame.display.flip()
            reloj.tick(5)

    pygame.quit()

#Utiliza lineas para hacer un cuadrado en espiral con separación de 10 pixeles
def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)
        x = 1
        while (390 - 10 * (x -1)) >= 0 or 410 + 10 * (x-1) <= 800:
            pygame.draw.line(ventana,(0,0,0),((400 - 10 * (x -1)),(400 + 10 * (x -1))),((405 + 10*(x - 1)),(400 + 10 * (x -1))),1)
            pygame.draw.line(ventana,(0,0,0),((405 + 10*(x -1)),(400 + 10 * (x - 1))),((405 + 10 * (x - 1)),(390-10*(x - 1))),1)
            pygame.draw.line(ventana,(0,0,0),((405 + 10 * (x - 1)),(390 - 10 * (x -1))),((390 - 10 * (x -1)),(390 - 10 *(x -1))),1)
            pygame.draw.line(ventana,(0,0,0),((390 -10 * (x - 1)),(390 - 10 * (x - 1))), ((390 - 10 * (x -1)),(410 + 10 * (x-1))),1)
            x += 1
            pygame.display.flip()
            reloj.tick(5)

    pygame.quit()


#Dibuja parábolas con colores aleatorios para crear un patron
def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    colorA = (randint(0,255),randint(0,255),randint(0,255))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)

        for contador in range(1, 81):
            pygame.draw.ellipse(ventana,(randint(0,255),randint(0,255),randint(0,255)),[395 - 5 * (contador -1) , 0 + 5 * (contador -1), 10 + 10 * (contador - 1),800 - 10 * (contador - 1)],1)
            reloj.tick(40)
        pygame.display.flip()
    pygame.quit()

#Crea 12 círculos con 30° de separación para formar un patron
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    radio = 150
    x = 400
    y = 400
    desviacionx = 150
    desviaciony = 0


    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(Blanco)
        for circulos in range(1,13):
            pygame.draw.circle(ventana,(0,0,0),((x + desviacionx), (y - desviaciony)), radio, 1)
            desviacionx = int(150 * sin((pi * circulos)/6))
            desviaciony = int(150 * cos((pi * circulos)/6))

            reloj.tick(40)
        pygame.display.flip()
    pygame.quit()


    pygame.quit()

#El usuario da un denominador y el programa aproxima el valor de pi sumando la fracción del 1 hasta el denominador elegido
def aproximarPi(divisiones):
    aproxPi = 0
    for divisor in range(1, (divisiones + 1)):
        aproxPi += 1/divisor**2
    aproxPi = aproxPi * 6
    aproxPi = aproxPi ** 0.5
    return aproxPi

# Da la cantidad de números que divisibles entre 19 que están entre 1000 y 9999
def contarDivisibles():
    cuenta = 0
    for i in range (1000,10000):
        if i % 19 == 0:
            cuenta += 1
    return cuenta


# Imprime una pirámide de números siguiendo patrones
def imprimirPiramide():
    num1 = 1
    num2 = 1
    for i in range(1,10):
        resultado1 = num1 * 8 + i
        print("%d*8+%d=%d" %(num1, i, resultado1))
        resultado2 = num2 ** 2
        num2 += 10 ** i
        num1 += num2
    print("")
    num2 = 1
    for x in range(1,10):
        resultado2 = num2 * num2
        print("%d*%d=%d" % (num2, num2, resultado2))
        num2 += 10 ** x


main()