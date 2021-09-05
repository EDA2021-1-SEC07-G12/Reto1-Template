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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():

    catalogo={"lista obras":None,
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
        print(lt.getElement(lista_artistas,i))

    return 0
    
        
     
    
    


"""   if inicio<int(catalogo["lista_artistas"][i]["BeginDate"])<final:
            diccionario= {}
            diccionario[["lista_artistas"][i]["DisplayName"]]= ["lista_artistas"][i]["BeginDate"]
            lt.addlast(lista,diccionario )"""


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamient