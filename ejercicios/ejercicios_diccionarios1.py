from csv import DictReader
from os import path
import pdb

"""
Ejercicos con diccionarios

Para esta actividad tenemos un diccionario con la informacion de 7 personas
El objetivo es responder las siguientes preguntas:
1.- Cual es el ahorro de Emmanuel Lazaro Contreras
2.- Cual es el ahorro de la familia Contreras Jimenez
3.- Cual es el ahorro total de todos los individuos

"""
def leer_csv():
    """Lee la informacion de un archivo csv"""
    ruta_ejercicios = path.dirname(__file__) 
    ruta_datos = path.join(ruta_ejercicios, "..", "Datos", "Ahorros.csv")
    ruta_interpretada = path.abspath(ruta_datos)
    with open(ruta_interpretada) as fp:
        data  = list(DictReader(fp))
        fp.close()
    return data

def main():
    """Funcion principal de este mudulo
    
    Abre un archivo tipo csv y obtiene su informacion para un posterior 
    procesamiento.
    """
    datos = leer_csv()
   # print (datos)

    Ahorro = 0.0
    AhorroCJ = 0.0
    Ahorrototal = 0.0

    for Ahorrador in datos : 
        Ahorrototal += float(Ahorrador["Ahorro"])
        if Ahorrador["Apellido paterno"] == "Contreras" and Ahorrador["Apellido Materno"] == "Jimenez" :
            AhorroCJ += float(Ahorrador["Ahorro"])
        if Ahorrador["Nombre"] == "Emmanuel" and Ahorrador["Apellido paterno"] == "Lazaro" and Ahorrador["Apellido Materno"] == "Contreras":
            Ahorro = float(Ahorrador["Ahorro"])
    print("El ahorro de Emmanuel es : ", Ahorro)
    print("El ahorro de la familia Contreras Jimenez es de: ", AhorroCJ)
    print("El ahorro de todos los individuos es de: ", Ahorrototal)





if __name__ == "__main__":
    main()