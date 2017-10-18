#encoding: UTF-8
#Autor: Sebastian Morales Martin
#TAREA05: Ciclos For
import pygame
import random
import math


ANCHO = 800                         #parámetros para las ventanas de pygame
ALTO = 800
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)


def dibujarParabolas(): #dibujara las parabolas que tienen 10 pixeles de distancia entre cada una y cambian de color dos veces cada segundo
    pygame.init()
    ventanaParabola = pygame.display.set_mode((ANCHO, ANLTO))
    end = False

    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        ventana.fill(COLOR_BLANCO)
        for change in range(0, 405, 10):
            colorParabolas = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pygame.draw.line(ventanaParabola,colorParabolas, (400 + cambio,400),(400,0+cambio))
            pygame.draw.line(ventanaParabola, colorParabolas, (400 + cambio, 400), (400, 0 + cambio))
            pygame.draw.line(ventanaParabola, colorParabolas, (400 - cambio, 400), (400, 0 + cambio))
            pygame.draw.line(ventanaParabola, colorParabolas, (400 - cambio, 400), (400, 0 + cambio))

        pygame.display.flip()
        reloj.tick(2)
    pygame.quit()

def dibujarCirculosYCuadros(): #dibuja un patrón de circulos y cuadrados, distanciados de entre el mas grande y el más pequeño por 10 pixeles
    pygame.init()
    ventanaCirculosYCuadrados = pygame.display.set_mode((ANCHO, ANLTO))
    end = False

    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        ventana.fill(COLOR_BLANCO)
        for cuadrado in range(0,400,10):
            pygame.draw.rect(ventanaCirculosYCuadrados, COLOR_NEGRO(cuadrado, cuadrado, ANCHO - (2*cuadrado), ALTO(2*cuadrado)),1)
        for circulo in range(0,400,10):
            pygame.draw.circle(ventanaCirculosYCuadrados, COLOR_NEGRO(ANCHO // 2, ALTO // 2), (400) - circulo, 2)

        pygame.display.flip()

    pygame.quit()

def dibujarEspiral(): #dibuja la espiral del centro hacia afuera con el cambio constante de seno y coseno, genereando triángulos, que cada vez se hacen más grades
    pygame.init()
    ventanaEspiral = pygame.display.set_mode((ANCHO, ANLTO))
    end = False

    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        ventana.fill(COLOR_BLANCO)
        x = 400
        y = 400
        variable = 10
        constante = variable/2

        for anngulo in range(0,14400, 90):
            anguloCalculos = math.radians(angulo)
            cosenoAngulo = math.cos(anguloCalculos)
            senoAngulos = math.sin(anguloCalculos)
            variableX = int(variable*cosenoAngulo)
            variableY = int(variable*cosenoAngulo)

            pygame.drawline(ventanaEspiral, COLOR_NEGRO,(x,y), (x+variableX, y-variableY), 1)

            x = x + variableX
            y = y - variableY
            variable = variable + constante

        pygame.display.flip()
    pygame.quit()

def encontrarDivisoresDe29(): #busca los divisores de 29, en números de 4 dígitos específicamente
    x=0

    for i in range(1000,9999):
        y=i%29

        if y==0:
            x=x+1

        else:
            x=x

    return(x)

def piramidesNumeros(): #imprime dentro de la caja de comandos de PyCharm una pirámide de números
    piramide = 1

    for variable in range(1, 10):

        resultado = piramide * 8 + variable
        print("%d X 8 + %e = %f"%(piramide, variable, resulrado))
        piramide = (piramide * 10) + (variable + 1)

    print("")

    numeros = 1

    for i in range(10):

        resultadocuadrado = numeros * numeros
        print(numeros, "X", numeros, "=", resultadocuadrado)
        numeros = (numeros * 10) + 1

def aproximarPi(intentos): #aproxima a PI dependiendo de ina variable que le des de INPUT, mientras sea más grande la variable, con mayor precision será el resultado
    x = 0

    for i in range(1, intentos):
        x = x + (1 / (i ** 2))

    x = x * 6
    x = x ** .5

    return(x)

def main(): #compila todas las funciones en un menu dencillo de usar para el usuario
    print("Tarea: Seleccione la opción que desee:")
    print("Por favor sólo introduce estos números, de lo contrario habrá error y se cerrará la aplicación")
    print("1- Parábolas de arcoiris")
    print("2- Dibujo de Cuadrados y Circulos")
    print("3- Espiral")
    print("4- ¿Divisor de 29?")
    print("5- Pirámides de Números")
    print("6- Aproximación de PI")
    print("0- Salir")
    problemaSeleccionado = int(input("¿Qué desea hacer? "))
    print("")
    print("------------------------------------------------------") #agregado por estética
    print("")
    if problemaSeleccionado == 0:
        break
    elif problemaSeleccionado == 2:
        dibujarCirculosYCuadros()
    elif problemaSeleccionado == 3:
        dibujarEspiral()
    elif problemaSeleccionado == 4:
        print("La cantidad de números de cuatro digitos divisibles entre 29 es de: %d"% (encontrarNumerosDivisiblesEntre29()))
    elif problemaSeleccionado == 5:
        piramidesNumeros()
    elif problemaSeleccionado == 6:
        aproxPi = int(input("Ingresa un número entero para determinar Pi. mimentras mayor sea tu número, más preciso será el resultado dado por la función "))
        print("La aproximación de Pi con %d intentos es de: %e"% (aproxPi, aproximarPi(aproxPi)))
    elif problemaSeleccionado == 1:
        dibujarParabolas()
    else:
        print("ERROR, No seleccionó un número de las opciones anteriores")



main()