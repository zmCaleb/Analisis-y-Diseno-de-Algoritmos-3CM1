def fact (n):
    if (n==1):
        return 1
    else:
        return n*fact(n-1)
    
def fibb(n):
    if n<2:
        return n
    else: 
        return fibb(n-1) + fibb(n-2)

c=1
while (c!=3):
    c=int(input("Ingrese la funcion que desea realizar\n"))
    if (c==1):
        mg=int(input("Ingrese el valor al que le desea sacar el factorial: "))
        print("\nEste es el factorial del valor ingresado: ", fact(mg))
        break
    elif(c==2):
        mg=int(input("Ingrese el valor al que le desea sacar la sucesion de fibbonacci: "))
        print("\nEste es el factorial del valor ingresado: ", fibb(mg))
        break
    elif(c==3):
        print("\nAdios\n")
    else:
        print("\nNO es una opcion valida\n")
