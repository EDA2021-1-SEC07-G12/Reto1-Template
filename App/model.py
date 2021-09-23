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

import pandas as pd
import config as cf
import time
from DISClib.ADT import list as lt
from datetime import date
from tabulate import tabulate

from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from prettytable import PrettyTable
assert cf

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
        if inicio<=int(fecha)<=final:
            diccionario["DisplayName"] = elemento["DisplayName"]
            diccionario["BeginDate"] = elemento["BeginDate"]
            diccionario["ConstituentID"]=elemento["ConstituentID"]
            if elemento["EndDate"]=="0":
                diccionario["EndDate"] = "Unknown"
            else:
                diccionario["EndDate"] = elemento["EndDate"]

            diccionario["Nationality"] = elemento["Nationality"]
            if elemento["Gender"]=="":
               diccionario["Gender"]="Unknown" 
            else:
                diccionario["Gender"]= elemento["Gender"]

            if elemento["ArtistBio"]=="":
                diccionario["ArtistBio"]="Unknown"
            else:
                diccionario["ArtistBio"]=elemento["ArtistBio"]
            
            if elemento["Wiki QID"]=="":
                diccionario["Wiki QID"]="Unknown"
            else:
                diccionario["Wiki QID"]=elemento["Wiki QID"]

            if elemento["ULAN"]=="":
                diccionario["ULAN"]="Unknown"
            else:
                diccionario["ULAN"]=elemento["ULAN"]
            
            
            lt.addLast(lista,diccionario)

    artistasOrdenados= ms.sort(lista,OrdenarFechas)
    primeros3=lt.subList(artistasOrdenados,1,3)
    ultimos3=lt.subList(artistasOrdenados,int(lt.size(artistasOrdenados))-3,3)
    for a in lt.iterator(ultimos3):
        lt.addLast(primeros3,a)
    
    
    return (lt.size(artistasOrdenados),primeros3)
    

def ordenarObras(dia1,mes1,anio1, dia2, mes2,anio2,catalogo):
   
    lista=lt.newList("ARRAY_LIST")
    inicial=date(anio1,mes1,dia1).isoformat()
    final=date(anio2,mes2,dia2).isoformat()
    
    lista_obras=catalogo["lista_obras"]
    for i in lt.iterator(lista_obras):
        if inicial<i["DateAcquired"]<final:
            lt.addLast(lista,i)
    obtenerAutor(lista,catalogo["lista_artistas"])
    
    
    retorno= ms.sort(obtenerAutor(lista,catalogo["lista_artistas"]),ordenarObrasFuncion)

    obrasCompradas(retorno)
    
    
    primeros3=lt.subList(retorno,1,3)
    ultimos3=lt.subList(retorno,int(lt.size(retorno))-3,3)
    for a in lt.iterator(ultimos3):
        lt.addLast(primeros3,a)
    


    return  (lt.size(retorno),lt.size(contarAutores(retorno)) , primeros3, obrasCompradas(retorno))


#Implementado por Juan Andrés Bernal Gil
def clasificar_obras_por_tecnica(nombre,catalogo):
   
    lista_artistas= catalogo["lista_artistas"]
    lista_obras=catalogo["lista_obras"]
    lista_obras_autor=lt.newList("ARRAY_LIST")
    lista_autor=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista_artistas):
       for j in lt.iterator(lista_obras):
           ConstituentID=str(i["ConstituentID"])
           if i["DisplayName"]==nombre and ("[" +ConstituentID + "]" == j["ConstituentID"]):
               lt.addLast(lista_obras_autor,j["Medium"])
               lt.addLast(lista_autor,j)
    
    Contador = contar(lista_obras_autor,eliminarRepetidos(lista_obras_autor))
    ordenado= ms.sort(Contador, ordenarContador)
    ordenado1 = lt.subList(ordenado,1,5)
    medio_mas_usado= lt.getElement(ordenado,1)
    medio_mas_usado= lt.getElement(medio_mas_usado,1)
    ObrasCantidad="El autor tiene una cantidad de " + str(lt.size(lista_obras_autor)) + " obras registradas en el museo"
    Mediosdif='El autor empleó ' + str(lt.size(eliminarRepetidos(lista_obras_autor))) + " Medios diferentes"
    
    tabla=tabulate(imprimir5Elementos(ordenado1), headers=["MediumName","Count"], tablefmt='fancy_grid')

    obras1=lt.newList("ARRAY_LIST")
    for k in lt.iterator(lista_autor):
        if k["Medium"]==medio_mas_usado:
            lt.addLast(obras1,k)
    
    
    return  [obras1,ObrasCantidad,Mediosdif,tabla]
#Implementado por Juan Esteban Lopez
def requerimiento_4_1(catalogo):
    obras=catalogo['lista_obras']
    artistas=catalogo['lista_artistas']
    lista_codigos_a=lt.newList('ARRAY_LIST')
    for k in range(lt.size(artistas)):
        elemento_a=lt.getElement(artistas,k)
        codigo_a=elemento_a['ConstituentID']
        lt.addLast(lista_codigos_a,codigo_a)
    lista_nacionalidad=lt.newList('ARRAY_LIST')  
    for i in range(lt.size(obras)):
        elemento_o=lt.getElement(obras,i)
        codigo_o=elemento_o['ConstituentID']
        codigo_o=codigo_o.replace('[',"")
        codigo_o=codigo_o.replace(']',"")
        posi=lt.isPresent(lista_codigos_a,codigo_o)
        elemento_final=lt.getElement(artistas,posi)
        nacionalidad=elemento_final['Nationality']
        lt.addLast(lista_nacionalidad,nacionalidad)
    nacionalidades_filtradas= eliminarRepetidos(lista_nacionalidad)
    n_contadas=contar(lista_nacionalidad,nacionalidades_filtradas)
    ordenada=ms.sort(n_contadas,OrdenarNacionalidad)
    top_10=lt.subList(ordenada,1,10)
    dict_top_10={}
    lista_paises=lt.newList('ARRAY_LIST')
    for c in top_10['elements']:
        lt.addLast(lista_paises,c['elements'][1])
        if c['elements'][1]=="":
            dict_top_10['Unkown']=c['size']
        else:
            dict_top_10[c['elements'][1]]=c['size']
    respuesta=(dict_top_10,lista_paises)
    return respuesta
def requerimiento_4_2(catalogo,lista_paises):
    pais=lt.getElement(lista_paises,1)
    obras=catalogo['lista_obras']
    artistas=catalogo['lista_artistas']
    lista_codigos_a=lt.newList('ARRAY_LIST')
    for k in range(lt.size(artistas)):
        elemento_a=lt.getElement(artistas,k)
        codigo_a=elemento_a['ConstituentID']
        lt.addLast(lista_codigos_a,codigo_a)
    lista_obras_pais=lt.newList('ARRAY_LIST')
    for i in range(lt.size(obras)):
        elemento_o=lt.getElement(obras,i)
        codigo_o=elemento_o['ConstituentID']
        codigo_o=codigo_o.replace('[',"")
        codigo_o=codigo_o.replace(']',"")
        posi=lt.isPresent(lista_codigos_a,codigo_o)
        elemento_final=lt.getElement(artistas,posi)
        nacionalidad=elemento_final['Nationality']
        resp_obra=lt.newList('ARRAY_LIST')
        lt.addLast(resp_obra,elemento_o['Title'])
        lt.addLast(resp_obra,elemento_final['DisplayName'])
        lt.addLast(resp_obra,elemento_o['Date'])
        lt.addLast(resp_obra,elemento_o['Medium'])
        lt.addLast(resp_obra,elemento_o['Dimensions'])
        if nacionalidad==pais:
            lt.addLast(lista_obras_pais,resp_obra)
    lista_final=lt.newList('ARRAY_LIST')
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,1))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,2))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,3))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,-1))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,-2))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,-3))
    print (lista_final)

    
def requerimiento5(catalogo, departamento):
    lista_obras=catalogo["lista_obras"]
    
    for i in lt.iterator(lista_obras):
        if i["Date"]=="":
            i["Date"]=9999
            #Pusimos este valor debido a que si ponemos 0 o "indefinido", no dejaría llegar a los primeros
        if i["Weight (kg)"]=="":
            i["Weight (kg)"]=0
    lista_artistas=catalogo["lista_artistas"]
    lista_obras_departamento=lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(lista_obras):
        if i["Department"]==departamento:
            lt.addLast(lista_obras_departamento, i)
    CalcularCostos=calcularCostos(lista_obras_departamento)
    ordenado=ms.sort(CalcularCostos,OrdenarCostos)
    
    costoMax=Costomax(ordenado)
    autores=obtenerAutor(ordenado,lista_artistas)
    ObrasMasCostosas=lt.subList(autores,1,5)
    fechas_obras= ms.sort(autores,OrdenarFechasObras1)
    fechas_obras=lt.subList(fechas_obras,1,5)
    peso=Peso(autores)
    #obras_viejas=lt.subList(OrdenarFechasObras1)
   # fechas_obras=lt.subList(fechas_obras,1,5)
   #(costoMax,ObrasMasCostosas, fechas_obras)
    return [costoMax,ObrasMasCostosas,fechas_obras,peso,lt.size(autores) ]

def requerimiento6(catalogo, anio1,anio2, area):
    lista=lt.newList("ARRAY_LIST")
    lista_artistas=catalogo["lista_artistas"]
    lista_obras=catalogo["lista_obras"]
    for i in lt.iterator(lista_obras):

        if i["Date"]=="":
            i["Date"]=0000
        elif anio1<=int(i["Date"])<=anio2:
            lt.addLast(lista,i)
    area1=calcularArea(lista)
    sumatoria=sumatoriaArea(area1,area)
    lista_final=lt.newList('ARRAY_LIST')
    total=lt.subList(sumatoria[1],1,5)
    ultimos3=lt.subList(area1,int(lt.size(area1))-5,5)
    for a in lt.iterator(ultimos3):
        lt.addLast(total,a)
    
    
    return [lt.size(area1), round(sumatoria[0],3), lt.size(sumatoria[1]) , total]
    


# Funciones utilizadas para comparar elementos dentro de una lista
def contarAutores(lista):
    lista1=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        autores=i["Autores"]
        for j in autores:
           
                lt.addLast(lista1,j)

    return lista1
def obtenerFechas(lista):
    lista1=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        
            lt.addLast(lista1, i["DateAcquired"])
    return lista1

def eliminarRepetidos(lista):
    lista1=lt.newList('ARRAY_LIST')
    for i in lt.iterator(lista):
        if lt.isPresent(lista1,i)==0:
            lt.addLast(lista1,i)
    return lista1

def contar(lista1,lista2):
    lista_grande=lt.newList("ARRAY_LIST")
    for a in lt.iterator(lista2):
        lista=lt.newList("ARRAY_LIST")
        for b in lt.iterator(lista1):
            if a==b:
                lt.addLast(lista,a)
        lt.addLast(lista_grande,lista)
    return lista_grande

def calcularCostos(catalogo):
    for i in lt.iterator(catalogo):
       
        if i["Height (cm)"]!= "":

            altura= float(i["Height (cm)"])/100
        elif i["Length (cm)"]!="":
            altura=float(i["Length (cm)"])/100
        else:
            altura=0
        if i["Width (cm)"]!="":

            ancho = float(i["Width (cm)"])/100
        else:
            ancho=0
        
        if i["Depth (cm)"]!="":

            profundidad= float(i["Depth (cm)"])/100
        else:
            profundidad=0
            
        if i["Weight (kg)"]!= "":

            peso=float(i["Weight (kg)"])
        else:
            peso=0
        
        if i["Diameter (cm)"]!="":

            radio = ((float(i["Diameter (cm)"])/2)/100)
        else:
            radio=0

        
        area=altura*ancho*72
        volumen=altura*ancho*profundidad*72
        peso = peso*72
        area_cir=(radio*radio*radio)*4*3.1416/3*72
        lista=[area,volumen,peso,area_cir]
        if max(lista)==0:
            i["Costo"]=48
        else:
            i["Costo"] = max(lista)
    return catalogo

def obtenerAutor(lista,lista_autores):
    for i in  lt.iterator(lista):
        lista1=[]
        lista2=[]
        for j in lt.iterator(lista_autores):
            autor=i["ConstituentID"]
            autor=autor.replace("[","")
            autor=autor.replace("]","")
            autor=autor.split(",")
            
        for k in autor:
            k=k.replace(" ", "")
            lista1.append(k)

        for h in lt.iterator(lista_autores):
            for n in lista1:

                if h["ConstituentID"]==n:
                    lista2.append(h["DisplayName"])
            i["Autores"]=lista2
    return lista
def Costomax(lista):
    costo=0
    for i in lt.iterator(lista):
        costo+=i["Costo"]
    return round(costo,3)

def Peso(lista):
    peso=0
    for i in lt.iterator(lista):
        peso+=int(i["Weight (kg)"])
    return round(peso,2)
def sumatoriaArea(lista,area):
    suma=0
    prueba=0
    lista1=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        if suma+i["Area estimada m^2"]>=area:
            break
        else:
            lt.addLast(lista1,i)
            suma+=i["Area estimada m^2"]
            prueba=suma        
    
    return [suma,lista1]
def obrasCompradas(lista):
    lista1=lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista):
        if i["CreditLine"]=="Purchase":
            lt.addLast(lista1,i)

    return lt.size(lista1)
# Funciones de ordenamiento


def OrdenarFechas(artista1,artista2):
    Retorno=True
    if int(artista1["BeginDate"])<=int(artista2["BeginDate"]):
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

def OrdenarFechasObras1(obra1,obra2):
    Retorno=True
    if int(obra1["Date"])<=int(obra2["Date"]):
        Retorno=True
    else:
        Retorno=False
    return Retorno

def calcularArea(lista):
    for i in lt.iterator(lista):
        if i["Width (cm)"]=="" or i["Height (cm)"]=="":
            area=0
        else:
            Ancho=float(i["Width (cm)"])/100
            Altura=float(i["Height (cm)"])/100
            area=Ancho*Altura

        i["Area estimada m^2"] = round(area,5)

    return lista
def ordenarObrasFuncion(obra1,obra2):
    retorno=None
    if int(obra1["DateAcquired"]<obra2["DateAcquired"]):
        retorno=True
    else:
        Retorno=False
    return retorno

def ordenarContador(objetos1, objetos2):
    retorno=None
    if int(objetos1["size"]>objetos2["size"]):
        retorno=True
    else:
        Retorno=False
    return retorno


def imprimir5Elementos(lista):
    print("Las 5 tecnicas más usadas por el autor fueron: ")
    diccionario={"MediumName" : [], "Count" : []}
    for i in lt.iterator(lista):
        elemento= i["elements"]
        diccionario["MediumName"].append(str(elemento[0]))
        diccionario["Count"].append(str(i["size"])) 
    return diccionario


def OrdenarCostos(obra1,obra2):
    Retorno=True
    
    if float(obra1["Costo"])>int(obra2["Costo"]):
        Retorno=True
    else:
        Retorno=False
    return Retorno
def OrdenarNacionalidad(lista1,lista2):
    Retorno=True
    if int(lista1['size'])>=int(lista2["size"]):
        Retorno=True
    else:
        Retorno=False
    return Retorno

