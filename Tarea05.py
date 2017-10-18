# encoding: UTF-8
# Autor: Edgar Alexis González Amador
# Matricula A01746540
import pygame
import math
from random import randint

#Declaración de variables
anchoPantalla = 800
altoPantalla = 800
colorBlanco = (255,255,255)
colorNegro = (0, 0, 0)
centroPantalla = 400

#Función de cuadros y circulos
    #Esta función permite crear en una pantalla de pygame cuadrados con separacion de 10 pixeles desde el centro de la pantalla hasta cada uno de los extremos y hacer lo mismo con circulos.
def DibujarCuadrosYCirculos():
    pygame.init()
    ventanaFuncion01 = pygame.display.set_mode((anchoPantalla, altoPantalla))
    relojFuncion01 = pygame.time.Clock()
    variableDeTermino = False
    #Se coloca un while para permitir la repeticion en la creación del dibujo
    while not variableDeTermino:
        #Se declara la sentencia para permitir la salida de pantalla
        for eventoPantalla in pygame.event.get():
            if eventoPantalla.type == pygame.QUIT:
                variableDeTermino=True
            #Se limpia la pantalla con el color blanco
            ventanaFuncion01.fill(colorBlanco)

        for pixelesRectangulo in range (0,400,10):
            pygame.draw.rect(ventanaFuncion01, colorNegro, (centroPantalla-pixelesRectangulo,
                                                           centroPantalla-pixelesRectangulo,
                                                           pixelesRectangulo * 2,
                                                           pixelesRectangulo * 2), 1)
        for pixelesCirculo in range(10, 400, 10):
            pygame.draw.circle(ventanaFuncion01, colorNegro, (centroPantalla, centroPantalla),
                               pixelesCirculo, 1)

        pygame.display.flip()
        relojFuncion01.tick(40)

    pygame.quit()

#Función de parabolas
    #Esta funcion permite crear con diferentes lineas una estrella a partir de parabolas.
def DibujarParabolas():
    pygame.init()
    ventanaFuncion02 = pygame.display.set_mode((anchoPantalla, altoPantalla))
    relojFuncion02 = pygame.time.Clock()
    variableDeTermino = False
    # Se coloca un while para permitir la repeticion en la creación del dibujo
    while not variableDeTermino:
        # Se declara la sentencia para permitir la salida de pantalla
        for eventoPantalla in pygame.event.get():
            if eventoPantalla.type == pygame.QUIT:
                variableDeTermino=True
            # Se limpia la pantalla con el color blanc
            ventanaFuncion02.fill(colorBlanco)

        for posicionPantalla in range (0,400,10):
            colorRandint = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventanaFuncion02, colorRandint, (posicionPantalla, centroPantalla), (centroPantalla, centroPantalla-posicionPantalla), 1)
            pygame.draw.line(ventanaFuncion02, colorRandint, (((centroPantalla*2)-posicionPantalla), centroPantalla), (centroPantalla, centroPantalla-posicionPantalla), 1)

            pygame.draw.line(ventanaFuncion02, colorRandint, (posicionPantalla, centroPantalla), (centroPantalla, centroPantalla+posicionPantalla), 1)
            pygame.draw.line(ventanaFuncion02, colorRandint, (((centroPantalla*2)-posicionPantalla), centroPantalla), (centroPantalla, centroPantalla+posicionPantalla), 1)

        pygame.display.flip()
        relojFuncion02.tick(40)

    pygame.quit()

#Función de espiral
    #Esta funcion permite rear una espiral con diferentes lineas, en diferentes direcciones y de diferentes dimensiones
def DibujarEspiral():
    pygame.init()
    ventanaFuncion03 = pygame.display.set_mode((anchoPantalla, altoPantalla))
    relojFuncion03 = pygame.time.Clock()
    variableDeTermino = False
    # Se coloca un while para permitir la repeticion en la creación del dibujo
    while not variableDeTermino:
        # Se declara la sentencia para permitir la salida de pantalla
        for eventoPantalla in pygame.event.get():
            if eventoPantalla.type == pygame.QUIT:
                variableDeTermino=True
            # Se limpia la pantalla con el color blanc
            ventanaFuncion03.fill(colorBlanco)
        FINDX = centroPantalla
        FINDY = centroPantalla

        for contador in range (0,40,1):
            contadorA = 5+(contador*20)
            contadorB = 10+(contador*20)
            contadorC = 15+(contador*20)
            contadorD = 20+(contador*20)
            #LineaA
            INICIOAX = FINDX
            INICIOAY = FINDY
            FINAX = FINDX + contadorA
            FINAY = FINDY
            pygame.draw.line(ventanaFuncion03, colorNegro, (INICIOAX, INICIOAY), (FINAX, FINAY), 1)
            #LineaB
            INICIOBX = FINAX
            INICIOBY = FINAY
            FINBX = FINAX
            FINBY = FINAY-contadorB
            pygame.draw.line(ventanaFuncion03, colorNegro, (INICIOBX, INICIOBY), (FINBX, FINBY), 1)
            # LineaC
            INICIOCX = FINBX
            INICIOCY = FINBY
            FINCX = FINBX-contadorC
            FINCY = FINBY
            pygame.draw.line(ventanaFuncion03, colorNegro, (INICIOCX, INICIOCY), (FINCX, FINCY), 1)
            # LineaD
            INICIODX = FINCX
            INICIODY = FINCY
            FINDX = FINCX
            FINDY = FINCY + contadorD
            pygame.draw.line(ventanaFuncion03, colorNegro, (INICIODX, INICIODY), (FINDX, FINDY), 1)

        pygame.display.flip()
        relojFuncion03.tick(40)

    pygame.quit()


#Función de 12 circulos
    #Esta funcion permite crear 12 circulos de tal forma que el centro del siguiente este ubicado en la circunferencia de otro.
def DibujarCirculos():
    pygame.init()
    ventanaFuncion04 = pygame.display.set_mode((anchoPantalla, altoPantalla))
    relojFuncion04 = pygame.time.Clock()
    variableDeTermino = False

    while not variableDeTermino:
        # Se declara la sentencia para permitir la salida de pantalla
        for eventoPantalla in pygame.event.get():
            if eventoPantalla.type == pygame.QUIT:
                variableDeTermino=True
            # Se limpia la pantalla con el color blanc
            ventanaFuncion04.fill(colorBlanco)

        for angulo in range(0, 360, 30):
            anguloRadianes = angulo * (math.pi / 180)
            ca = int(150 * (math.cos(anguloRadianes)))
            co = int(150 * (math.sin(anguloRadianes)))
            pygame.draw.circle(ventanaFuncion04, colorNegro, (centroPantalla + co, centroPantalla + ca), 150, 1)

        pygame.display.flip()
        relojFuncion04.tick(40)

    pygame.quit()

#Función Aproximar PI
    #Esta función permite aproximar el numero PI mediante una sumatoria
def AproximarPI(ultimoValor):
    valorAproximado = 0.0
    for contador in range (1, ultimoValor, 1):
        valorAproximado = valorAproximado + (1/(contador**2))
    valorAproximado = (math.sqrt(valorAproximado*6))
    return valorAproximado

#Funcion Contar divisibles entre 19
    #Esta funcion permite saber cuandos numeros de 4 digitos son divisibles entre 19
def ContarDivisiblesEntre19():
    contadorDeNumerosDivisibles = 0
    for numeroACalcular in range(1000, 10000, 1):
        if (numeroACalcular%19 == 0):
            contadorDeNumerosDivisibles = contadorDeNumerosDivisibles + 1
    return contadorDeNumerosDivisibles

#Funcion imprimir piramides
    #Esta funcion permite crear dos piramides con dos for, a partir de una secuencia de operaciones
def ImprimirPiramides():
    variableAMultiplicar = 0
    for contador in range (1, 10, 1):
        variableAMultiplicar = (variableAMultiplicar * 10) + contador
        resultado = (variableAMultiplicar * 8) + contador
        print(variableAMultiplicar, " * 8 + ", contador, " = ", resultado)
    variableAMultiplicar = 0
    for contador in range (1, 10, 1):
        variableAMultiplicar = (variableAMultiplicar * 10) + 1
        resultado = variableAMultiplicar**2
        print(variableAMultiplicar, " * ", variableAMultiplicar, " = ", resultado)

#Función Main
    #La funcion main es la encargada de capturar la entrada de datos y de arrojar cada una de las opciones por medio de un menú.
def main():
    print("Tarea 5. Seleccione qué quiere hacer.\n1. Dibujar cuadros y círculos\n"
          "2. Dibujar espiral\n3. Dibujar círculos\n4. Dibujar parábolas\n5. Aproximar PI\n"
          "6. Contar divisibles entre 19\n7. Imprimir pirámides de números\n0. Salir")
    eleccion = 1
    while eleccion != 0:
        eleccion = int(input("¿Qué desea hacer? : "))
        if eleccion == 1:
            DibujarCuadrosYCirculos()
        elif eleccion == 2:
            DibujarEspiral()
        elif eleccion == 3:
            DibujarCirculos()
        elif eleccion == 4:
            DibujarParabolas()
        elif eleccion == 5:
            valor = int(input("Introduce el parametro: "))
            valorAproximado = AproximarPI(valor)
            print("El valor aproximado es = %f"%valorAproximado)
        elif eleccion == 6:
            numerosDivisibles = ContarDivisiblesEntre19()
            print("Existen %d numeros divisibles entre 19 de 4 digitos"%numerosDivisibles)
        elif eleccion == 7:
            ImprimirPiramides()
        elif eleccion > 7:
            print("Debes elegir alguna de las opciones del menú")

main()