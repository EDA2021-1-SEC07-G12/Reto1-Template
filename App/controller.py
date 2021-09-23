"""
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
import time


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

def organizar_fechas(catalog):
    inicial= int(input("Inserte fecha inicial "))
    final= int(input("Inserte fecha final "))
    return model.ordernarCronologicamente(inicial,final,catalog)


def organizar_obras(catalog):
    dia1=int(input("Inserte dia inicial : "))
    mes1=int(input("Inserte mes inicial : "))
    anio1=int(input("Inserte año inicial : "))

    dia2=int(input("Inserte dia final : "))
    mes2=int(input("Inserte mes final : "))
    anio2=int(input("Inserte año final : "))
    
    return model.ordenarObras(dia1,mes1,anio1, dia2, mes2,anio2,catalog)
   
def clasificar_obras_por_tecnica(catalog):
    nombre=input("Inserte nombre del artista: ")
    return model.clasificar_obras_por_tecnica(nombre,catalog)


def clasificar_obras_por_nacionalidad(catalog):
    
    
    
    dict_top_10= model.requerimiento_4_1(catalog)
    init3_ult3=model.requerimiento_4_2(catalog,dict_top_10[1])
    
    
    
    return (dict_top_10[0],init3_ult3)
def requerimiento5(catalog):
    
    departamento= input("Inserte nombre del departamento: ")
    
    req5=model.requerimiento5(catalog, departamento)
    
    
    
    return model.requerimiento5(catalog, departamento)

def requerimiento6(catalog):
    inicial=int(input("Inserte año inicial: "))
    final=int(input("Inserte año final: "))
    area=float(input("Introduzca area "))
    return model.requerimiento6(catalog,inicial,final,area)




#
# 
#  Funciones de ordenamiento



