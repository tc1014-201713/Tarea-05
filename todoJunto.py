# encoding: UTF-8
# Autor: Raul Ortiz Mateos A01375407

import pygame
import random
import math
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
radio=150
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO=(0,0,0)
def dibujarParabolas():#para dibujar la parabola
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)

        for i in range(0, 400,10):
            pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i,ALTO/2),(ANCHO/2,i+ALTO/2))
            pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i,ALTO/2),(ANCHO/2,-i+ALTO/2))
            pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO-i,ALTO/2),(ANCHO/2,ALTO/2+i))
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO-i,ALTO/2),(ANCHO/2,ALTO/2-i))






        pygame.display.flip()   # Actualiza trazos
                  # 40 fps

    pygame.quit()   # termina pygame
def dibujarEspiral():#Dibujar la espiral
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras


        for i in range(0,400,10):
            pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i,ALTO-i),(ANCHO-i,ALTO-i))#esta primer linea es de la parte de abajo del espiral
            pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(ANCHO-(10+i),i),(ANCHO-(10+i),ALTO-(10+i)))#esta es la parte de la derecha de la espiral
            #lo que se hio para hacer la espiral fue sumarle 10 para que cuando la corriera esta no quedara semejnte a la de la
            #  parte de abajo  y se recorriera un espacio para porfar la espiral
            pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i,i),(ANCHO-(10+i),i))#Esta es la continuacion de la espiral de la parte de arriba
            #  le agregue el mas 10 para que no quedara junta.
            pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i,i),(i,ALTO-i))#y para finalizar esta es la parte de la derecha de la espiral,
            #  esta se quedo normal debido a que es la que conecta con la parte de abajo y no necesita ninguna modificacion.





        pygame.display.flip()   # Actualiza trazos


    pygame.quit()   # termina pygame
def dibujarCirculoCuadrado():#dibujar los 12 circulos
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(NEGRO)
        # este for se utiliza para dibujar los circulos, don i es cuado le vas a quitar de los 400 de radio va ir disminuyendo 10
        for i in range(1, 400,10):
            pygame.draw.circle(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) , (ANCHO // 2, ALTO // 2), 400-(i), 1)

        for i2 in range(1,400,10):#este es para hacer los cuadros que van con los circulos.
            pygame.draw.rect(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),(i2,i2,ANCHO-(2*i2),ALTO-(2*i2)),1)
            



        pygame.display.flip()   # Actualiza trazos


    pygame.quit()   # termina pygame
def dibujarCirculos():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)

        for i in range(0,12):
            pygame.draw.circle(ventana, NEGRO, (int(ANCHO//2+radio*math.cos(math.pi*i/6)),int(ALTO//2 + radio*math.sin(math.pi*i/6))),radio,1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps


    pygame.quit()   # termina pygame
def aproximarPi(n):
    suma=0
    for d in range(1,n+1):
        contador=1/d**2
        suma=suma+contador
    aproximacion=suma
    ValorExacto=math.pi**2/6
    print("su aproximacion es de:",aproximacion)
    print("------------------------------------")
    print("El valor exacto de Pi**2/6 es de:",ValorExacto)


    return suma
def calculardivisiblesEntre29():
    d = 0
    for i in range(1000, 10000):
        if i % 29 == 0:
            d += 1
    return d
def calcularCadena():
    numero=0
    viii=8
    for i in range (0,10):
        numero= numero* 10+ i
        total=numero*viii+i
        print(numero,"*",viii,"+",i,"=",total)
    print("============================================")
    UNo = 0

    for i in range(1, 10):
        UNo = UNo * 10 + (i + (1 - i))
        total = UNo**2
        print(UNo, "*", UNo, "=", total)

def main():

    print("Menu")
    print("1=Dibujar cadrados y circulos.")
    print("2=Dibujar parabolas.")
    print("3=Dibujar espiral.")
    print("4=Dibujar 12 circulos")
    print("5=Aproximar el valor de PI,dependiendo del valor que le asigne el usuario")
    print("6=cuántos números de 4 dígitos son divisibles entre 29")
    print("7=cadenas de numeros")
    print("0=salir del menu")
    numero=int(input("¿que numero desea poner en el menu?  "))
    while not numero==0:
        if numero==1:
            print("usted eligio,dibujar los cuadrados y el circulo")
            dibujarCirculoCuadrado()

        elif numero==2:
            print("Usted eligio dibujar parabolas")
            dibujarParabolas()

        elif numero==3:
            print("Usted decidio dibujar Espiral")
            dibujarEspiral()

        elif numero==4:
            print("Usted decidio dibujar 12 circulos")
            dibujarCirculos()

        elif numero==5:
            print("Usted decidio aproximar el valor de PI,dependiendo del valor que le asigne el usuario")
            Numero = int(input("que numero es el que quiere aproximar a Pi**2/6: "))
            aproximarPi(Numero)

        elif numero==6:
            print("Usted quiere saber cuántos números de 4 dígitos son divisibles entre 29")
            print("La cantidad de numeros divicibles entre 29 son de:", calculardivisiblesEntre29())

        elif numero==7:
            print("cadenas de numeros")
            print(calcularCadena())
        else:
            print("ERROR, Escriba un número válido (0 al 7)")

        print("=================_________________===========================")
        print("Menu")
        print("1=Dibujar cadrados y circulos.")
        print("2=Dibujar parabolas.")
        print("3=Dibujar espiral.")
        print("4=Dibujar 12 circulos")
        print("5=Aproximar el valor de PI,dependiendo del valor que le asigne el usuario")
        print("6=cuántos números de 4 dígitos son divisibles entre 29")
        print("7=cadenas de numeros")
        print("0=salir del menu")
        numero = int(input("¿que numero desea poner en el menu?  "))



    print("nos vemos")
    pygame.quit()

main()