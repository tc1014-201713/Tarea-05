# Encoding: UTF-8
#Autor: Viviana Osorio Nieto
#Crear un menu con diferentes funciones como dibujar o aproximar valores.
import pygame
blanco =(255, 255, 255)
negro = (0, 0, 0)
reloj = pygame.time.Clock()
def  dibujarCuadradosyCirculos():
    pygame.init()
    dimensiones = (800, 800)
    pantalla = pygame.display.set_mode(dimensiones)
    done = False
    while not done:
        r = 0
        r = r + 10
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                done = True
            pantalla.fill(blanco)
            while r <= 800:
                r = r + 10
                pygame.draw.rect(pantalla, negro, [400 - r, 400 - r, 2 * r, 2 * r], 1)
                pygame.draw.ellipse(pantalla, negro, [400 - r, 400 - r, 2 * r, 2 * r], 1)
                pygame.display.flip()
                reloj.tick(11)
    pygame.quit()
    main()

def dibujarParabola():
    pygame.init()
    dimensiones = (800, 800)
    pantalla = pygame.display.set_mode(dimensiones)
    done = False
    while not done:
        r = 0
        r = r + 10
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                done = True
            pantalla.fill(blanco)
            while r <= 400:
                r = r + 10
                pygame.draw.line(pantalla, negro, [400 + r, 400], [400, 800 - r], 1)
                pygame.draw.line(pantalla, negro, [400 - r, 400], [400, 800 - r], 1)
                pygame.draw.line(pantalla, negro, [400 + r, 400], [400, 0 + r], 1)
                pygame.draw.line(pantalla, negro, [400 - r, 400], [400, 0 + r], 1)
                pygame.display.flip()
                reloj.tick(11)
    pygame.quit()
    main()

def dibujarEspiral ():
    pygame.init()
    dimensiones = (800, 800)
    pantalla = pygame.display.set_mode(dimensiones)
    done = False
    while not done:
        r = 0
        r = r + 10
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                done = True
            pantalla.fill(blanco)
            for r in range(0, 400, 10):
                pygame.draw.line(pantalla, negro, (400 - r, 400- r), (400+ r, 400- r), 1)
                pygame.draw.line(pantalla, negro, (400+ r + 10, 400+ r), (400- r, 400+ r), 1)
                pygame.draw.line(pantalla, negro, (400+ 10, 400 - 10), (400+ 10, 400), 1)
                pygame.draw.line(pantalla, negro, (400- r, 400+ r), (400- r, 400- r), 1)
                pygame.draw.line(pantalla, negro, (400+ r, 400- r), (400+ r, 400+ r), 1)

            pygame.display.flip()
            reloj.tick(40)

        pygame.quit()

        main()


def dibujarCirculos ():
    pygame.init()
    dimen = (800, 800)
    pantalla = pygame.display.set_mode(dimen)
    done = False
    while not done:
        x = 400
        y = 400
        r = 0
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                done = True
            pantalla.fill(blanco)
            pygame.draw.circle(pantalla, negro, (550, 400), 150, 1)
            pygame.draw.circle(pantalla, negro, (400, 550), 150, 1)
            pygame.draw.circle(pantalla, negro, (250, 400), 150, 1)
            pygame.draw.circle(pantalla, negro, (400, 250), 150, 1)
            pygame.draw.circle(pantalla, negro, (540, 340), 150, 1)
            pygame.draw.circle(pantalla, negro, (340, 540), 150, 1)
            pygame.draw.circle(pantalla, negro, (490, 280), 150, 1)
            pygame.draw.circle(pantalla, negro, (280, 490), 150, 1)
            pygame.draw.circle(pantalla, negro, (340, 260), 150, 1)
            pygame.draw.circle(pantalla, negro, (260, 340), 150, 1)
            pygame.draw.circle(pantalla, negro, (300, 280), 150, 1)
            pygame.draw.circle(pantalla, negro, (510, 500), 150, 1)

            pygame.display.flip()
            reloj.tick(80)

    pygame.quit()
    main()
def aproximarValorPI(n):
    suma = 0
    contador = 0
    for d in range (1, n+1, 2):
        contador += 1
        if contador%2 == 1:
            suma = suma + 1/d
        else:
            suma= suma - 1/d
    return 4*suma
    main()
def calcularNum ():
    r = 0
    for n in range (1000,10000):
        if n%29 == 0:
            r = r-1
    print (n," numeros de 4 digitos son divisibles entre 29")
    main()
def main ():
  print("1- Dibujar circulos y cuadrados."
  
         "2- Dibujar parábolas."
  
         "3- Dibujar una espiral."
  
         "4- Dibujar circulos. "
  
         "5- Aproximar el valor de pi."
  
         "6- calcular cuantos numeros de 4 digitos son divisibles entre 29."
  
         "7- Calcular piramides de numeros."
  
        "8- salir :( ")

  N = int(input("Que quieres hacer?: "))
  done = False
  while not done:
      if N == 1:
        dibujarCuadradosyCirculos()
      elif N== 2:
          dibujarParabola()
      elif N== 3:
          dibujarEspiral()
      elif N== 4:
          dibujarCirculos ()
      elif N == 5:
          n = int(input("De que rango quiere hacer la aproximacion?"))
          print(aproximarValorPI (n))
          break
      elif N == 6:
          calcularNum ()
      elif N== 7:
          break



main()
