# encoding: UTF-8
# Autor: Angel Ramírez Martínez
# Descripción: Tarea 5, programa que apartir de un menu, realiza diferentes acciones.
#importación de librerías
from random import *
import pygame
from math import *
#Determinación de constantes globales
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO =(0,0,0)



#Función en la cual se hacen todos los dibujos en pygame (opciones de menu 1-4).
def dibujar(accion):
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        control=False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Si el usuario ingresó 1 en el menú, se dibujarán cuadros y círculos.
        if accion==1:
            for i in range(0,800,10):
                pygame.draw.rect(ventana,NEGRO,(int(ANCHO/2-i/2),int(ALTO/2-i/2),i,i),1)
            for i in range(10,400,10):
                pygame.draw.circle(ventana,NEGRO,(400,400),i,1)
        # Si el usuario ingresó 2 en el menú, se dibujará una espiral cuadrada
        elif accion==2:
            for d in range(0, ANCHO, 10):
                pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 - 10) - d, (ALTO // 2 - 10) - d),((ANCHO // 2 + 5) + d, (ALTO // 2 - 10) - d), 1)
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - d, ALTO // 2 + d), ((ANCHO // 2 + 5) + d, ALTO // 2 + d),1)
                pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 - 10) - d, (ALTO // 2 - 10) - d),((ANCHO // 2 - 10) - d, (ALTO // 2 + 10) + d), 1)
                pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 + 5) + d, (ALTO // 2 - 10) - d),((ANCHO // 2 + 5) + d, ALTO // 2 + d), 1)
        # Si el usuario ingresó 3 en el menú, se dibujará  12 circulos.
        elif accion==3:
            for e in range(0, 360, 30):
                x = int(ANCHO // 2 + 150 * cos(radians(e)))
                y = int(ALTO // 2 + 150 * sin(radians(e)))
                pygame.draw.circle(ventana, NEGRO, (x, y), 150, 1)
        # Si el usuario ingresó 4 en el menú, se dibujará una parábla multicolor cambiante.
        else:
            for c in range(0, ANCHO // 2, 10):
                ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, 0 + c), (ANCHO // 2 + c, ALTO // 2), 1)
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - c), (ANCHO // 2 + c, ALTO // 2), 1)
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, 0 + c), (ANCHO // 2 - c, ALTO // 2), 1)
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - c), (ANCHO // 2 - c, ALTO // 2), 1)
        pygame.display.flip()   # Actualiza trazos
        reloj.tick(10)          # 40 fps

    pygame.quit()   # termina pygame

# Función que aproxima pi a partir de una serie que recibe como parámetro
def aproximarpi(x):
    z=(6*x)**.5
    return 'La aproximación de pi es: %.4f' %z
# Función que determina la serie a seguir para determinar pi, a partir de un límite que recibe como parámetro
def aproximarserie(var):
    x = 0
    for i in range(1, var + 1):
        y = 1 / (i ** 2)
        x += y
    return x

# Función que realiza dos pirámides de números
def calcularpiramides():
    piramides = "\n"
    salto = 0
    for g in range(1, 10):
        salto = int("1" * g) + salto
        resultado = salto * 8 + g
        piramides = piramides + ("%d * 8 + %d = %d\n" % (salto, g, resultado))
    piramides = piramides + "\n"
    for g in range(1, 10):
        salto = int("1" * g)
        resultado = salto * salto
        piramides = piramides + ("%d * %d = %d\n" % (salto, salto, resultado))
    return piramides
#Función que determina la cantidad de números de cuatro dígitos que son divisibles entre 29.
def calcularnumeros():
    z=0
    for i in range(1000,9999):
        if i%29 ==0:
            z+=1
    return z

#Función main que aloja un menu para el usuario y dependiendo de su elección, llama a la función pertinente
def main():
    menu= '''
Tarea 5. Seleccione lo que quiere hacer.
1. Dibujar cuadros y círculos
2. Dibujar espiral
3. Dibujar círculos
4. Dibujar parábolas
5. Aproximar PI
6. Contar divisibles entre 29
7. Imprimir pirámides de números 
0. Salir '''
    print(menu)
    accion=int(input('¿Qué desea hacer? '))
    while not(accion==0): #Mientras el usuario no ingrese el valor 0, entrará al ciclo.
        if accion >= 1 and accion<=4: #Si el usuario ingresa un numero entre el 1 y el 4, llama a la función dibujar.
            dibujar(accion)
            print(menu)
            accion = int(input('¿Qué desea hacer? '))
        elif accion==5:
            var=int(input('Ingresa el límite para aproximar Pi '))
            serie = aproximarserie(var)
            pi= aproximarpi(serie)
            print(pi)
            print(menu)
            accion = int(input('¿Qué desea hacer? '))
        elif accion==6:
            calc=calcularnumeros()
            print('La cantidad de números de cuatro digitos que son divisibles entre 29 son %d, son los siguientes:' %calc)
            for i in range (1000,10000):
                if i % 29 == 0:
                    print(i)
            print(menu)
            accion = int(input('¿Qué desea hacer? '))
        elif accion==7:
            piramides1=calcularpiramides()
            print(piramides1)
            print(menu)
            accion = int(input('¿Qué desea hacer? '))
        else:
            print('')
            print('Valor incorrecto favor de ingresar un valor adecuado')
            accion = int(input('¿Qué desea hacer? '))

main()