cant_nomb = int(input("Cuantas personas quieres agregar?\n"))

nombres = []

for i in range(cant_nomb) :
    nombre = input(f"Escribe el nombre numero {i+1} de la lista"+"\n")
    nombres.append(nombre)

tamaños = {}
for nombre in nombres :
    tamaño = len(nombre)
    if tamaño in tamaños :
        tamaños[tamaño].append(nombre)
    else :
        tamaños[tamaño] = [nombre]
    

print(f"El nombre con mas caracteres es : {tamaños[max(tamaños)]}")
