#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Escribir una función que calcule cuántos cnúmeros	de 4 dígitos son divisibles entre 29.
def calcularNumeros():
    n=0
    for k in range(1000,100000):
        if k%29==0:
            n+=1
    return k


def main():
    print("Los numeros divisibles son:",calcularNumeros())



main()