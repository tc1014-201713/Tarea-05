#encoding: UTF-8
#Nazdira Abigail Cerda del Prado
#A01375428
#Programa con un menu para que el usuario decida qué quiere que el programa haga

#Importa librerias y establec constantes (globales)
import pygame
from random import randint
import math
import sys
ANCHOV = 800
ALTOV = 800
NEGRO = (0,0,0)
BLANCO = (255,255,255)

#Dibuja cuadrados y círculos con una diferencia de tamaño de 10 pixeles
def dibujarCuadroCirculo():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHOV, ALTOV))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        #Dibuja los cuadrados y circulos
        for x in range(0,ANCHOV//2 + 1,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHOV//2-x,ALTOV//2-x,2*x,2*x),1)
        for x in range(10,ANCHOV//2 + 1,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHOV//2,ALTOV//2),x,1)
        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps
    pygame.quit()

#Dibuja parabolas con color aleatorio
def dibujarparabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHOV, ALTOV))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibuja parabolas
        for diferencia in range(0, ANCHOV//2 +1, 10):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana, ALEATORIO,(ANCHOV//2, 0 + diferencia), (ANCHOV//2 + diferencia,ALTOV//2), 1)
            pygame.draw.line(ventana, ALEATORIO,(ANCHOV//2, ALTOV - diferencia), (ANCHOV//2 + diferencia,ALTOV//2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHOV//2, 0 + diferencia), (ANCHOV//2 - diferencia,ALTOV//2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHOV//2, ALTOV - diferencia), (ANCHOV//2 - diferencia,ALTOV//2), 1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Dibuja un espiral de cuadrados
def dibujarEspiralCuadros():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHOV, ALTOV))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibuja los cuadrados
        for diferencia in range(0, ANCHOV//2 +1, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHOV//2 - diferencia, ALTOV//2 + diferencia), (ANCHOV//2 + 5 + diferencia, ALTOV//2 + diferencia))
            pygame.draw.line(ventana, NEGRO, (ANCHOV//2 - 10 - diferencia, ALTOV//2 - 10 - diferencia), (ANCHOV//2 + 5 + diferencia, ALTOV//2 - 10 - diferencia))
            pygame.draw.line(ventana, NEGRO, (ANCHOV//2 + 5 + diferencia, ALTOV//2 - 10 - diferencia), (ANCHOV//2 + 5 + diferencia,  ALTOV//2 + diferencia))
            pygame.draw.line(ventana, NEGRO, (ANCHOV//2 - diferencia,  ALTOV//2 - diferencia), (ANCHOV//2 - diferencia,  ALTOV//2 + diferencia))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Dibuja circulos intersectados
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHOV, ALTOV))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibuja circulos
        for diferencia in range(0, 360, 30):
            coseno = ((math.cos(diferencia*math.pi/180)))
            seno = ((math.sin(diferencia*math.pi/180)))
            pygame.draw.circle(ventana,NEGRO,(int(ANCHOV/2+ (150*coseno)),int(ALTOV/2 + (150*seno))),150,1)



        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Aproxima al valor de pi de acuerdo al número que indique el usuario
def calcularValorPi(limite):
    serie = 0
    for x in range (1,limite+1):
        serie= serie+(1/x**2)
    pi = (6*(serie))**(1/2)
    return pi

#Calcula todos los números de 4 digitos divisibles entre 29
def calcularNumerosDivisiblesentre29():
    ndivisibles = 0
    for numeros in range (1000,10000,1):
        if numeros % 29 == 0:
            ndivisibles += 1
    return ndivisibles

#Calcula e imprime piramaides de multiplicaciones
def calcularPiramidesNumeros():
    piramides = "\n"
    escalera = 0
    for factor in range(1,10):
        escalera = int("1"*factor) + escalera
        resultado = escalera * 8 + factor
        piramides = piramides + ("%d * 8 + %d = %d\n" % (escalera,factor,resultado))
    piramides = piramides + "\n"
    for factor in range(1,10):
        escalera = int("1" * factor)
        resultado = escalera * escalera
        piramides = piramides + ("%d * %d = %d\n" % (escalera, escalera, resultado))

    return piramides

#Funcion principal que dirige al programa y pregunta al usuario qué acción quiere realizar
def main():
    termina = True
    while termina:
        print(""" ---------------------------- MENU ----------------------------
            1) Cuadros y circulos
            2) Parabolas multicolor
            3) Espiral cuadrado
            4) Circulos intersectados
            5) Aproximación de pi
            6) Contar divisibles entre 29
            7) Imprimir piramides de numeros enteros
            0) Salir """)
        eleccion = int(input("Seleccione qué quiere hacer:"))
        if eleccion == 1:
            dibujarCuadroCirculo()
            print("")
        elif eleccion == 2:
            dibujarparabolas()
            print("")
        elif eleccion == 3:
            dibujarEspiralCuadros()
            print("")
        elif eleccion == 4:
            dibujarCirculos()
            print("")
        elif eleccion == 5:
            nlimite = int(input("Dame el número limite de la serie para aproxima pi: "))
            print("Pi vale aproximadamente: %.4f " % calcularValorPi(nlimite))
            print("")
        elif eleccion == 6:
            print(" Los numeros de 4 digitos divisibles entre 29 son: ", calcularNumerosDivisiblesentre29())
            print("")
        elif eleccion == 7:
            print(calcularPiramidesNumeros())
            print("")
        elif eleccion == 0:
            sys.exit()
        else:
            print("¡ERROR! El termino que uso no es válido")
            sys.exit()

main()