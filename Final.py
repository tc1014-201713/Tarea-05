#encoding: UTF-8
#Autor: Aaron Villanueva
#Este programa hace muchas cosas.
import pygame
import math
import os

anchoVentana = 800
altoVentana = 800
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

def dibujarCuadrosCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((anchoVentana, altoVentana))
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for diferencia in range(0,400,10):
            pygame.draw.circle(ventana, NEGRO, (anchoVentana // 2, altoVentana // 2), 400-diferencia, 2)
        for cambio in range(0,400,10):
            pygame.draw.rect(ventana, NEGRO, (cambio, cambio, anchoVentana-(2*cambio), altoVentana-(2*cambio)), 1)
        pygame.display.flip()
    pygame.quit()

def dibujarLaberinto():
    pygame.init()
    ventana = pygame.display.set_mode((anchoVentana, altoVentana))
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        x=400
        y=400
        cambio=10
        constante=cambio/2
        for angulo in range(0,14400,90):
            anguloOperaciones=math.radians(angulo)
            anguloCoseno=math.cos(anguloOperaciones)
            cambioX=int(cambio*anguloCoseno)
            anguloSeno=math.sin(anguloOperaciones)
            cambioY=int(cambio*anguloSeno)
            pygame.draw.line(ventana, NEGRO,(x,y),(x+cambioX,y-cambioY), 1)
            x=x+cambioX
            y=y-cambioY
            cambio=cambio+constante
        pygame.display.flip()
    pygame.quit()

def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((anchoVentana, altoVentana))
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for angulo in range(0,360,30):
            anguloOperaciones=math.radians(angulo)
            anguloCoseno=math.cos(anguloOperaciones)
            x=int(150*anguloCoseno)
            anguloSeno=math.sin(anguloOperaciones)
            y=int(150*anguloSeno)
            pygame.draw.circle(ventana, NEGRO, (400+x, 400+y), 150, 1)
        pygame.display.flip()
    pygame.quit()
            
#Esta función aproxima el valor de Pi a partir de una formula recursiva. Requiere un parametro para el número de recursiones.
#Entre mayor sea el número de recursiones, mas cercana la aproximación de pi.
def aproximarPi(intentos):
    x = 0
    for i in range(1, intentos):
        x = x + (1 / (i ** 2))
    x = x * 6
    x = x ** .5
    return(x)

#Esta función encuentre los números divisibles entre 29 que tengan 4 digitos.
def encontrarNumerosDivisiblesEntre29():
    x=0
    for i in range(1000,9999):
        y=i%29
        if y==0:
            x=x+1
        else:
            x=x
    return(x)

#Esta función imprime un par de piramides númericas sin utilizar string o listas. Solamente calculos.
def piramidesNumeros():
    piramide = 1
    for factor in range(1, 10):
        resultado = piramide * 8 + factor
        print(piramide, "X 8 +", factor, "=", resultado)
        piramide = (piramide * 10) + (factor + 1)
    print("")
    numeros = 1
    for i in range(10):
        resultadocuadrado = numeros * numeros
        print(numeros, "X", numeros, "=", resultadocuadrado)
        numeros = (numeros * 10) + 1
    
def main():
    respuesta=True
    while respuesta==True:
        print("Tarea 5. Seleccione qué quiere hacer.")
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar espiral")
        print("3. Dibujar círculos")
        print("4. Dibujar parabolas")
        print("5. Aproximar PI")
        print("6. Contar divisibles entre 29")
        print("7. Imprimir piramides de números")
        print("0. Salir")
        eleccion = int(input("¿Qué desea hacer?"))
        print("")
        if eleccion==0:
            print("saliendo")
            respuesta=False
        elif eleccion==1:
            dibujarCuadrosCirculos()
        elif eleccion==2:
            dibujarEspiral()
        elif eleccion==3:
            dibujarCirculos()
        elif eleccion==4:
            dibujarParabolas()
        elif eleccion==5:
            final=int(input("Ingrese un número entero para determinar Pi. Entre mayor sea, más exacto el resultado"))
            print("La aproximación de Pi con", final,"intentos es de:",aproximarPi(final))
        elif eleccion==6:
            print("El número de números de cuatro digitos divisibles entre 29 es:",encontrarNumerosDivisiblesEntre29())
        elif eleccion==7:
            print(piramidesNumeros())
        else:
            print("error. Número no localizado")
        print("")
        os.system('CLS')
main()
