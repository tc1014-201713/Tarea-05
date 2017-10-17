# encoding: UTF-8
# Autor: Angel Roberto Pesado Bartolo A01374942
# Tarea 5 para utilizar ciclos for

import pygame
from random import randint
import math


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL=(0,0,120)
NEGRO=(0,0,0)
ALEATORIO=(randint(0,255),randint(0,255),randint(0,255))


def dibujarParabolas(): #definimos la funcion dibujarParabolas
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
        ventana.fill(VERDE_BANDERA)
        # Borrar pantalla+
        #ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))


        ALEATORIO = randint(0, 255), randint(0, 255), randint(0, 255) #Definimos colores aleatorios
        Aleatorio = (randint(0, 255), randint(0, 255), randint(0, 255))
        Aleatorio1 = (randint(0, 255), randint(0, 255), randint(0, 255))
        Aleatorio2 = (randint(0, 255), randint(0, 255), randint(0, 255))
        puntoi = 0 #indicamos que el punto inicial es 0
        for i in range(0,(ANCHO//2+1),10):#El rango es de (0,400) de 10 en 10
            pygame.draw.line(ventana, ALEATORIO,(ANCHO//2,(ALTO//2-i) ) ,(puntoi, ALTO//2) , 1) #Dibuja la parte superior izquierda de las parabolas
            puntoi += 10
        puntoi=0
        for i in range(0, (ALTO // 2+1), 10):
            pygame.draw.line(ventana, Aleatorio1, (puntoi, ALTO // 2), (ANCHO// 2, ALTO // 2 + i), 1)#Dibuja la parte inferior izquierda de la parabola
            puntoi += 10
        puntof=ANCHO
        for i in range(ANCHO // 2, (ANCHO+1), 10): #El rango es de 400 a 800 de 10 en 10
            pygame.draw.line(ventana, Aleatorio, (ANCHO // 2, (ALTO - i)), (puntof, ALTO // 2), 1)#Dibuja la parte superior derecha de la parabola
            puntof -= 10
        puntof=ANCHO
        for i in range(ANCHO//2, (ANCHO+1), 10):#Dibuja la parte inferior derecha de la parabola.
            pygame.draw.line(ventana, Aleatorio2, (puntof, ALTO//2), (ANCHO//2, i), 1)
            puntof -=  10
        pygame.display.flip()   # Actualiza trazos
        reloj.tick(10)          # 40 fps

    pygame.quit()   # termina pygame

def dibujarEspiralDeCirculos():#definimos la funcion dibujarEspiralDeCirculos
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    # radio = ANCHO // 2
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)
        radio=150 #Definimos el radio de los circulos
        pi= math.pi #Configuramos el valor pi en una variable

        for angulo in range(360,0,-30): #Definimos el rango de los angulos, será de 360 a 0, como es de derecha a izquierda los intervalos van de -30 en -30 (porque son 12 circulos en un angulo de 360°)
            conversión=(angulo*pi/180) #Convertimos los ángulos a radianes
            x = (math.sin(conversión)) #Obtenemos la distancia respecto al ángulo en seno
            y = (math.cos(conversión)) #Obtenemos la distancia respecto al ángulo en coseno

            pygame.draw.circle(ventana, AZUL, (int(ANCHO // 2 + (radio * x)),int(ALTO // 2 + (radio * y)) ),radio, 1) #Trazamos los circulos

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(10)  # 10 fps

    pygame.quit()  # termina pygame

def calculcarDivisiblesEntre29(n):#definimos la funcion calcularDivisiblesEntre29
    suma=0 #indicamos que la variable suma es 0
    for divisor in range(1,n): #el rango de la entrada será hasta n
        if n%29==0:#Indicamos que si la división da como residuo 0 es una numero divisible exacto.
            suma+=divisor #La guardamos en suma
        return suma

def esDivisibleDe29(): #Continuación del código anterior.
    pp = 1
    cp = 0

    for pp in range (1000,10000): #Tenemos un rango de 1000 a 10000 ya que en ellos hay numeros de 4 digitos
        if calculcarDivisiblesEntre29(pp):#Mandamos los datos a la función calcularDivisiblesEntre29
            cp+=1 #Cada que encuentre ub numero lo pondrá en orden que lo encontró
            print(cp,"-",pp)
            print("Por lo tanto los numeros divisibles de 4 digitos entre 29 son: ", cp)#imprime cuantos valores son exactamente divisibles entre 29
        pp+=1

def dibujarCuadradoConCirculos(): #definimos la funcion dibujarCuadradoConCirculos
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)
        radio = ANCHO // 2 #Definimos el radio de los circulos
        ym=40 #Indicamos cuanto le quitamos en un inicio a la linea en x
        xm=40 #Indicamos cuanto le quitamos en un inicio a la linea en y
        x= 20 #indicamos en que posición en x empieza la primer linea
        y= 20 #indicamos en que posición en y empieza la primer linea
        while radio>0: #mientras el radio sea mayor a 0 se hará lo siguiente

            pygame.draw.rect(ventana, VERDE_BANDERA, (x, y, ANCHO - xm, ALTO - ym), 1)
            pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), radio, 1)
            x+=10 #cada vez que se repita se le sumara 10 a la posición en x
            y+=10 #cada vez que se repita se le sumara 10 a la posición en y
            xm+=20 #cada vez que se repita se le quitará 20 a la linea en x
            ym+=20 #cada vez que se repita se le quitará 20 a la linea en y
            radio -= 10 #cada vez que se repita el ciclo al radio se le irá quitando 10 hasta que llegue a 0 y se detenga el dibujo

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(10)          # 40 fps

    pygame.quit()   # termina pygame

def calcularTabla():#definimos la función calcularTabla
    numero = 0 #Damos valor a numero

    for n in range (1,11): #Tenemos un rango de 1 a 10
        numero=numero*10+n #El numero cada vez se multiplicará por 10 y se le sumará  n
        resultado=numero*8+n #El resultado se multiplicará por 8 y se le sumará n
        print(numero,"x 8 +","1 =", resultado) #se genera la tabla

    print("La siguiente tabla es:  ")

    inicial=0 #indicamos que inicial es 0
    for i in range (1,11): #Tenemos un rango de 1 a 10
        inicial = inicial * 10 + 1 #el valor inicial se multiplica por 10 y se le suma 1
        resultado = inicial * inicial# el valor inicial se multiplica por si mismo
        print(inicial, "x",inicial,"=", resultado)#Se genera la tabla
    return 0

def dibujarCuadradosEnEspiral(): #definimos la funcion dibujarCuadradosEnEspiral
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    #radio = ANCHO // 2
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(AZUL)
        pmx=ANCHO//2 #Punto medio en x
        pmy=ALTO//2 #Punto medio en y
        for movimiento in range(0, ANCHO // 2 , 10):
            pygame.draw.line(ventana, ALEATORIO, (pmx + movimiento, pmy - movimiento),(pmx - 5 - movimiento, pmy - movimiento),1)#Traza las lineas horizontales de la parte superior
            pygame.draw.line(ventana, ALEATORIO, (pmx + movimiento, pmy + movimiento), (pmx + movimiento, pmy - movimiento), 1) #Traza las lineas verticales de la parte derecha
            pygame.draw.line(ventana, ALEATORIO, (pmx + 10 + movimiento, pmy + 10 + movimiento),(pmx - 5 - movimiento, pmy + 10 + movimiento),1) #Dibuja las lineas horizontales de la parte inferior
            pygame.draw.line(ventana, ALEATORIO, (pmx - 5 - movimiento, pmy + 10 + movimiento), (pmx - 5 - movimiento, pmy - movimiento),1) #Traza las lineas verticales de la parte izquierda

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(10)          # 40 fps

    pygame.quit()   # termina pygame

def calcularValorPi():#definimos la función calcularPi
    aproximar = int(input("Dame el numero para calcular pi: "))#pedimos el numero al usuario

    for valorpi in range(0, aproximar + 1):#Tenemos un rango de 0 a lo que indique el usuario
        if valorpi > 0:# si el valor es mayor a 0
            resultado1 = (1 / (valorpi ** 2)) #sigue la funcion de sumatoria
            resultado2 = resultado2 +resultado1
        else:
            resultado1=0
            resultado2= resultado1 +0
    numero_aproximado_a_pi = math.sqrt((resultado2*6))#despejando la formula dada por el profesor se obtiene el numero aproximado a pi
    return numero_aproximado_a_pi #regresamos el valor obtenido



def main(): #definimos la función main
    salirMenu=True
    while salirMenu:
        print("Tarea 5. Seleccione qué quiere hacer.\n 1. Dibujar cuadros y círculos \n 2. Dibujar espiral(cuadrados)\n 3. Dibujar círculos \n 4. Dibujar Parábolas \n 5. Aproximar PI\n 6. Contar divisibles entre 29 \n 7. Imprimir piramides de números\n 0. Salir  ")
        selección = int(input("¿Qué deseas hacer?: \n "))
        if selección<=0 or selección >=8: #Si selección es menor a 0 y mayor a 7 el programa termina
            return print("¡¡¡Muchas gracias por la elección!!!")
        elif selección == 1: #si la seleccion es 1 llama a la funcion dibujarCuadradoConCirculos
            dibujarCuadradoConCirculos()  # LISTO
        elif selección == 2: #si la selección es igual a 2 llama a la función dibujarCuadradosEnEspiral
            dibujarCuadradosEnEspiral()  # LISTO
        elif selección == 3: #si la selección es igual a 3 llama a la función dibujarEspiralDeCirculos
            dibujarEspiralDeCirculos()
        elif selección == 4: #si la selección es igual a 4 llama a la función dibujarParabolas
            dibujarParabolas()  # LISTO
        elif selección == 5: #si la selección es igual a 5 llama a la función calcularPi
            print("El valor aprocimado es: ", calcularValorPi())
        elif selección == 6: #si la selección es igual a 6 llama a la función esDivisibleDe29
            esDivisibleDe29()  # LISTO
        elif selección == 7: #si la selección es igual a 7 llama a la función calcularTabla
            print(calcularTabla())

main()#Llamamos a la función main