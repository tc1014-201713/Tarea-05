# encoding UTF-8
# Autor: Luis Enrique Neri Pérez
# Matrícula: A01745995
# Descripción: PROGRAMA MATRIZ QUE PIDE LA ENTRADA DE UN NÚMERO PARA ACCEDER A UNA FUNCIÓN ESPECÍFICA
import random
import pygame
import math


#DIMENSIONES DE PANTALLA
ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

#FUNCIÓN QUE DIBUJA CUADROS Y CÍRCULOS
def dibujarCuadrosCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for contador in range (1,41):
            pygame.draw.rect(ventana, NEGRO, (10*contador, 10*contador, ANCHO-(20*contador), ALTO-(20*contador)), 1)
        for contador2 in range(1, 40):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), 400-(10*contador2), 1)
        pygame.display.flip()
    pygame.quit()

#FUNCIÓN QUE DIBUJA UNA ESPIRAL
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

        for variable in range (1,39):
            pygame.draw.line(ventana, NEGRO,(10+(10*variable),0+20+(10*variable)), (10+(10*variable),ALTO-(10*variable))) #IZQUIERDA
            pygame.draw.line(ventana, NEGRO, (ANCHO-10-(10*variable),20+(10*variable)), (ANCHO - 10-(10*variable),ALTO-10-(10*variable))) #DERECHA 39

        for variable in range(1, 40):
            pygame.draw.line(ventana, NEGRO, (10+(10*variable),ALTO-(10*variable)),(ANCHO - (10*variable),ALTO-(10*variable))) #ABAJO 40
        for variable in range(2, 40):
            pygame.draw.line(ventana, NEGRO, (0+ (10 * variable), 10 + (10 * variable)),(ANCHO - (10 * variable), 10 + (10 * variable)))  # ARRIBA 39
        pygame.display.flip()
    pygame.quit()

#FUNCIÓN PARA DIBUJAR CÍRCULOS
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock()
    termina = False
    radio = 150
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

            ventana.fill(BLANCO)

            for angulo in range(0,12):
                pygame.draw.circle(ventana, NEGRO, (int(ANCHO // 2 + 150 * math.cos(math.pi*angulo/6)), int(ALTO // 2 + 150 * math.sin(math.pi*angulo/6))), radio, 1)
            pygame.display.flip()
    pygame.quit()


#FUNCION PARA DIBUJAR PARÁBOLAS
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

            for altura in range(1, 41):
                pygame.draw.line(ventana, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (0 + 10*altura, ALTO / 2), (ANCHO / 2, ALTO / 2 + 10 * altura))
                pygame.draw.line(ventana, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (0 + 10*altura, ALTO / 2), (ANCHO / 2, ALTO / 2 - 10 * altura))
                pygame.draw.line(ventana, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (ANCHO - 10 * altura, ALTO / 2), (ANCHO / 2, ALTO / 2 + 10 * altura))
                pygame.draw.line(ventana, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (ANCHO - 10 * altura, ALTO / 2), (ANCHO / 2, ALTO / 2 - 10 * altura))
            pygame.display.flip()
            reloj.tick(40)
    pygame.quit()

#FUNCIÓN QUE CALCULA UN APROXIMADO DE π²/6
def aproximarPI(n):
    sumatoria = 0
    print("Espere un momento...")
    for denominador in range(1,n+1):
        aproximar = 1/denominador**2
        sumatoria = sumatoria + aproximar
    valorPI = (math.pi**2) / 6
    total = sumatoria
    print("\n")
    print("El valor de π²/6 es:" , valorPI)
    print("LA APROXIMACIÓN ES:", total)


#FUNCIÓN QUE CUENTA LOS NÚMEROS DE CUATRO DÍGITOS QUE SON DIVISIBLES ENTRE 19
def contarDivisibles():
    sumatoria = 0
    for numeros in range (1000,10000):
        if (numeros % 19) == 0:
            sumatoria = sumatoria + 1
        else:
            pass
    print("\n")
    print("NÚMEROS DIVISIBLES DE 19")
    print("----------------------------------")
    print("Dentro del rango de 1,000 a 9,999 hay %d números divisibles entre 19" % sumatoria)


#FUNCIÓN QUE IMPRIME PIRÁMIDES DE NÚMEROS
def imprimirPiramides():

    print("\n")
    print("PIRÁMIDES DE NÚMEROS")
    print("----------------------------------")
    numero = 0
    for numeros in range (1,10):
        numero = numero * 10 +numeros
        ocho = 8
        resultado = numero * ocho + numeros
        print(numero,"*",ocho,"+",numeros,"=",resultado)
    print("\n")
    variable = 0
    for unos in range (1,10):
        variable = variable * 10 + (unos + (1 - unos))
        cuadrado = variable ** 2
        print(variable,"*",variable ,"=", cuadrado)

#FUNCIÓN PRINCIPAL DEL PROGRAMA
def main():
        print("MENÚ TAREA 05: ")
        print("----------------------------------")
        print("1. Dibujar Cuadros y Círculos")
        print("2. Dibujar Espiral")
        print("3. Dibujar Círculos")
        print("4. Dibujar Parábolas")
        print("5. Aproximar PI")
        print("6. Contar Divisibles Entre 19")
        print("7. Imprimir Pirámides de Números")
        print("0. Salir")
        print("\n")
        entrada = int(input("¿QUÉ DESEA HACER?: "))
        while not entrada == 0:
            if entrada == 1:
                print("\n")
                print("FIGURA CUADROS Y CÍRCULOS")
                print("----------------------------------")
                dibujarCuadrosCirculos()
            elif entrada == 2:
                print("\n")
                print("FIGURA ESPIRAL")
                print("----------------------------------")
                dibujarEspiral()
            elif entrada == 3:
                print("\n")
                print("FIGURA CÍRCULOS")
                print("----------------------------------")
                dibujarCirculos()
            elif entrada == 4:
                print("\n")
                print("FIGURA PARÁBOLAS")
                print("----------------------------------")
                dibujarParabolas()
            elif entrada == 5:
                print("\n")
                print("APROXIMACIÓN DE PI")
                print("----------------------------------")
                n = int(input("Ingrese un número. Recuerde que entre mayor sea su número, el valor de π²/6 será más aproximado: "))
                aproximarPI(n)

            elif entrada == 6:
                contarDivisibles()
            elif entrada == 7:
                imprimirPiramides()
            else:
                print("ERROR, Escriba un número válido (0 al 7)")
            print("\n")
            print("MENÚ TAREA 05")
            print("1. Dibujar Cuadros y Círculos        5. Aproximar PI")
            print("2. Dibujar Espiral                   6. Contar Divisibles Entre 19")
            print("3. Dibujar Círculos                  7. Imprimir Pirámides de Números")
            print("4. Dibujar Parábolas                 0. Salir")
            print("\n")
            entrada = int(input("¿QUÉ MÁS DESEA HACER?: "))


        print("\n")
        print("¡HASTA LUEGO!")
        pygame.quit()

main()
