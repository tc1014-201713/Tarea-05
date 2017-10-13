#encoding: UTF-8
#Autor: Javier Martínez Hernández      A01375496
#Descripción:  En este programa se juntaran todas varios elementos a a ejecutar
import math
from random import randint
import pygame

ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

def calculaEImprimeDivisibles29():
    #Esta funcion calculara los numeros divisibles de 4 digitos entre 29
    numerosDividios=[] #lista vacia
    for numeroDivisible in range(1000,10000): #rango de los numerosde 4 digitos
        if numeroDivisible%29==0: #agregaran los valores de 4 digitos dividios exctamente entre 29
                numerosDividios.append(numeroDivisible)
    print ("El conteo total de los numeros de 4 digitos divisibles exactamente entre 29 son ", len(numerosDividios))
    main()
def sacarEImprimirPiramidesNumeros():
    #sacara las piramides de numeros
    numeroDesdeString=""  #se hara un string vacio para agregar los numeros
    for numeroCambiante in range (1,10): #los valores de la piramide serán del 1-9
        numeroString=str(numeroCambiante) #se cambia a string el numero para poder adicionarlo al Numero string
        numeroDesdeString+=numeroString
        resultado=int(numeroDesdeString)*8+numeroCambiante #Se cambia el numero que contiene el numeroDesdeString para poder hacer la multiplicación
        print("%s x 8 + %d = %d"% (numeroDesdeString,numeroCambiante, resultado))

    valorInicial="1"
    for valorDeVeces in range (1,10):
        multiplicaciónSTR=valorInicial*valorDeVeces
        resultadoNumeroDos=int(multiplicaciónSTR)*int(multiplicaciónSTR)
        print("%s x %s = %d"%(multiplicaciónSTR,multiplicaciónSTR,resultadoNumeroDos))
    main()
def aproximaEimprimePi(aproximacion): #aproximaciones de pi
    sumaMaxima=0 #se crea un aumento para despues usarlo
    for valorDenominador in range (1,aproximacion+1): #se hace el rango para aproximar pi
        resultadoDivisión=1/valorDenominador**2 #operacion necesaria
        sumaMaxima+=resultadoDivisión #aqui se muestra donde se usa el aumeto
    porSeis=sumaMaxima*6
    resultadoAproximado=math.sqrt(porSeis)#operaciones finales
    print("Tu valor aproximado de pi es %f"%resultadoAproximado)
    main()
def dibujaCuadrosCirculos():# se dibujaran los rectangulos sobrepuestos de los circulos
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range (1,ANCHO//2,10):
        # Dibujar, aquí haces todos los trazos que requieras
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), x, 1) #se dibujaran los circulos
            pygame.draw.rect(ventana,NEGRO,(x,x,ANCHO-x*2,ALTO-x*2),1) #se dibujan los rectangulos

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame
    main()
def dibujaParabolas():
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)
        ALEATORIO = randint(0, 255), randint(0, 255), randint(0, 255)
        for x in range (0,ANCHO//2,10):
        # Dibujar, aquí haces todos los trazos que requieras   #se hacen 4 lineas las cuales seran las que haran la parabola
            pygame.draw.line(ventana,ALEATORIO,(ANCHO//2,ALTO//2+x),(0+x,ALTO//2),1 )  #linea 1
            pygame.draw.line(ventana,ALEATORIO,(ANCHO//2+x,ALTO//2),(ANCHO//2, 0+x),1) #linea 2
            pygame.draw.line(ventana,ALEATORIO,(0+x,ALTO//2),(ANCHO//2,ALTO//2-x),1)  #linea 3
            pygame.draw.line(ventana, ALEATORIO,(ANCHO//2,ALTO//2+x),(ANCHO-x,ALTO//2),1) #linea 4
        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame
    main()
def dibujaEspiral():
    #se crea una espiral
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range(0,ANCHO//2,10):
            # Dibujar, aquí haces todos los trazos que requieras
            # estas tres pimeras lineas delimitan lo que son los lados horizontales
            #la tercera linea es la que se usa para la conexión en la espiral
            pygame.draw.line(ventana,NEGRO,(ANCHO//2,ALTO//2),(ANCHO//2+10,ALTO//2),1)
            pygame.draw.line(ventana, NEGRO,(ANCHO//2-x,ALTO//2-x),(ANCHO//2+x,ALTO//2-x),1)
            pygame.draw.line(ventana, NEGRO,(ANCHO//2+x+10,ALTO//2+x),(ANCHO//2-x,ALTO//2+x),1)

            #estas tres lineas delimitan los lados verticales
            #igualmente la tercera linea es la que se usa para la conexión de la espiral
            pygame.draw.line(ventana, NEGRO, (ANCHO//2+10,ALTO//2-10),(ANCHO//2+10,ALTO//2),1)
            pygame.draw.line(ventana, NEGRO, (ANCHO//2-x,ALTO//2+x),(ANCHO//2-x,ALTO//2-x),1)
            pygame.draw.line(ventana, NEGRO, (ANCHO//2+x+10,ALTO//2-x-10),(ANCHO//2+x+10,ALTO//2+x),1)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame
    main()
def dibujaCirculos():
    #se crearan los 12 circulos de radio 150

    radio=150
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        for angulo in range(0, 360,30):
            # Dibujar, aquí haces todos los trazos que requieras
            anguloRadianes=angulo*math.pi/180 #transforma los angulos en radianes
            pygame.draw.circle(ventana,NEGRO,((ANCHO//2+int(radio*math.cos(anguloRadianes)),ALTO//2+int(radio*math.sin(anguloRadianes)))),radio,1)#con esta linea se hacen los 12 circulos

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame
    main()

def main():
    #este es el menu principal donde se escogera lo que se querra hacer
    variableSeleccion=int(input('''Menú principal de tarea 5 ¿Qué quiere hacer?
    1. Dibujar cuadros y circulos
    2. Dibujar una espiral
    3. Dibujar circulos
    4. Dibujar parabolas
    5. Aproximar pi
    6. Contar los numero divisibles entre 29 de 4 numeros
    7. Imprimir piramides de numeros
    0. Salir 
    ¿Que desea hacer?: '''))
    if variableSeleccion==1:
        dibujaCuadrosCirculos()
    elif variableSeleccion==2:
        dibujaEspiral()
    elif variableSeleccion==3:
        dibujaCirculos()
    elif variableSeleccion==4:
        dibujaParabolas()
    elif variableSeleccion==5:
        aproximacion=int(input("Hasta con que numero quieres aproximar pi: "))
        aproximaEimprimePi(aproximacion)
    elif variableSeleccion==6:
        calculaEImprimeDivisibles29()
    elif variableSeleccion==7:
        sacarEImprimirPiramidesNumeros()
    elif variableSeleccion==0:
        print("Gracias por su tiempo")
    else:
        print("Escoja una opción viable")
        main()
main()