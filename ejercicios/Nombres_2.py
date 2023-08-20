import os
os.system("cls")

while True :
    try : 
        cant_nomb = (input("Cuantas personas quieres agregar?\n"))
        cant_nomb = int(cant_nomb)
        break
    except ValueError :
        print(f"Lo que escribiste ({cant_nomb}) no es un numero")
os.system("cls")

nombres = []

for i in range(cant_nomb) :
    nombre = input(f"Escribe el nombre numero {i+1} de la lista"+"\n")
    nombres.append(nombre.capitalize())


tamaños = {}
for nombre in nombres :
    tamaño = len(nombre)
    if tamaño in tamaños :
        tamaños[tamaño].add(nombre)
    else :
        tamaños[tamaño] = {nombre}
os.system("cls")

    

print(f"El nombre con mas caracteres es : {tamaños[max(tamaños)]}")
