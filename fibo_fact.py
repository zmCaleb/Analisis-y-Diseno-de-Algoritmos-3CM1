def factos (n):
    facto=1
    for i in range (n, 1, -1):
        facto=facto*i
    print(facto)
def fibb(n):
    if n<2:
        return n
    else: 
        return fibb(n-1) + fibb(n-2)
cw=1
while (cw!=3):
    print("1. Fibbonachi \n")
    print("2. Factorial \n")
    print("3. Salir \n")
    cw=int(input())
    if (cw==1):
        N=int(input("Ingrese el numero al que se le desea sacar la sucesion de fibbonachi: \n"))
        print("Este es el numero: ", fibb(N))
    elif(cw==2):
        N=int(input("Introduzca el numero al que le desea sacar el factorial: \n"))
        factos(N)
    elif(cw==3):
        print("Adeu \n")
        break
    else:
        print ("No es una opcion valida \n")
