
def Hacer_Piramides():
    cuenta=0
    for i in range(1,10,1):
        for x in range (i+1,1,-1):
            cuenta+=(10**x)//100
        print("%d * 8 +%d = %d" % (cuenta, i, cuenta*8+i))
    print("\n")


    for i in range(0, 10, 1):
        factor=0
        for j in range(1, i + 1, 1):
            factor += 10 ** j
        factor+=1
        print("%d * %d = %d" %(factor, factor, factor * factor))
Hacer_Piramides()

