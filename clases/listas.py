from copy import deepcopy

#Crear lista vacia 
x = []
y = list()
print(x,y)

#Lista con elementos
x = [2,4,8,4,45,"gato",(3,8,25,"perro"),False]

#   Acceder a elemento con indice positivo
print(x[5][3])

#   Acceder a elementos con indices negativos
print(x[-2][-1])

#   Modificar un elemento
x[5] = (3,8,25,"gallina")
print(x)

#    Convertir una lista a tupla
y = tuple(x)
print(y)

#    Convertir una lista a un conjunto
y = set(x)
print(y)

#    Copiar una lista

z = x #Comparten la misma informacion en memoria
w = deepcopy(x) #Genera una copia con informacion diferente
p = list(x)

x[0]+= 8
print (x)
print(z)
print(p)
print(w)

#   Anadir elementos a lista
x.append(w) #Anadir al final
print(x)

x.insert(0,"Tlacuache") #Anadir en un indice en especifico
print(x)

#Eliminar elementos de una lista
x.remove("Tlacuache")
print(x)

#   Eliminar por posicion
k = x.pop(4)
print(k)
print(x)

#    Contar elementos en una lista
l = x.count(4)
print(l)

l = x.count("perro")
print(l)

#   Ordenar en una lista
x = [8,9,56,48,3,7,10,-56,-2,-79]
x.sort()    #Ascendente
print(x)
x.sort(reverse=True)    #Descendente
print(x)

#   Sumar listas
x = [5,69,25]
y = [48,2,9]
print(x+y)

z = x + y
print(z)

x.extend(y)
print(x)

# Busqueda de un elemento
idx = x.index(2, 4)
print(idx,x)

# Saber si un elemento esta en una lista

t = 2 in x
print(t)

#   Invertir una lista
x.reverse()
print(x)

#   Limpia la lista
x.clear()
print(x)

#   Saber el tamano de una lista
print(x.__len__())

print(len(x)) #Con funciones