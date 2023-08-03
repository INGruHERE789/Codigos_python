contador = 0

while contador<10 :
    print("iteracion", contador)
    contador+=1

while True :
    print("iteracion", contador)
    contador+=1
    if contador==20 :
        break

#######################################################################################################

x="Alonso"

for letra in x :
    print(letra)

for i in range(5) :
    print (i)

for i in range(len (x)) :
    print (x[i])

x= ["Alonso", "Jose Luis", "Alondra", "Heber", "Miranda" ]

for nombre in x :
    print (nombre)

x= ("Alonso", "Jose Luis", "Alondra", "Heber", "Miranda" )

for nombre in x :
    print (nombre)

x= {"Alonso", "Jose Luis", "Alondra", "Heber", "Miranda" }

for nombre in x :
    print (nombre)

x= {"Alonso" : "Hijo Mayor", "Jose Luis" : "Padre", "Alondra" : "Madre", "Heber" : "Hijo de enmedio", "Miranda" : "Hija menor" }

for clave , descripcion in x.items() : #values, keys, items
    print (clave , descripcion)

