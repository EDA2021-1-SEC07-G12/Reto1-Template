﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import abc
import config as cf
import model
import csv
import datetime



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Inicialización del Catálogo de libros
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtist(catalog)
    loadArtWork(catalog)
    

# Funciones para la carga de datos



def loadArtist(catalogo):
    booksfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalogo, Artist)


def loadArtWork(catalogo):
    booksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for ArtWorks in input_file:
        model.addArtwork(catalogo, ArtWorks)

def ultimosArtistas(catalog):

    return model.UltimosArtistas(catalog)


def ultimasObras(catalog):
    
    return model.UltimasObras(catalog)

# Funciones de ordenamiento



#def ordernarCronologicamente(inicio,final, catalogo):
    lista= lt.newList("ARRAY_LIST")
    for i in catalogo:
        fecha= catalogo["BeginDate"]

        if inicio<fecha<final
            lista=lt.addlast(i)
   


        
# Funciones de consulta sobre el catálogo




    
   



print(comparacionAnios(15/2/2021,"",""))

