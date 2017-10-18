# Encoding: UTF-8
# Autor: Gabriela Mariel Vargas Franco

#Función que dibuje cuadrados y circulos.

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO = (0, 0, 0)

def dibujarCuadrosCirc():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  #salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)


        # Dibujar cuadrado

        for i in range (0,ANCHO//2,10):
            x=0
            y=0
            pygame.draw.rect(ventana, NEGRO, (x+i, y+i, ANCHO-(2*i), ALTO-(2*i)), 1)

        #Dibujar circulo

        for i in range (0,ANCHO//2,10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), i+10, 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame
    main()

# Dibujar parabola

def dibujarParabola():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  #salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)


        # Dibujar parabola
        import random
        for i in range (0,ANCHO,10):
            color=random.randrange(0,255),random.randrange(0,255), random.randrange(0,255)
            pygame.draw.line(ventana, color, [ANCHO//2+i,ALTO//2],[ANCHO//2, ALTO-i], 1)
            pygame.draw.line(ventana, color, [ANCHO//2 - i, ALTO//2], [ANCHO//2, ALTO- i], 1)
            pygame.draw.line(ventana, color, [ANCHO//2 + i, ALTO//2], [ANCHO//2, 0 +i], 1)
            pygame.draw.line(ventana,color,[ANCHO//2-i,ALTO//2],[ANCHO//2, 0+i], 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame



    main()

#Espiral

def dibujarEspiral():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  #salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)


        # Dibujar cuadrado
        x1=0
        y1=0
        x2=800
        y2=800

        for i in range (0,800,10): #i=10,20,30,40...

            pygame.draw.line(ventana, NEGRO,(x1,y1),(x1,y2),1)
            pygame.draw.line(ventana, NEGRO,(x1,y2),(x2,y2),1)

            pygame.draw.line(ventana, NEGRO,(x2,y2),(x2,y1+10),1)

            pygame.draw.line(ventana,NEGRO,(x2,y1+10),(x1+10,y1+10),1)
            x1=x1+10
            y1=y1+10
            y2=y2-10

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame
    main()
#Función que dibuje circulos.

import math

def dibujarCirculos():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  #salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Dibujar circulo

        for i in range (0,360,30):
            x=math.sin(i/180*math.pi)*150
            y=math.cos(i/180*math.pi)*150
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2+ int(x),ALTO//2+ int(y)),150, 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

    main()

# Calcula y regresa una aproximación al valor Pi con una serie


def aproximarPi():
    suma=0
    contador=0
    n=int(input("Último número:"))
    for i in range(1, n+1,1):
        contador +=1

        suma=suma+(1/(i*i))

    pi=(suma*6)**0.5
    print(pi)
    main()


# Calcula y regresa cuántos número de 4 dígitos son divisibles entre 29
def imprimirDigitos29():
    x=0
    m=0
    for factor in range (999,10000):
        x=x+1
        resultado=factor%29
        if resultado==0:
            m=m+1

    print("¿Cuántos números de 4 dígitos divisibles entre 29?", m)
    main()


# Calcula e imprime las siguientes operaciones usando un ciclo.

def imprimirDigitosx8(digitos):
    x=0
    y=0

    for factor in range (1,11):
        x=x+1
        y=y+1
        digitos=(digitos*10)+x
        resultado=(digitos*8)+y
        print("%d x 8 +%d = %d" % (digitos,x, resultado))

def imprimirDigitos(digitos):

    for factor in range(1,11):
        digitos=(digitos*10)+1
        factor=digitos
        resultado=digitos*factor
        print("%d x %d = %d" % (digitos,factor, resultado))



    for y in range (0,1):
        imprimirDigitosx8(y)
    for t in range(0,1):
        imprimirDigitos(t)


    main()

def main():
    print("Tarea5-¿Qué deseas hacer?")
    print("1.Dibujar cuadros y círculos ")
    print("2.Dibujar espiral")
    print("3.Dibujar círculos ")
    print("4.Dibujar parábolas")
    print("5.Aproximar PI ")
    print("6.Contar divisibles entre 29")
    print("7.Imprimir pirámides de números")
    print("0.Salir")
    opcion=int(input("¿Qué deseas hacer?"))

    terminar=False

    while opcion!=terminar:
        if opcion==1:
            dibujarCuadrosCirc()
        elif opcion==2:
            dibujarEspiral()
        elif opcion==3:
            dibujarCirculos()
        elif opcion==4:
            dibujarParabola()
        elif opcion==5:
            aproximarPi()
        elif opcion==6:
            imprimirDigitos29()
        elif opcion==7:
            imprimirDigitosx8(digitos)
            imprimirDigitos(digitos)
        elif opcion==0:
            print("Saliendo del programa")
            break #FIN
main()
