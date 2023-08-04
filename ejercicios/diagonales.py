n = int(input("Ingrese el tamano del cuadro (entre 5 y 20): \n"))

if n >= 5 and n <=20 :
    for i in range(n) :
        for j in range(n) :
            if i==j or i==n - j -1 :
                print("=",end="")
            else :
                print("0",end="")

        print("")
else: 
    print("Valor fuera de rango")
