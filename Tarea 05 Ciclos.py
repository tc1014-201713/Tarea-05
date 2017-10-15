# Autor: Sául Rodrigo Toral Luna.
# Matrícula: A01745007

# El programa contiene un menú en el cual el usuario al ingresar un número
# desplegará el ejercicio deseado


#Se importan distintas librerías para poder trabajar con ella durante los ejercicios
import math
import pygame
from random import randint

# Se definen Constantes
ANCHO = 800
ALTO = 800
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)


# La función dibuja cuadros y círculos que van aumentando en tamaño dejando una separación de 10 pixeles
def dibujarCuadriCirculos():
# Cuerpo para iniciar pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
# Decisión del usuario si termina cierra la pantalla y termina el proceso
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        for x in range(0, ANCHO // 2 + 1, 10):
            pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x, 2 * x, 2 * x), 1)
        for x in range(10, ANCHO // 2 + 1, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), x, 1)

            pygame.display.flip()
            reloj.tick(40)
    pygame.quit()

# La función dibuja cuadros y círculos que van aumentando en tamaño dejando una separación de 10 pixeles
def dibujarCuadradosCirculos():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    reloj=pygame.time.Clock()
    termina=False
    while not termina:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                termina=True
        ventana.fill(BLANCO)
        for x in range (0,ANCHO//2 +1,10):
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-x,ALTO//2-x,2*x,2*x),1)
        for x in range (10,ANCHO//2+1,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),x,1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

# La función dibuja un espiral de líneas en donde estas van aumentando su distancia de acuerdo a un ciclo for
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
        for x in range(0,ANCHO//2+1,10):
            pygame.draw.line(ventana, NEGRO,(ANCHO//2-x,ALTO//2+x),(ANCHO//2+5+x,ALTO//2+x))
            pygame.draw.line(ventana, NEGRO, (ANCHO //2-10 - x, ALTO // 2-10 - x), (ANCHO // 2 + 5 + x, ALTO // 2-10 - x))
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2+5 + x, ALTO // 2 -10- x), (ANCHO // 2 + 5 + x, ALTO // 2 + x))
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x), (ANCHO // 2 - x, ALTO // 2 + x))
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


# La función dibuja una serie de círculos en donde se cambia los grados a donde es dibujado para formar una imagen entre la unión de círculos
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
        for x in range(0, 360, 30):
            cos = ((math.cos(x * math.pi / 180)))
            sen = ((math.sin(x * math.pi / 180)))
            pygame.draw.circle(ventana, NEGRO, (int(ANCHO / 2 + (150 * cos)), int(ALTO / 2 + (150 * sen))), 150, 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


# La función dibuja una serie de lineas que forman parabolas por medio de un ciclo for
def dibujarParabolas():
        pygame.init()
        ventana = pygame.display.set_mode((ANCHO, ALTO))
        reloj = pygame.time.Clock()
        termina = False
        while not termina:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    termina = True
            ventana.fill(BLANCO)
            #Se realiza un ciclo el cual dibujará las lineas dejando como espacio 10 pixeles
            for x in range(0, ANCHO // 2 + 1, 10):
                # Aqui se define el color aleatorio
                ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, 0 + x), (ANCHO // 2 + x, ALTO // 2), 1)
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - x), (ANCHO // 2 + x, ALTO // 2), 1)
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, 0 + x), (ANCHO // 2 - x, ALTO // 2), 1)
                pygame.draw.line(ventana, ALEATORIO, (ANCHO // 2, ALTO - x), (ANCHO // 2 - x, ALTO // 2), 1)
            pygame.display.flip()
            reloj.tick(40)
        pygame.quit()


# La función aproxima a pi por medio de la suma hasta el número que es ingresado.
def aproximarPI(aprox):
    suma = 0
    # Se hace un "for" hasta el número ingresado para aproximar a PI
    for i in range (1,aprox+1):
        suma = suma + (1/(i**2))
    suma = math.sqrt(suma*6)
    return suma


# La función  calcula cuantos números son divisibles entre 19
def contarDivisibles():
    divisible = 0
    # Calcular el valor entre  números de 4 digitos para ver si son divisibles entre 19
    for numeros in range(1000,10000):
        if (numeros % 19) == 0:
# Por cada número que cumpla con la condición, este se ira almacenando en el contador
            divisible += 1
    return divisible


# La función desarrolla las piramides de ciertas series de números y se define acumulador
def desarrollarPiramide():
    piramides = "\n"
    escalera = 0
# Por medio del for se le asigna un rango de 1 a 10 para la primera piramide ya que no usa el 10
    for numero in range(1, 10):
        escalera = int("1" * numero) + escalera
        producto = escalera * 8 + numero
        piramides = piramides + ("%d * 8 + %d = %d\n" % (escalera, numero, producto))
    piramides +="""
"""
# For para la segunda piramide de números
    for numero in range(1, 10):
        escalera = int("1" * numero)
        producto = escalera * escalera
        piramides = piramides + ("%d * %d = %d\n" % (escalera, escalera, producto))

    return piramides


# Función principal donde lee e imprime los datos
# Se visualiza un menú en donde el usuario por medio de números elige el ejercicio a resolver
def main():
# Mientras el ejercicio siga teniendo el valor de verdadero este seguira repitiendo procesos hasta que se vuelva falso
    ejercicio = True
# Ciclo "while" permite repetir los procesos "n" cantidad de veces hasta que deje de cumplir la condición
    while ejercicio == True:
# Se muestran los ejercicios a resolver
        print("Tarea 5. Seleccione que quiere hacer.")
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar espiral")
        print("3. Dibujar círculos")
        print("4. Dibujar parábolas")
        print("5. Aproximar PI")
        print("6. Contar divisibles entre 19")
        print("7. Imprimir pirámides de números")
        print("0. Salir")
# Ingresa lo que el usuario desea hacer
        hacer = int(input("¿Qué desea hacer?: "))
        print("")
# Por medio de decisiones se evalua y muestra el ejercicio deseado
        if hacer == 1:
            print(dibujarCuadradosCirculos())
        elif hacer == 2:
            print(dibujarEspiral())
        elif hacer == 3:
            print(dibujarCirculos())
        elif hacer == 4:
            print(dibujarParabolas())
        elif hacer == 5:
            aprox = int(input("Ingresa hasta que numero quieres aproximar PI: "))
            print("")
            if aprox > 0:
                print("En base a %d la aproximación de PI es de" % aprox,  aproximarPI(aprox))
                print("")
            else:
                print("Ingresa un número valido")
        elif hacer == 6:
            print("Existen %d numeros de 4 digitos que son divisibles entre 19" % contarDivisibles())
            print("")
        elif hacer == 7:
            print("")
            print(desarrollarPiramide())
            print("")
        elif hacer == 0:
            ejercicio = False
            print("Gracias por participar")
# Si ingresa el numero 0 se muestra un mensaje y detiene los procesos
        else:
            print("La opción %d es invalida, escoge un número del menú" % hacer)
            print("")
main()