#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Calcular la aproximación de Pi con una función.

import math
def calcularPi(n):
    suma=0
    for valor in range (1,n+1):
        resultado= 1/n**2
        total=suma+resultado
    aproximacion=total
    raiz=math.pi**2/6
    return raiz, aproximacion






def main():
   n=int(input("¿Cual es el valor que quieres usar:"))
   print(calcularPi(n))




main()