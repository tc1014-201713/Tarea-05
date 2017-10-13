def dividir_29():
    numero=0
    for i in range (1000,10000):
        if i&29==0:
            numero += 1
    return (numero)
def main():
    numero= dividir_29()
    print(numero)
main()