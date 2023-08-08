exp = int(input("Ingresa el valor del exponente para calcular su triangulo de pascal (Entre 0 y 20) \n"))

if exp<1 or exp>20 :
    print("Valores fuera de rango")
else :
    for i in range(exp+1) :
        for j in range(i+1) :
            if i==0 or j==0 :
                num = 1
            else :
                num = num * (i-j+1) / j
            print(int(num), end=" ")
        print()
