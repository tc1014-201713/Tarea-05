# encoding: UTF-8
# Autor : Javier León Alcántara
# Tarea 05, Muestra un menu para acceder a los diferentes ejercicios.

# Dimensiones de la pantalla

import pygame
from math import *
from random import *


ANCHO = 800
ALTO = 800

# Colores

BLANCO = (255,255,255)  #RGB en el rango [0,255]
NEGRO = (0,0,0)


def a ():   #Dibuja cuadrados y circulos
    pygame.init()  #Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO,ALTO))  #Crea la ventana de dibujo
    reloj = pygame.time.Clock()    #Para limitar los fps
    termina = False #Bandera para saber si termina la ejecución

    while not termina:   #Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:   #Si el usuario hace click en el boton de salir
                termina = True

            #Borrar pantalla
            ventana.fill(BLANCO)

        for i in range(1,400,10):  # Va desde 1 hasta el valor del ancho en 10 en 10
            pygame.draw.circle(ventana, NEGRO,(ANCHO//2,ANCHO//2),i,1)   #Dibuja los circulos
            pygame.draw.rect(ventana,NEGRO,(i,i, ANCHO-(2*i),ALTO-(2*i)),1)  #Dibuja los cuadrados

        pygame.display.flip() #Actualiza trazos
        reloj.tick(10) #10 fps

    pygame.quit()



def b ():  #Dibuja parábolas
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    ALTERNO = (randint(0, 255))


    while not termina:  # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hace click en el boton de salir
                termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

        for i in range(1, 400, 10):
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,i),(400+i,400),) #Dibuja el primer cuadrante
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,i),(400-i,400),) #Dibuja el segundo cuadrante
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,800-i),(400+i,400),) #Dibuja el cuarto cuadrante
            pygame.draw.line(ventana,(randint(0,255),randint(0,255),randint(0,255)),(400,800-i),(400-i,400),) #Dibuja el tercer cuadrante

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()



def c (): #Dibuja espiral
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    ALTERNO = (randint(0, 255))

    while not termina:  # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hace click en el boton de salir
                termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

        for i in range(0, 400, 10):
            pygame.draw.line(ventana,NEGRO,(400-i,400+i),(410+i,400+i),)   #Dibuja las lineas
            pygame.draw.line(ventana,NEGRO,(410+i,400+i),(410+i,390-i),)
            pygame.draw.line(ventana,NEGRO,(410+i,390-i),(390-i,390-i),)
            pygame.draw.line(ventana,NEGRO,(390-i,390-i),(390-i,410+i),)

        pygame.display.flip()
        reloj.tick(10) # temporisador

    pygame.quit()



def d (): #Dibuja círculos
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    ALTERNO = (randint(0, 255))
    radio = 150

    while not termina:  # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hace click en el boton de salir
                termina = True

            # Borrar pantalla
            ventana.fill(BLANCO)

        for i in range(0,12):
            angulo = (pi/6)*i     # 30 grados es igual a pi/6 radianes
            x = int((cos(angulo))*150)   #Calcula la posicion del circulo en x
            y = int((sin(angulo))*150)   #Calcula la posicion del circulo en y
            pygame.draw.circle(ventana, NEGRO, (400+x,400+y),radio,1)  #Dibuja los circulos

        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()



def Pi(numero):  #Aproximar PI
        piCuadrado = 0
        for i in range(1, numero + 1):
            piCuadrado += (1 / (i ** 2))
        pi = sqrt((piCuadrado * 6))

        return pi



def NumerosDivisibles ():   #Contar divisibles entre 29
    numerosD = 0   #Comienza con 0 numeros divisibles
    for i in range(1000,9999):   #Rango de numeros con 4 digitos
        resultado = i % 29     # Residuo de dividir el numero entre 29
        if resultado == 0:     #Si el residuo es 0 va a aumentar 1 a "numerosDivisibles"
            numerosD += 1

    return numerosD



def Piramides ():   #Imprimir pirámides de numeros
    numero = 1
    for i in range (1,10):
        resultado = (numero * 8) + i   #Calcula el resultado
        print(numero, "* 8 +",i,"=",resultado)    #Imprime las operaciones
        numero = (numero * 10)+(i+1)   #Se genera el nuevo numero


    print("")   #Espacio :P

    numero = 1   #Regresa el valor de "numero" a 1 despues del for de arriba
    for i in range (1,10):
        resultado = numero * numero  #Resultado de la operación
        print(numero, "*", numero, "=", resultado)  #Imprime las operaciones
        numero = (numero*10)+1  #Genera el nuevo número



def main():  #Menu

    print("Tarea 5. Seleccione qué quiere hacer" 
          "\n" 
          " 1. Dibujar cuadros y círculos "
          "\n"
          " 2. Dibujar espiral "
          "\n" 
          " 3. Dibujar círculos"
          "\n" 
          " 4. Dibujar parábolas "
          "\n" 
          " 5. Aproximar PI "
          "\n" 
          " 6. Contar divisibles entre 29 "
          "\n"    
          " 7. Imprimir pirámides de números"
          "\n"
          " 0. Salir "
          "\n")
    elegir = int(input(" ¿Qué desea hacer? "))  #Ingresa la instrucción

    salir = False
    while not salir:      #Ejecuta las instrucciones
        if elegir == 0:
            salir=True
            quit()

        elif elegir == 1:
            a()
        elif elegir ==2:
            c()
        elif elegir ==3:
            d()
        elif elegir ==4:
            b()
        elif elegir ==5:
            respuesta = int(input("Escriba el numero: "))
            pi = Pi(respuesta)
            print(pi)
        elif elegir ==6:
            resultado = NumerosDivisibles()
            print(resultado)
        elif elegir ==7:
            Piramides()

        else:
            print("El número es invalido")

        elegir=int(input(" ¿Qué desea hacer? "))




main()