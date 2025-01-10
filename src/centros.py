import csv
from collections import namedtuple
from coordenadas import *
from mapas import *

Coordenadas = namedtuple('Coordenadas', 'latitud longitud')
CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_discapacitados, tiene_uci')


def leer_centros (fichero): #ubicacion pasaa ser coordenadas?
    with open (fichero, encoding='utf-8') as f:
        lector = csv.reader (f, delimiter=';')
        next (lector)
        res = []
        centros_sanitarios = []
        for nombre, localidad, latitud, longitud, estado, num_camas, tiene_acceso_discapacitados, tiene_UCI in lector:
            localidad = localidad.strip ()
            latitud = float (latitud.strip ())
            longitud = float (longitud.strip ())
            estado = estado.strip ()
            num_camas = int (num_camas.strip ())
            tiene_acceso_discapacitados = tiene_acceso_discapacitados.strip () == 'true'
            tiene_UCI = tiene_UCI.strip () == 'true'
            # Para que la namedtuple una la latitud y la longitud en coordenadas hay que crear una 
            coordenadas = Coordenadas (latitud, longitud)
            res.append (CentroSanitario (nombre, localidad, coordenadas, estado, num_camas, tiene_acceso_discapacitados, tiene_UCI))
    return res



def calcular_total_camas_centros_accesibles(lista):
    total_camas = 0
    for centro in lista:
        if centro.acceso_discapacitados == True:
            total_camas += centro.num_camas
    return total_camas



def obtener_centros_con_uci_cercanos_a(lista, coordenadas, umbral):
    res = []

    for centro in lista:
        if centro.tiene_uci and calcular_distancia(centro.coordenadas, coordenadas) <= umbral:
                res.append((centro.nombre, centro.localidad, centro.coordenadas))
    return res

def generar_mapa (nombres_localidades_coordenadas):
    coordenadas = [coord  for _, _, coord in nombres_localidades_coordenadas]
    media_coord = calcular_media_coordenadas(coordenadas)
    mapa = crea_mapa (media_coord)
    #Coordenadas = coordinates (coordenadas[0], coordenadas[1])
    for nombre, localidad, coord in nombres_localidades_coordenadas:
        agrega_marcador (mapa, coord, nombre + "("+ localidad + ")", "purple")
    guarda_mapa(mapa, "./data/mapa.html")




if __name__ == "__main__":
    datos = leer_centros("data\\centrosSanitarios.csv")
    #print(datos)

    #print(f"{calcular_total_camas_centros_accesibles(datos)}")

    #print(f"{obtener_centros_con_uci_cercanos_a(datos, Coordenadas(40.4168, -3.7037), 4.1)}")