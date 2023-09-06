op=1
while op >=1 and op<=4:
    n1=input("Ingrese un numero\n")
    n1=float(n1)
    n2=input("Ingrese otro numero\n")
    n2=float(n2)
    print ("Ingrese la operacion que desea realizar\n")
    print ("1. Suma\n")
    print ("2. Resta\n")
    print ("3. Multiplicacion\n")
    print ("4. Division\n")
    print ("Cualquier otro numero terminara el codigo\n")
    op=input()
    op=int(op)
    if op == 1:
        resul=n1+n2
        print("El resultado de la suma es: ", resul, "\n")
    elif op == 2:
        resul=n1-n2
        print("El resultado de la resta es: ", resul, "\n")
    elif op == 3:
        resul=n1*n2
        print("El resultado de la multiplicacion es: ", resul, "\n")
    elif op == 4:
        resul=n1/n2
        print("El resultado de la division es: ", resul, "\n")
else:
    print ("Adios po\n")
