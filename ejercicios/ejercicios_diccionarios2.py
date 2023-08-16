import requests
from bs4 import BeautifulSoup

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
            dato = (ele.text.replace("\xa0", ""))
            aux.append(dato)
        poblacion.append(aux)
    return poblacion

def procesar_datos():
    datos = get_poblacion()
    while True:
        pais = input("Dime el nombre de un pais?\n")
        if pais == "salir":
            break
        bandera = True
        for row in datos :
            if pais==row[1]:
                print("Los habitantes que tiene el pais son: ", row[8])
                bandera = False
                break
        if bandera :
            print("El pais no existe o no se encuentra en la lista")

        

if __name__ == "__main__":
    
    procesar_datos()