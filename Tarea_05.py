#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez.
#Usando un menú le da la opción al usuario de decidir que quiere hacer, dibujar figuaras o realizar algunos cálculos.

import pygame #importamos la librería pygame.
from random import randint #importamos de la librería random, randint para generar colores aleatorios
import math #importamos math para generar calculos más exactos.

#Dimensiones de la pantalla.
ANCHO = 800
ALTO = 800
#Colores.
BLANCO = (255,255,255)
NEGRO = (0,0,0)
VERDE = (0,155,0)

def dibujarCuadradosCirculos (): #dibuja una figura compuesta por cuadrados y círculos.

    pygame.init() #Inicia pygame.
    ventana = pygame.display.set_mode((ANCHO,ALTO)) #Crea la ventana.
    reloj = pygame.time.Clock() #fps
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ancho = 800
        alto = 800

        ventana.fill(BLANCO) #Borra pantalla.

        #Dibuja.
        for x in range (10,400,10):
            ancho = ancho - 20
            alto = alto -20
            pygame.draw.rect(ventana,NEGRO,(x,x,ancho,alto),1)

        for x in range (10,400,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),x,1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def dibujarParabolas(): #dibuja una figura que asemeja a 4 parábolas.

    pygame.init() #Inicia programa.
    ventana = pygame.display.set_mode((ANCHO,ALTO)) #Crea ventana.
    reloj = pygame.time.Clock()#Limitar fps
    termina = False #Termino de la ejecución.

    while not termina:
        #Eventos del programa.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #Usuario teclea el botón de salir para finalizar programa.
                termina = True

        #Borra Pantalla.
        ventana.fill(BLANCO)

        #Dibujar.
        for x in range (0,401,10):
            aleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana,aleatorio,(ANCHO//2,x),(ANCHO//2+x,ALTO//2),1)
            pygame.draw.line(ventana,aleatorio,(ANCHO//2,x),(ANCHO//2-x,ALTO//2),1)
            pygame.draw.line(ventana,aleatorio,(ANCHO//2,ALTO-x),(ANCHO//2+x,ALTO//2),1)
            pygame.draw.line(ventana,aleatorio,(ANCHO//2,ALTO-x),(ANCHO//2-x,ALTO//2),1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(5)  # fps

    pygame.quit()

def dibujarEspiral(): #dibuja una figura hecha por una espiral.

    pygame.init()  # Inicia pygame.
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana.
    reloj = pygame.time.Clock()  # fps
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)  # Borra pantalla.

        # Dibuja.
        for x in range(0, 401, 10):
            pygame.draw.line(ventana,NEGRO,(ANCHO//2-x,ALTO//2+x),(ANCHO//2+10+x,ALTO//2+x),1)
            pygame.draw.line(ventana,NEGRO,(ANCHO//2+10+x,ALTO//2+x),(ANCHO//2+10+x,ALTO//2-10-x),1)
            pygame.draw.line(ventana,NEGRO,(ANCHO//2+10+x,ALTO//2-10-x),(ANCHO//2-10-x,ALTO//2-10-x),1)
            pygame.draw.line(ventana,NEGRO,(ANCHO//2-10-x,ALTO//2-10-x),(ANCHO//2-10-x,ALTO//2+10+x),1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def dibujarCirculos(): #dibuja una figura compuesta por 12 círculos.

    pygame.init()  # Inicia pygame.
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana.
    reloj = pygame.time.Clock()  # fps
    termina = False
    radio = 150

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)  # Borra pantalla.

        #Dibuja.
        for x in range (0,13,1):
            angulo = (math.pi/6)*x
            x = int((math.cos(angulo))*150)
            y = int((math.sin(angulo))*150)
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2+x,ALTO//2+y),radio,1)

        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()

def aproximarPi(num): #aproxima el valor de pi.

    acumula_sumas = 0

    for x in range (1,num+1):
        aproxima = 1/(x**2)
        acumula_sumas = acumula_sumas + aproxima

    aproximacionPi = (6*acumula_sumas)**0.5


    return aproximacionPi

def contarDivisibles(): #cuenta los números de 4 dígitos divisibles entre 29.

    contar_numeros = 0

    for x in range (1000,10000):
        if x % 29 == 0:
            contar_numeros = contar_numeros + 1

    return contar_numeros

def hacerPiramides(): #crea pirámides de números.

    numero = 1

    for x in range (1,10):
        resultado = numero * 8 + x
        print(numero, "* 8 +",x,"=",resultado)
        numero = (numero * 10)+(x)

    print("\r")

    numero = 1

    for x in range (1,10):
        resultado = numero * numero
        print(numero, "*", numero, "=", resultado)
        numero = (numero * 10) + 1


def main ():

    finaliza = "h"

    print("Tarea 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadradros y círculos")
    print("2. Dibujar espiral")
    print("3. Dibujar círculos")
    print("4. Dibujar parábolas")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 29")
    print("7. Imprimir pirámides de números")
    print("0. Salir")

    while not finaliza == 0:

        finaliza = int(input("¿Qué desea hacer?: "))

        if finaliza == 0:
            print("Programa Terminado")

        elif finaliza < 0 or finaliza > 7:
            print("Ingresa un número correcto (del 0 al 7)")

        elif finaliza == 1:
            dibujarCuadradosCirculos()

        elif finaliza == 2:
            dibujarEspiral()

        elif finaliza == 3:
            dibujarCirculos()

        elif finaliza == 4:
            dibujarParabolas()

        elif finaliza == 5:

            print("\r")

            print("Esta aproximación funciona mejor mientras el número que ingreses sea más grande")
            num = int(input("Ingresa el número hasta el que se realizará la aproximación: "))

            print(aproximarPi(num))
            print("\r")

        elif finaliza == 6:

            print("\r")

            print("Cuenta los números de 4 dígitos divisibles entre 29")
            print(contarDivisibles())
            print("\r")

        elif finaliza == 7:
            hacerPiramides()

main()