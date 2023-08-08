#   Diccionario vacio
dicc = {}

dicc_2 = dict()

#   Diccionario con datos

dicc = {"llave 1": "Valor 1", "llave 2": "Valor 2"}

print(dicc)

dicc_2 = dict({"llave 1": "Valor 1", "llave 2": "Valor 2"})
print(dicc_2)

#Como acceder a elementos

print(dicc["llave 2"])

#Como cachar un error
try :
    print(dicc["llave 3"]) #Error (Lanzara un key error por que la llave no existe)
except :
    pass

# Como modificamos un elemento

dicc["llave 1"] = 46882
print(dicc)

# Como agregar un elemento

dicc["llave 3"] = "Perro"
print(dicc)

# Como borrar un elemento
del dicc["llave 3"]
print(dicc)

print(dir(dicc))

# Metodos de un diccionario
llaves = dicc.keys()
print(llaves)

valores = dicc.values()
print(valores)

llaves, valores = dicc.items()
print(llaves, valores)

valor = dicc.pop("llave 2") # Elimina una llave
print(valor)
print(dicc)


dicc["llave 3"] = "Perro"
llave, valor = dicc.popitem() # Elimina la ultima llave que se ingreso
print(llave, valor)
print(dicc)

dicc["llave 3"] = "Perro"
dicc.update(dicc_2)         # Se agrega el contenido del segundo diccionario en el primero
print(dicc)
print(dicc_2)   # No quedan ligados

# print(help(dicc.setdefault))  Ayuda

# Asignacion de elementos pero bloqueando la actualizacion en caso de que ya exista una llave
x = dicc.setdefault("llave 3", "gato")      # Esta llave ya existe
print(x)
print(dicc)
x = dicc.setdefault("llave 4", "gato")      #Esta llave no existe
print(x)
print(dicc)            

#Limpiar un diccionario

dicc.clear()
print(dicc)