import requests
from bs4 import BeautifulSoup
import os

def get_poblacion():
    URL = r"https://es.wikipedia.org/wiki/Anexo:Países_y_territorios_dependientes_por_población"
    response = requests.get(URL) 
    if not response.ok:
        return None
    contenido = response.content.decode()
    poblacion = []
    soup =  BeautifulSoup(contenido, 'html.parser')
    if soup is None:
        return None
    tabla = soup.find('table' ,attrs={'class':"wikitable sortable"})
    if tabla is None:
        return None
    for row in tabla.find_all('tr'):
        aux = []
        for ele in row.find_all(['th', 'td']):
            dato = (ele.text.replace("\xa0", " "))
            x = ele.find('span', attrs={"style":"display:none;"})
            if x :
                aux.append(x.text)
            else:
                aux.append(dato)
        poblacion.append(aux)
    return poblacion

def procesar_datos():
    datos = get_poblacion()
    dicc_datos = {}
    for i, row in enumerate(datos):
        if i == 0:
            continue
        pais = row[1]
        poblacion = row[8]
        dicc_datos[pais] = poblacion

    while True:
        os.system("cls")
        pais_de_busqueda = input("Dime el nombre de un pais?\n")
        if pais_de_busqueda == "salir":
            break
        if pais_de_busqueda not in dicc_datos:
            print (f"El pais ({pais_de_busqueda}) no esta en la tabla")
        else:
            print (f"La poblacion de {pais_de_busqueda} es {dicc_datos[pais_de_busqueda]}")
        volver_jugar = input("Quieres Jugar otra vez? [Si(s)/No(n)]")
        if volver_jugar == "n":
            os.system("cls")
            break

if __name__ == "__main__":
    procesar_datos()