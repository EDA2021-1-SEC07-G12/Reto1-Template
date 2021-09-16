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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt


from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs


assert cf
import re
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
#def importar(texto):

   # if texto=="1":
   #     from DISClib.Algorithms.Sorting import quicksort as sa 

def newCatalog():

    catalogo={"lista_obras":None,
                "lista_artistas":None
    }

    lista_obras= lt.newList("ARRAY_LIST")
    lista_artistas= lt.newList("ARRAY_LIST")

    catalogo["lista_obras"] = lista_obras
    catalogo["lista_artistas"] = lista_artistas

    return catalogo



    
    

# Funciones para agregar informacion al catalogo

def addArtist(catalogo, artista):
    lt.addLast(catalogo['lista_artistas'], artista)
    # Se obtienen los autores del libro
    #authors = artista['lista_artistas'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    ## crea un libro en la lista de dicho autor (apuntador al libro)
   # Funcionesfor author in authors:
     #   addBookAuthor(catalog, author.strip(), book)



def addArtwork(catalogo, artwork):
    lt.addLast(catalogo['lista_obras'], artwork)
# Funciones para creacion de datos
def UltimosArtistas(catalogo):
    lista_artistas= catalogo["lista_artistas"]
    print("El numero de artistas es " + str(lt.size(lista_artistas)))
    lista_artistas = lt.subList(lista_artistas,lt.size(lista_artistas)-3,3)
    

    return lista_artistas



def UltimasObras(catalogo):
    lista_obras= catalogo["lista_obras"]
    print("El numero de obras es " + str(lt.size(lista_obras)))
    lista_obras = lt.subList(lista_obras,lt.size(lista_obras)-3,3)
    return lista_obras



# Funciones de consulta

def ordernarCronologicamente(inicio,final, catalogo):
    
    lista= lt.newList("ARRAY_LIST")

    lista_artistas= catalogo["lista_artistas"]

    for i in range(lt.size(lista_artistas)):

        diccionario={}
        elemento=lt.getElement(lista_artistas,i)

        fecha = elemento["BeginDate"]
        if inicio<int(fecha)<final:
            diccionario["Nombre"] = elemento["DisplayName"]
            diccionario["Nacimiento"] = elemento["BeginDate"]
            if elemento["EndDate"]=="0":
                diccionario["Fallecimiento"] = "Desconocido"
            else:
                diccionario["Fallecimiento"] = elemento["EndDate"]

            diccionario["Nacionalidad"] = elemento["Nationality"]
            if elemento["Gender"]=="":
               diccionario["Genero"]="Desconocido" 
            else:
                diccionario["Genero"]= elemento["Gender"]
            lt.addLast(lista,diccionario)

    artistasOrdenados= sa.sort(lista,OrdenarFechas)
    return artistasOrdenados


def ordenarObras(inicio,final,catalogo, entrada, tamano):
    lista=lt.newList(entrada)
    
    lista_artistas=catalogo["lista_artistas"]
    lista_obras= catalogo["lista_obras"]

    for i in range(lt.size(lista_obras)):

        diccionario={}
        elemento=lt.getElement(lista_obras,i)

        
        fecha = elemento["DateAcquired"]

        if elemento["DateAcquired"]=="":
            fecha=0000

        if len(str(fecha))>5:
            fecha =fecha.split("-")
            fecha=fecha[0]
            
        if inicio<=int(fecha)<=final:
            
            
            
            
            diccionario["Titulo"] = elemento["Title"]
            
           # for j in range(lt.size(lista_artistas)):
               # elemento1=lt.getElement(lista_artistas,j)
              #  if elemento1["ConstituentID"]==elemento["ObjectID"]:
             #       diccionario["Autor"]= elemento1["DisplayName"]
            
            autor=elemento["ConstituentID"]
            autor=autor.replace("[","")
            autor=autor.replace("]","")
            autor=autor.split(",")

            for j in range(len(autor)):
                for k in range(lt.size(lista_artistas)):
                    texto = ""
                    elemento1=lt.getElement(lista_artistas,k)
                    if autor[j]==elemento1["ConstituentID"]:
                        texto= texto + " " + elemento1["DisplayName"]  
                        diccionario["Autores"] =  texto  
            diccionario["Fecha adquisicion"]=fecha
            diccionario["Medio"] = elemento["Medium"]
            diccionario["Dimensiones"] = elemento["Dimensions"]

            lt.addLast(lista,diccionario)
    
    orden= input("Inserte orden, 1 para ShellSort, 2 para Insertionsort, 3 para mergesort, 4 para quicksort ")
    fechasOrdenadas= sortBooks(lista,tamano, orden)
    return fechasOrdenadas

def sortBooks(catalog, size, elemento):
    sub_list = lt.subList(catalog, 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if elemento=="1":
        sorted_list = sa.sort(sub_list, OrdenarFechasObras)
    elif elemento=="2":
        sorted_list=ins.sort(sub_list, OrdenarFechasObras)

    elif elemento=="3":
        sorted_list=ms.sort(sub_list, OrdenarFechasObras)
    elif elemento=="4":
        sorted_list=qs.sort(sub_list, OrdenarFechasObras)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def clasificar_obras_por_tecnica(nombre,catalogo):
    lista_artistas=catalogo["lista_artistas"]
    lista_obras= catalogo["lista_obras"]

    lista=lt.newList("ARRAY_LIST")
    datos=0000
    for i in range(lt.size(lista_artistas)):
        elemento= lt.getElement(lista_artistas,i)

        if str(elemento["DisplayName"])==nombre:
            datos=str(elemento["ConstituentID"])

    for k in range(lt.size(lista_obras)):
        
        elemento1=lt.getElement(lista_obras,k)
        
        if elemento1["ConstituentID"]=="[" +datos + "]":
            elemento1["ConstituentID"] = nombre
            lt.addLast(lista,elemento1)

    
    print("El autor tiene una cantidad de " + str(lt.size(lista)) + " obras registradas en el museo")

    lista_medios=lt.newList("ARRAY_LIST")
    
    for l in range(lt.size(lista)):
        elemento2=lt.getElement(lista,l)
        

        if lt.isPresent(lista_medios,elemento2["Medium"]) == 0:
            
            lt.addLast(lista_medios,elemento2["Medium"])
    
    print("El autor registró " + str(lt.size(lista_medios)) + " medios diferentes ")
    lista1=lt.newList("ARRAY_LIST")
    diccionario={}
    for a in range(lt.size(lista)):
        elemento3=lt.getElement(lista, a)
        if elemento3["Medium"] not in diccionario.keys():
            diccionario[elemento3["Medium"]]=1
        else:
            diccionario[elemento3["Medium"]]+=1
            

    
    return diccionario




# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento


def OrdenarFechas(artista1,artista2):
    Retorno=True
    if int(artista1["Nacimiento"])<=int(artista2["Nacimiento"]):
        Retorno=True
    else:
        Retorno=False
    return Retorno

def OrdenarFechasObras(obra1,obra2):
    Retorno=True
    if int(obra1["Fecha adquisicion"])<=int(obra2["Fecha adquisicion"]):
        Retorno=True
    else:
        Retorno=False
    return Retorno

