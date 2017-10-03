#encoding: UTF-8
#Autor: Aaron Villanueva
#Este programa hace muchas cosas.
#Espirales
#Calculos
#Pi
def aproximarPi(intentos):
    x = 0
    for i in range(1, intentos):
        x = x + (1 / (i ** 2))
    x = x * 6
    x = x ** .5
    return(x)

def encontrarNumerosDivisiblesEntre29():
    x=0
    for i in range(1000,9999):
        y=i%29
        if y==0:
            x=x+1
        else:
            x=x
    return(x)

def piramidesNumeros():
    piramide = 1
    for factor in range(1, 10):
        resultado = piramide * 8 + factor
        print(piramide, "X 8 +", factor, "=", resultado)
        piramide = (piramide * 10) + (factor + 1)
    print("")
    numeros = 1
    resultadocuadrado = 1
    for i in range(10):
        resultadocuadrado = numeros * numeros
        print(numeros, "X", numeros, "=", resultadocuadrado)
        numeros = (numeros * 10) + 1


def Main():
    print("Tarea 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar espiral")
    print("3. Dibujar círculos")
    print("4. Dibujar parabolas")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 29")
    print("7. Imprimir piramides de números")
    print("0. Salir")
    eleccion=int(input("¿Qué desea hacer?"))
    respuesta=True
    while respuesta==True:
        if eleccion==0:
            print("saliendo")
            respuesta=False
        elif eleccion==1:
            dibujarCuadrosCirculos()
        elif eleccion==2:
            dibujarEspiral()
        elif eleccion==3:
            dibujarCirculos()
        elif eleccion==4:
            dibujarParabolas()
        elif eleccion==5:
            final=int(input("Ingrese un número entero para determinar Pi. Entre mayor sea, más exacto el resultado"))
            print("La aproximación de Pi con", final,"intentos es de:",aproximarPi(final))
        elif eleccion==6:
            print("El número de números de cuatro digitos divisibles entre 29 es:",encontrarNumerosDivisiblesEntre29())
        elif eleccion==7:
            print(piramidesNumeros())
        else:
            print("error. Número no localizado")

Main()
