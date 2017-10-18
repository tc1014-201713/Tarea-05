# encoding: UTF-8
# Autor: Daniel Sahuer
# Programa donde por medio de un menú, se eligen dibujos en pygame y varias funciones

#Librerias
import pygame
import math
from random import randint

#Dimensiones
ANCHO = 800
ALTO = 800

#Colores
BLANCO = (255,255,255)
NEGRO = (000,000,000)


def dibujarCuadrosYCirculos():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibuja rectangulo
        for x in range(0,ANCHO,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-x,ALTO//2-x,2*x,2*x),1)
        # Dibuja circulo
        for y in range(1,ALTO//2,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),y,1)


        pygame.display.flip()   #Actualiza trazos
        reloj.tick(40)  #Fps

    pygame.quit()   #Termina pygame


def dibujarEspiral():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Dibuja la espiral con base en líneas
        for i in range(0,ANCHO,10):
            pygame.draw.line(ventana,NEGRO,(ANCHO//2-i,ALTO//2+i),(ANCHO//2+10+i,ALTO//2+i))
            pygame.draw.line(ventana,NEGRO,(ANCHO//2-i,ALTO//2-i),(ANCHO//2-i,ALTO//2+i))
            pygame.draw.line(ventana,NEGRO,(ANCHO//2-10-i,ALTO//2-10-i),(ANCHO//2+10+i,ALTO//2-10-i))
            pygame.draw.line(ventana,NEGRO,(ANCHO//2+10+i,ALTO//2-10-i),(ANCHO//2+10+i,ALTO//2+i))


        pygame.display.flip()   #Actualiza trazos
        reloj.tick(40)  #Fps

    pygame.quit()   #Termina pygame


def dibujarCirculos():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Dibuja los circulos
        for i in range(30,361,30):
            rad = (i * math.pi)/180 #Calcula los angulos en radianes
            pygame.draw.circle(ventana, NEGRO, (int((ANCHO // 2+(math.cos(rad)*150))), (int((ALTO // 2+(math.sin(rad)*150))))), 150, 1)


        pygame.display.flip()   #Actualiza trazos
        reloj.tick(40)  #Fps

    pygame.quit()   #Termina pygame


def dibujarParabolas():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Dibuja parábolas de acuardo a líneas
        for x in range (0,ANCHO//2,10):
            random = (randint(0,255),randint(0,255),randint(0,255)) #Se elige un color aleatorio
            pygame.draw.line(ventana, random, (ANCHO//2,x), (ANCHO//2+x,ALTO//2), 1)
            pygame.draw.line(ventana, random, (ANCHO//2,x), (ANCHO//2-x,ALTO//2), 1)
            pygame.draw.line(ventana, random,(ANCHO//2,ALTO-x), (ANCHO//2+x,ALTO//2), 1)
            pygame.draw.line(ventana, random, (ANCHO//2,ALTO-x), (ANCHO//2-x,ALTO//2), 1)


        pygame.display.flip()   #Actualiza trazos
        reloj.tick(40)  #Fps

    pygame.quit()   #Termina pygame


def aproximarPi(div): #Calcula una aproximación de pi de acuerdo al divisor escrito por el usuario
    suma=0

    for d in range (1,div+1,1):
        suma = suma + 1/div**2
        aprox = (suma*6)**.5
    return aprox


def divisibles(): #Calcula cuantos números de 4 dígitos son divisibles entre 29
    total = 0
    for div in range(29,9999):
        if div % 29 == 0:
            total += 1
    return total



def piramidesNumeros(): #Imprime 2 cadenas de números
    num1 = 0
    num2 = 0
    cons = 8

    for valor1 in range(1, 10):
        num1 = valor1 + (num1*10)
        total = num1 * cons + valor1
        print ("\n%d * %d + %d = %d" % (num1,cons,valor1,total))


    for valor2 in range (1,10):
        num2 = (num2*10) + 1
        total = num2 * num2
        print("\n%d * %d = %d" % (num2, num2, total))


def main():
    opcion = 8
    while opcion != 0:
        print ("\nTarea 5. Seleccione qué quiere hacer.\n 1. Dibujar cuadros y círculos\n 2. Dibujar espiral\n 3. Dibujar círculos\n 4. Dibujar parábolas\n 5. Aproximar PI\n 6. Contar divisibles entre 29\n 7. Imprimir pirámides de números\n 0. Salir\n")
        opcion = int(input("¿Qué desea hacer? "))

        if opcion == 1:
            dibujarCuadrosYCirculos()
        elif opcion == 2:
            dibujarEspiral()
        elif opcion == 3:
            dibujarCirculos()
        elif opcion == 4:
            dibujarParabolas()
        elif opcion == 5:
            div = int(input("Escribe el último valor del divisor: "))
            aproximacion = aproximarPi(div)
            print ("Pi es: %.5f" % aproximacion)
        elif opcion == 6:
            div = divisibles()
            print ("Los números divisibles entre 29 son: ",div)
        elif opcion == 7:
            piramidesNumeros()
        elif opcion == 0:
            print("Adios")
        else:
            print("%d no es un numero válido\nIntenta otra vez\n"% opcion)


main()