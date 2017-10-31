#Encoding: UTF-8
#Autor: Alberto López Reyes
#Descripción: Este programa le da la posibilidad al usuario de graficar 4 funciones distintas, estimar el valor
#Pi de acuerdo a un valor de entrada, contar los divisbles de 4 digitos entre el número 29 e imprimir pirámides
#de números.

import sys
import pygame
from random import randint
import math

Ancho = 800
Alto = 800
Blanco = (250, 250, 250)
Negro = (0, 0, 0)

def ImprimirMenu():
    print("""====================
Tarea 5. Seleccion qué quiere hacer.
1.  Dibujar cuadros y círculos
2.  Dibujar espiral
3.  Dibujar círculos
4.  Dibujar parábolas
5.  Aproximar PI
6.  Contar divisibles entre 29
7.  Imprimir pirámides de números
0.  Salir""")
    intSeleccion = int(input("¿Qué desea hacer? "))

    print("====================")

    return intSeleccion

def DibujarCuadrosyCirculos():
    global Ancho
    global Alto

    pygame.init()
    Ventana = pygame.display.set_mode((Ancho, Alto))
    Reloj = pygame.time.Clock()
    Terminar = False

    Ventana.fill(Blanco)

    while not Terminar:
        for intMultiplicadorTacito in range(1, Alto//10 + 1):

            pygame.draw.rect(Ventana, Negro , (Ancho // 2 - 5*intMultiplicadorTacito, Alto // 2 - 5*intMultiplicadorTacito, intMultiplicadorTacito*10, intMultiplicadorTacito*10), 1)

            pygame.draw.circle(Ventana, Negro, (Ancho//2, Alto//2), intMultiplicadorTacito*5, 1)

            pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Terminar = True

        Reloj.tick(5)

    pygame.quit()

def DibujarEspiral():
    global Ancho
    global Alto
    global Blanco
    global Negro

    pygame.init()
    Ventana = pygame.display.set_mode((Ancho, Alto))
    Reloj = pygame.time.Clock()
    Terminar = False

    Ventana.fill(Blanco)

    while not Terminar:
        for intMultiplicadorTacito in range(0, 500):

            intX1 = Ancho//2 - 5 * (intMultiplicadorTacito + 1)
            intX2 = Ancho//2 + 5 * (intMultiplicadorTacito + 1)
            intX3 = Ancho//2 + 5 * (intMultiplicadorTacito - 1)
            intX4 = Ancho//2 - 5 * (intMultiplicadorTacito - 1)

            intY1 = Alto // 2 - 5 * (intMultiplicadorTacito + 1)
            intY2 = Alto // 2 + 5 * (intMultiplicadorTacito + 1)
            intY3 = Alto // 2 + 5 * (intMultiplicadorTacito - 1)
            intY4 = Alto // 2 - 5 * (intMultiplicadorTacito - 1)

            pygame.draw.line(Ventana, Negro, (intX1, intY1), (intX2, intY1), 1)

            pygame.draw.line(Ventana, Negro, (-intX1, intY1), (-intX2, intY1), 1)

            pygame.draw.line(Ventana, Negro, (intX1, intY1), (intX1, intY2), 1)

            pygame.draw.line(Ventana, Negro, (intX1, -intY1), (intX1, -intY2), 1)

            pygame.draw.line(Ventana, Negro, (intX3, intY3), (intX4, intY3), 1)

            pygame.draw.line(Ventana, Negro, (-intX3, intY3), (-intX4, intY3), 1)

            pygame.draw.line(Ventana, Negro, (intX3, intY3), (intX3, intY4), 1)

            pygame.draw.line(Ventana, Negro, (intX3, -intY3), (intX3, -intY4), 1)

            pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Terminar = True

        pygame.display.flip()

        Reloj.tick(10)

    pygame.quit()

def DibujarCirculos():
    global Ancho
    global Alto
    global Blanco
    global Negro

    pygame.init()
    Ventana = pygame.display.set_mode((Ancho, Alto))
    Reloj = pygame.time.Clock()
    Terminar = False

    Ventana.fill(Blanco)

    ltCoordenadas = [(Ancho//2 + int(150 * math.cos(0)), Alto//2 + int(150 * math.sin(0))),
                      (Ancho//2 + int(150 * math.cos(1*math.pi/6)), Alto//2 + int(150 * math.sin(1*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(2*math.pi/6)), Alto//2 + int(150 * math.sin(2*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(3*math.pi/6)), Alto//2 + int(150 * math.sin(3*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(4*math.pi/6)), Alto//2 + int(150 * math.sin(4*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(5*math.pi/6)), Alto//2 + int(150 * math.sin(5*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(6*math.pi/6)), Alto//2 + int(150 * math.sin(6*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(7*math.pi/6)), Alto//2 + int(150 * math.sin(7*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(8*math.pi/6)), Alto//2 + int(150 * math.sin(8*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(9*math.pi/6)), Alto//2 + int(150 * math.sin(9*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(10*math.pi/6)), Alto//2 + int(150 * math.sin(10*math.pi/6))),
                      (Ancho//2 + int(150 * math.cos(11*math.pi/6)), Alto//2 + int(150 * math.sin(11*math.pi/6)))]

    while not Terminar:
        for intNumero in range(0, 11+1):

            pygame.draw.circle(Ventana, Negro, ltCoordenadas[intNumero], 150, 1)

            pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Terminar = True

        Reloj.tick(20)

    pygame.quit()

def DibujarParabolas():
    global Ancho
    global Alto
    global Blanco

    pygame.init()
    Ventana = pygame.display.set_mode((Ancho, Alto))
    Reloj = pygame.time.Clock()
    Terminar = False

    Ventana.fill(Blanco)

    while not Terminar:
        for intMultiplicadorTacito in range(1, (Ancho//2)//10 + 1):

            Paleta1 = (randint(0, 250), randint(0, 250), randint(0, 200))

            pygame.draw.lines(Ventana, Paleta1,  True, ((0 + 10*intMultiplicadorTacito, Alto//2), (Ancho//2,  Alto//2 + 10*intMultiplicadorTacito), (Ancho - 10*intMultiplicadorTacito, Alto//2), (Ancho//2,  Alto//2 - 10*intMultiplicadorTacito)), 1)

            pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Terminar = True

        Reloj.tick(40)

    pygame.quit()

def AproximarPi(intUltimoDivisor):
    if intUltimoDivisor <= 0:
        return False

    intAproxPi = 0
    fltTermino = 0

    for intDivisor in range(1, intUltimoDivisor+1):
        fltTermino = fltTermino + float((1/(intDivisor**2)))

    fltAproxPi = (6*(fltTermino))**.5

    return fltAproxPi

def ContarDivisiblesEntre29():
    intConteoDivisbles = 0

    for intDivisible in range(1000, 9999+1):
        if intDivisible % 29 == 0:
            intConteoDivisbles = intConteoDivisbles + 1

    return intConteoDivisbles

def ImprimirPirámidesdeNumeros():
    intPrimerTermino = 0
    intSegundoTermino = 8

    print("-   -   -   -   -   -")

    for intTercerTermino in range(1, 9+1):
        if intTercerTermino == 1:

            intMultiplicadorTacito = 1

        else:

            intMultiplicadorTacito = 10

        intPrimerTermino = intPrimerTermino*intMultiplicadorTacito + intTercerTermino
        intCuartoTermino = intPrimerTermino*intSegundoTermino+intTercerTermino
        print(str(intPrimerTermino)+" * "+str(intSegundoTermino)+" + "+str(intTercerTermino)+" = "+str(intCuartoTermino))

    intPrimerTermino = 0

    print("-   -   -   -   -   -")

    for intVeces1 in range(1, 9+1):
        if intVeces1 == 1:

            intMultiplicadorTacito = 1

        else:

            intMultiplicadorTacito = 10

        intPrimerTermino = intPrimerTermino * intMultiplicadorTacito + 1

        intTercerTermino = intPrimerTermino**2

        print(str(intPrimerTermino)+" * "+str(intPrimerTermino)+" = "+str(intTercerTermino))

    print("-   -   -   -   -   -")

def Volver():
    print("""····················""")

    intVolver = int(input("Presione 1 si desea volver al menú, o 2 si desea terminar. "))

    print("""····················""")

    if intVolver == 1:
        main()

    elif intVolver == 2:
        print("- - - - - - - - - - -")
        print("Terminando programa.")
        print("- - - - - - - - - - -")

        sys.exit()

    else:
        ImprimirError()

def ImprimirError():
    print("""####################
ERROR: PRESIONE UN VALOR VÁLIDO
####################""")
    Volver()

def main():
    intSeleccion = ImprimirMenu()

    if intSeleccion == 1:
        print("- - - - - - - - - - -")
        print("Iniciando función. Presione culaquier parte del gráfico para salir.")

        DibujarCuadrosyCirculos()

        print("- - - - - - - - - - -")

        Volver()

    elif intSeleccion == 2:
        print("- - - - - - - - - - -")
        print("Iniciando función. Cierre la ventana para salir.")

        DibujarEspiral()

        print("- - - - - - - - - - -")

        Volver()

    elif intSeleccion == 3:
        print("- - - - - - - - - - -")
        print("Iniciando función. Cierre la ventana para salir.")

        DibujarCirculos()

        print("- - - - - - - - - - -")

        Volver()

    elif intSeleccion == 4:
        print("- - - - - - - - - - -")
        print("Iniciando función. Cierre la ventana para salir.")

        DibujarParabolas()

        print("- - - - - - - - - - -")

        Volver()

    elif intSeleccion == 5:
        print("- - - - - - - - - - -")
        intUltimoDivisor = int(input("Introduzca el último divisor para la aproximación de Pi: "))

        fltAproxPi = AproximarPi(intUltimoDivisor)

        print("Pi se aproxima a: "+str(fltAproxPi))
        print("- - - - - - - - - - -")
        Volver()

    elif intSeleccion == 6:
        print("- - - - - - - - - - -")
        print("La cantidad de números divisibles entre 29 es de: "+str(ContarDivisiblesEntre29()))
        print("- - - - - - - - - - -")
        Volver()

    elif intSeleccion == 7:
        print("- - - - - - - - - - -")
        ImprimirPirámidesdeNumeros()
        print("- - - - - - - - - - -")
        Volver()

    elif intSeleccion == 0:
        print("- - - - - - - - - - -")
        print("Terminando programa.")
        print("- - - - - - - - - - -")

        sys.exit()

    else:
        ImprimirError()

main()
