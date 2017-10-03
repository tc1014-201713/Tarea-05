# encoding: UTF_8
# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
#Juntar todos los ejercicios para que el usuario pueda ver lo que quiera

#imports

import pygame
import random
import math

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

#Ventana
ventana = (ANCHO, ALTO)

#colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

#dibuja el primer patron a)
def a():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro)
        for distancia in range(10, 400, 10):
            pygame.draw.circle(ventana, blanco, (400, 400), (distancia), 1)   # dubuja el circulo
            pygame.draw.rect(ventana, blanco,((distancia), (distancia), (800 - (distancia * 2)), (800 - (distancia * 2))), 1) #dibuja el cuadrado
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()

#dibuja el 2 patron b)
def b():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro)
        for distancia in range(0, 405, 5):
            # color
            RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #este colo tiene que ir aqui apra que se actualice y cambie cada vez que se pida
            #dibujo
            pygame.draw.line(ventana, RANDOM, (400 - distancia, 400), (400, 0 + distancia))  # dibuja lineas en distinto plano carteciano
            pygame.draw.line(ventana, RANDOM, (400 + distancia, 400), (400, 0 + distancia))
            pygame.draw.line(ventana, RANDOM, (400 + distancia, 400), (400, 800 - distancia))
            pygame.draw.line(ventana, RANDOM, (400 - distancia, 400), (400, 800 - distancia))

        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()
#dubuja el 3 patron c)
def c():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro)
        for d in range(0, 400, 10):
            pygame.draw.line(ventana, blanco, (405 - d, 400 + d), (405 + d, 400 + d)) # dibuja lineas a distinta distancia
            pygame.draw.line(ventana, blanco, (405 + d, 400 + d), (405 + d, 395 - d))
            pygame.draw.line(ventana, blanco, (405 + d, 395 - d), (395 - d, 395 - d))
            pygame.draw.line(ventana, blanco, (395 - d, 395 - d), (395 - d, 410 + d))
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()
#d
def d():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(negro)
        for d in range(0, 330, (int(360 / 11))): #hace 12 ángulos, 360 / 12
            pygame.draw.circle(ventana, blanco, (int((math.cos(d) * 150) + 400), int((math.sin(d) * 150) + 400)), (150), 1) #dibuja el circulo
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()
#funcion de pi
def calcularpi():
    x = 0
    for i in range(1, 100000, 1):
        x += (1/(i**2))
    x = (x * 6) ** (1/2)
    return(x)
#divisibles entre 29
def dividir(numero):
    x = 0
    for i in range(0, 10000000):
        if (i % numero) == 0:
            x += 1
    return(x)
#escribir numero
def imprimirNumero(): # imprime la serie de numeros que piden
    for n in range(1,10):
        print((str(numero(n))) + " * 8 + " + (str(n)) + " = " + (str((int(numero(n))) * 8 + n))) #serie de 123456789
    for n in range(1,10):
        print(((str(1)) * n) + " * " + ((str(1)) * n) + " = " + (str((int((str(1)) * n)) * (int((str(1)) * n))))) #serie 1111111...
def numero(n): # hace el numero: 123456789
    x = ""
    for i in range(1, (n +1)):
        x = str(x) + (str(i)) # junta el numero donde esta n al anterior
    return(x)
# funcion main
def main():
    jugar = 1
    while jugar == 1:
        accion = int(input(""" Tarea 5. Seleccione qué quiere hacer.
        1. Dibujar cuadros y círculos
        2. Dibujar espiral
        3. Dibujar círculos
        4. Dibujar parábolas
        5. Aproximar PI
        6. Contar divisibles entre 19
        7. Imprimir pirámides de números
        0. Salir
        ¿Qué desea hacer?"""))
        if accion == 0:
            jugar = 0
        elif accion == 1:
            a()
        elif accion == 2:
            b()
        elif accion == 3:
            c()
        elif accion == 4:
            d()
        elif accion == 5:
            print(calcularpi())
        elif accion == 6:
            print(dividir(29))
        elif accion == 7:
            print(imprimirNumero())
        else:
            print("Debes de escribir un número válido")  #por si no pones un número válido
main()