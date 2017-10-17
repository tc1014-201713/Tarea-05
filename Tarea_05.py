#encoding UTF-8
#Autor: Omar Israel Galván García
#A01745810

import pygame
import random
import math

ANCHO = 800
ALTO  = 800
BLANCO = (255,255,255)
NEGRO = (0,0,0)

VERDE = (97,240,11)
ROJO =  (245,5,5)
AZUL =  (0,0,245)
NARANJA = (244, 147,0)

radio = 150

def cuadrosCirculos():

    x = ANCHO//2
    y = ALTO//2

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for i in range (1,400,10):
            pygame.draw.circle(ventana,NEGRO,(x,y),i,1)
            #se traza un círculo dentro de los límites establecidos con el ciclo for y va aumentando el tamaño de su radio
        for aumento in range(0, 400, 10):
            pygame.draw.rect(ventana, NEGRO, (aumento, aumento, ANCHO - (2 * aumento), ALTO - (2 * aumento)), 1)
            #se traza un rectángulo dentro de los límites establecidos con el ciclo for y va reduciendo su tamaño
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
    main()


def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for x in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2, ALTO // 2), (ANCHO // 2 + 10, ALTO // 2), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x), (ANCHO // 2 + x, ALTO // 2 - x), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + x + 10, ALTO // 2 + x), (ANCHO // 2 - x, ALTO // 2 + x), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 10, ALTO // 2 - 10), (ANCHO // 2 + 10, ALTO // 2), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 + x), (ANCHO // 2 - x, ALTO // 2 - x), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + x + 10, ALTO // 2 - x - 10),(ANCHO // 2 + x + 10, ALTO // 2 + x), 1)
            # de pone un límite para cada una de las líneas dibujadas para crear el efecto de espiral
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

    main()

def dibujarParabola():
    x = ANCHO//2
    y = ALTO//2

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for i in range(0,401,10):
            COLOR = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            pygame.draw.line(ventana, COLOR, (x, i), (x - i, y), 1)   # se dibuja una línea del punto más alto y a la mitad de la pantalla al sigueinte punto
            pygame.draw.line(ventana, COLOR, (x, i), (x + i, y), 1)   # que es 10 unidades a la izquierda en x y en "y" a la mitad de la pantalla
            pygame.draw.line(ventana, COLOR, (x, y + i), (i, y), 1)
            pygame.draw.line(ventana, COLOR, (x, ALTO - i), (x + i, y), 1) # une una línea desde el punto mas bajo a la mitad en el eje y y 10 unidades a la  izquerda


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
    main()

def calcularPi(n):
    suma = 0  # se inicia un contador en 0
    for i in range (1,n+1):  #ciclo for de 1 al número que se teclee
        suma += (1/(i**2))  #ahora suma tiene un valor
    pi = (suma*6)**(0.5)  # se le asigna la operacion a pi
    print("\n"*2)
    print("El valor aproximado de Pi,con", n, "intentos es: ", pi)  #imprime el resultado
    print("\n"*5)
    main()

def calcularDivisibles ():
    numero = 0  # se inicia un contador en 0
    for x in range (1000,10000): #un ciclo for para contar los 4 dígitos, empezando desde el 1000 hasta el 10000 (9999 + 1)
        if x %19 == 0: # se crea una condicional
            numero+=1  # se le asigna un nuevo valor al contador número
    print("\n")
    print("Hay", numero, "números de 4 dígitos divisibles exactamente entre 19") # imprime el resultado
    print("\n")
    main()


def dibujarPiramide ():
    print("\n"*3)  #espacio para evitar que se junten los  datos
    a = "" # se crea una variable de tipo string inicialmente vacía
    for i in range (1,10): #ciclo for de 1 a 10
        posicion = str(i) #transforma el entero del ciclo for a un string
        a += posicion  #ahora la variable vale el entero convertido
        resultado = int(a)*8 + i # se convierte el string a entero y se realizan las operaciones
        print("%s * 8 + %d = %d"%(a,i,resultado))  #imprime los resultados

    valorInicial = "1" #se inicializa una variable en "1" para empezar el conteo
    print("\n"*3) #espacio para borrar datos
    for x in range(1, 10):   #ciclo for de 1 a 10
        posicionDos = valorInicial * x  #la variable almacena el valor de multiplicar x veces el string inicial con valor de 1
        resultadoDos = int(posicionDos) * int(posicionDos)  #convierte el string a entero y los multiplica
        print("%s * %s = %d" % (posicionDos, posicionDos, resultadoDos))    #imprime los resultados
    print("\n"*3)  #espacio
    main()

def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for angulo in range(0, 360, 30):  #ciclo for de 0 a 360 (grados que tiene un círculo)
            anguloRadianes = angulo * math.pi / 180 #convierte a radianes los ángulos  obtenidos por el ciclo for
            pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + int(radio * math.cos(anguloRadianes)), ALTO // 2 + int(radio * math.sin(anguloRadianes)))),radio, 1)
            #se dibuja un círculo con las coordenadas realizando funciones trigonométricas y crea los 12 círculos
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
    main()

def main ():

    print("Tarea 5. Seleccione qué quiere hacer." # se muestra el menú princiipal
            "\n"
          "1. Dibujar cuadrados"
            "\n"
          "2. Dibujar espiral "
            "\n"
          "3. Dibujar círculos "
            "\n"
          "4. Dibujar parábolas"
            "\n"
          "5. Aproximar Pi"
            "\n"
          "6. Contar divisibles entre 19"
            "\n"
          "7. Imprimir pirámides de números"
            "\n"
          "0. Salir")
    opcion = int(input("¿Qúe desea hacer?")) #se pregunta y se lee lo que se quiere hacer



    salir = False
    while not salir:
        if opcion == 1:   #se lee cada una de las condicionales y si alguna resulta verdadera, salta a la función creada
          cuadrosCirculos()
        elif opcion == 2:
            dibujarEspiral()
        elif opcion == 3:
            dibujarCirculos()
        elif opcion == 4:
            dibujarParabola()
        elif opcion == 5:
            numeros = int(input("Ingrese el número que desee para calcular Pi..."))
            calcularPi(numeros)
        elif opcion == 6:
            calcularDivisibles()
        elif opcion == 7:
            dibujarPiramide()
        elif opcion == 0:
            print("\n"*10)
            print("¡Gracias! Vuelva Pronto...")
            break  #termina el programa



main() # se ejecuta la función principal main

