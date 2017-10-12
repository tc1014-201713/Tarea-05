from math import *
def Ejercicio_Pi(n):
    pi_cuadrada = 0
    for i in range(1,n+1):
        pi_cuadrada+=1/(i**2)
        pi=sqrt(6*pi_cuadrada)

        return pi


def main():
    ultimo_denominador=int(input("Dame un valor numerico: "))
    pi=Ejercicio_Pi(ultimo_denominador)
    print(pi)
main()