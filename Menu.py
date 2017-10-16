#enconding :UTF-8
#Ernesto Ibhar Guevara Gómez
#A01746121
#Programa que sirve para resolver diferentes ejercicios segun sea la opción del usuario.
import pygame
from random import randint
import math
from math import pi
ANCHO=800
ALTO=800
NEGRO=(0,0,0)
BLANCO=(255,255,255)
def dibujarCuadradosCirculos():
    # Esqueleto de pygame
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    reloj=pygame.time.Clock()
    termina=False
    while not termina:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                termina=True
        ventana.fill(BLANCO)
        #Aqui Se dibujan los cuadrados y los circulos.
        for x in range (0,ANCHO//2 +1,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-x,ALTO//2-x,2*x,2*x),1)
        for x in range (10,ANCHO//2+1,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),x,1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def dibujarParabolas():
    # Esqueleto de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        #Aqui se dibuja la estrella que se forma mediante parabolas
        for x in range (0,ANCHO//2+1,10):
            ALEATORIO=(randint(0,255),randint(0,255),randint(0,255))
            pygame.draw.line(ventana,ALEATORIO,(ANCHO//2,0+x),(ANCHO//2+x,ALTO//2),1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - x), (ANCHO // 2 + x, ALTO // 2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, 0 + x), (ANCHO // 2 - x, ALTO // 2), 1)
            pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - x), (ANCHO // 2 - x, ALTO // 2), 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

def cuadradoEspiral():
    #Esqueleto de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        #Aqui se dibuja el espiral
        for x in range(0,ANCHO//2+1,10):
            pygame.draw.line(ventana, NEGRO,(ANCHO//2-x,ALTO//2+x),(ANCHO//2+5+x,ALTO//2+x))
            pygame.draw.line(ventana, NEGRO, (ANCHO //2-10 - x, ALTO // 2-10 - x), (ANCHO // 2 + 5 + x, ALTO // 2-10 - x))
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2+5 + x, ALTO // 2 -10- x), (ANCHO // 2 + 5 + x, ALTO // 2 + x))
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x), (ANCHO // 2 - x, ALTO // 2 + x))
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()



def circulos():
    # Esqueleto de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        #Aqui se dibujan los circulos
        for x in range(0,360,30):
            coseno=((math.cos(x*math.pi/180)))
            seno=((math.sin(x*math.pi/180)))
            pygame.draw.circle(ventana,NEGRO,(int(ANCHO/2+(150*coseno)),int(ALTO/2+(150*seno))),150,1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def conseguirPi(valor):
    #Funcion para aproximarse a Pi
    suma=0
    for i in range (1,valor+1):
        suma= suma+(1/i**2)
    pi=(6*(suma))**(1/2)
    return pi
def calcularDivisables():
    divisibles=0
    for x in range(1000,10000):
        if (x%29)==0:
            divisibles += 1
    return divisibles


def calcularCiclo():
    #Funcion para generar piramide de numeros.
    piramide="\n"
    secuencia=0
    for x in range(1,10):
        secuencia= int("1"*x)+secuencia
        resultado=secuencia*8+ x
        piramide=piramide+("%d*8+%d=%d\n"%(secuencia,x,resultado))
    piramide=piramide+ "\n"


    for x in range(1,10):
        secuencia=int("1"*x)
        resultado= secuencia*secuencia
        piramide= piramide+("%d * %d =%d\n"%(secuencia,secuencia,resultado))
    return piramide

def main():
    ejercicio=1 #Este valor hace que el ciclo de generar el menu sea infinito hasta que él ponga 0 y esto haga que termine.
    while ejercicio==1:
        #Menú
        print("Tarea 5. Selecciona que quieres hacer: ")
        print("1. Dibujar cuadrados y circulos.")
        print("2. Dibujrar espiral")
        print("3. Dibujar círculos")
        print("4. Dibujar parabolas")
        print("5. Aproximar Pi")
        print("6. Contar divisibles entre 29")
        print("7. Imprimir pirámides de números")
        print("0. Salir")
        dato= int(input("¿Que deseas hacer?"))
        #Condiciones de menú
        if dato==0:
            ejercicio=0
        elif dato==1:
            dibujarCuadradosCirculos()
        elif dato==2:
            cuadradoEspiral()
        elif dato==3:
            circulos()
        elif dato==4:
            dibujarParabolas()
        elif dato==5:
            valor=int(input("Valor hasta el cual quieres calcular: "))
            print("Aproximadamente pi vale %.4f"%conseguirPi(valor))
        elif dato==6:
            print("Hay:",calcularDivisables(),"divisibles de 4 digitos de 29")
        elif dato==7:
            print(calcularCiclo())
        else:
            ejercicio=0

main()