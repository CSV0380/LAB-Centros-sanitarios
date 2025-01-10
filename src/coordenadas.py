from collections import namedtuple
import math
from centros import *

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')


def calcular_distancia(coordenadas1, coordenadas2):
    latitud1, longitud1 = coordenadas1
    latitud2, longitud2 = coordenadas2
    return math.sqrt((latitud2 - latitud1) ** 2 + (longitud2 - longitud1) ** 2)


def calcular_media_coordenadas(lista):
    suma_latitudes = 0
    suma_longitudes = 0
    for centro in lista:
        suma_latitudes += centro.ubicacion.latitud
        suma_longitudes += centro.ubicacion.longitud
    
    media_latitud = suma_latitudes / len(lista)
    media_longitud = suma_longitudes / len(lista)
    
    return Coordenadas(media_latitud, media_longitud)



#if __name__ == "__main__":
    datos = leer_centros("data\\centrosSanitarios.csv")
    print(f"{calcular_media_coordenadas(datos)}")