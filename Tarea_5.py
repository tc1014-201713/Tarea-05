# encoding: UTF-8

# Autor: MARIA FERNANDA TORRES VELAZQUEZ A01746537

# El siguiente programa, recibe un numero entre 0 y 7 para ejecutar una funcion o salir del programa

import pygame
from random import randint
import math



# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO= (0,0,0)


def dibujarA(): #Funcion que dibuja cuadros y circulos con una separacion de 10 pixeles
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)

        #Dibujar cuadrados
        for x in range (10,400,10):
            pygame.draw.rect(ventana, NEGRO, (x, x, ANCHO -(x*2), ALTO - (x*2)), 2)

        #Dibujar circulos
        for restaRadio in range (10,400,10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), ((ANCHO // 2) -restaRadio),2)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps
    pygame.quit()   # termina pygame




def dibujarB(): #Funcion que dibuja parabolas con separacion de 10 pixeles
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)


        for x in range(0, (ALTO // 2) + 1, 10):
            shuffle = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, shuffle, (x, ALTO // 2),(ANCHO // 2, ALTO // 2 + x))
            pygame.draw.line(ventana, shuffle, (ANCHO - x, ALTO // 2),(ANCHO // 2, ALTO // 2 + x))
            pygame.draw.line(ventana, shuffle, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x))
            pygame.draw.line(ventana, shuffle, (x, ALTO // 2),(ANCHO // 2, ALTO // 2 - x))


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps
    pygame.quit()   # termina pygame


def dibujarC(): #Funcion que dibuja espiral cuadricular
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)

        for x in range(0, 400, 10):
            for x in range(0, 400, 10):
                pygame.draw.line(ventana, NEGRO, (405 + x, 400 - x), (405 - x, 400 - x))
                pygame.draw.line(ventana, NEGRO, (405 - x, 400 - x), (405 - x, 395 + x))
                pygame.draw.line(ventana, NEGRO, (405 - x, 395 + x), (395 + x, 395 + x))
                pygame.draw.line(ventana, NEGRO, (395 + x, 395 + x), (395 + x, 410 - x))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps
    pygame.quit()   # termina pygame


def dibujarD (): # Funcion que dibuja 12 circulos entrelazados

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        ventana.fill(BLANCO)

        for grados in range(1, 13):
            pygame.draw.circle(ventana, NEGRO, (int(ANCHO // 2 + 150 * math.cos(math.pi * grados / 6)),int(ALTO // 2 + 150 * math.sin(math.pi * grados / 6))),150, 1)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps
    pygame.quit()   # termina pygame


def aproximarPI(divisor): #Funcion que aproxima a PI**2/6
        operacion = 0
        for x in range(1, divisor + 1):
            operacion = operacion + 1 / (x ** 2)
            pi = (6 * operacion) ** 0.5
        return pi

def cuatroDigitos(): #Calcula numeros de 4 digitos divisibles entre 29
    contador = 0
    for i in range(1000,10000):
        if i % 29 == 0:
            contador = contador + 1
    print("Hay %d de 4 digitos múltiplos de 29" %contador)

def piramides(): #Crea piramides de numeros
    cont = 0
    contador = 0
    for multiplo in range(1, 10): #Primer piramide
        cont = cont * 10 + multiplo
        result = cont * 8 + multiplo
        print(cont, "*", "8" , "+", multiplo , "=", result)
    print("")
    print("")
    print("")
    for x in range (1,10): #Segunda piramide
        contador = contador*10 + 1
        potencia = contador **2
        print (contador, "*", contador,"=", potencia)


def main():
        print ("      BIENVENIDO TAREA 5     ")
        print ("-----------------------------")
        print ("             MENU            ")
        print ("-----------------------------")
        print ("1. Dibujar cuadros y circulos")
        print ("2. Dibujar espiral")
        print ("3. Dibujar circulos")
        print ("4. Dibujar parabolas")
        print ("5. Aproximar a PI")
        print ("6. Contar divisibles entre 29")
        print ("7. Imprimir piramides de numeros")
        print ("0. Salir ")
        print ("-----------------------------")
        opcion=(int(input("Por favor introduzca el numero de la accion que desea realizar: ")))

        while not opcion ==0:
            if opcion == 1:
                print ("Figura A: Cuadros y Circulos")
                dibujarA()

            elif opcion == 2:
                print("Figura C: Espiral cuadricular")
                dibujarC()

            elif opcion == 3:
                print("Figura D: 12 Circulos entrelazados")
                dibujarD()

            elif opcion == 4:
                print("Figura B: Parabolas")
                dibujarB()

            elif opcion == 5:
                print("Aproximacion a PI**2/6")
                divisor=(int(input("Introduzca el valor del ultimo divisor: ")))
                pi= aproximarPI(divisor)
                print ("El resultado mas proximo es: ",pi)

            elif opcion == 6:
                cuatroDigitos()

            elif opcion==7:
                print("Piramides de numeros")
                piramides()

            else:
                print ("ERROR! Opcion inexistente, por favor introduzca un numero entre 1 y 7")
                print ("O, presione 0 para salir")

            print("")
            print("")
            print("")
            print ("          BIENVENIDO         ")
            print ("-----------------------------")
            print ("             MENU            ")
            print ("-----------------------------")
            print ("1. Dibujar cuadros y circulos")
            print ("2. Dibujar espiral")
            print ("3. Dibujar circulos")
            print ("4. Dibujar parabolas")
            print ("5. Aproximar a PI")
            print ("6. Contar divisibles entre 29")
            print ("7. Imprimir piramides de numeros")
            print ("0. Salir ")
            print ("-----------------------------")
            opcion=(int(input("Por favor introduzca el numero de la accion que desea realizar: ")))
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")


main()