"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import pandas as pd

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo ")
    print("2- Listar cronologicamente los artistas ")
    print("3- Listar cronologicamenta las adquisiciones ")
    print("4- Clasificar los obras de un artista por técnica ")
    print("5- Clasificar las obras por la nacionalidad de sus creadores ")
    print("6- Transportar obras de un departamento ")
    print("7- Cuantas obras caben en un area")
    print("0- Salir")



catalog= controller.initCatalog()


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
       
        

        
        
        
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        artistas = controller.ultimosArtistas(catalog)
        obras= controller.ultimasObras(catalog)
        print(catalog)
        


        
    elif int(inputs[0]) == 2:
        controlador=controller.organizar_fechas(catalog)
        print("Hubo una cantidad de " + str(controlador[0]) + " Autores en el intervalo ")
        print("Los tres primeros y tres últimos autores del intervalo insertado son " )
        for i in lt.iterator(controlador[1]):

            print(i)
    elif int(inputs[0]) == 3:
        controlador=controller.organizar_obras(catalog)
        print("Hubo una cantidad de " + str(controlador[0])+ " piezas adquiridas en el intervalo insertado" )
        print("Con " + str(controlador[1]) + " artistas y " + str(controlador[3]) + " Obras compradas por el museo")
        print("Las 3 primeras y ultimas obras son ")
        for i in lt.iterator(controlador[2]):
            print({"ObjectID":i["ObjectID"] , "Title":i["Title"]  , "ArtistNames":i["Autores"] , "Medium":i["Medium"] , "Date":i["Date"] , "DateAcquired":i["DateAcquired"], "URL":i["URL"]})
    

    elif int(inputs[0]) == 4:
        controlador=controller.clasificar_obras_por_tecnica(catalog)
        print(controlador[1])
        print(controlador[2])
        print("Las obras con la técnica mas usada por el autor fueron:")
        for i in lt.iterator(controlador[0]):
            print({"Title":i["Title"] , "Date":i["Date"], "Medium" : i["Medium"] , "Dimensions" : i["Dimensions"]})
       # print("Los 5 medios mas usados por el autor fueron ")
       # print(controller.clasificar_obras_por_tecnica(catalog))

        print("Los medio más usados fueron: ")
        print(controlador[3])
    elif int(inputs[0]) == 5:
        print('Las tres primeras y las tres ultimas obras del pais con mas obras son: ')
        respuesta=(controller.clasificar_obras_por_nacionalidad(catalog))
        print ("Este es el top 10 de los paises con más obras")
        for i,j in respuesta[0].items():
            print(i,j)
       
        print(respuesta[1])
            
    elif int(inputs[0]) == 6:

        controlador = controller.requerimiento5(catalog)
        print("El total de obras a transportar es " + str(controlador[4]))
        print("El peso del departamento a transportar es " + str(controlador[3]))
        print("El costo del departamento a transportar es " + str(controlador[0]))
        print("Las obras mas costosas a transportar son: ")
        for i in lt.iterator(controlador[1]):
            print({"Title":i["Title"] , "Artists":i["Autores"]  , "Medium" : i["Medium"] , "Date":i["Date"] ,"Medium" : i["Medium"] , "Dimensions": i["Dimensions"], "Costo" : i["Costo"]})
        print("Las obras mas antiguas a transportar son: ")
        for j in lt.iterator(controlador[2]):
            print({"Title":j["Title"] , "Artists":j["Autores"]  , "Medium" : j["Medium"] , "Date":j["Date"] ,"Medium" : j["Medium"] , "Dimensions": j["Dimensions"], "Costo" : j["Costo"]})
        pass

    elif int(inputs[0]) == 7:
        controlador=controller.requerimiento6(catalog)
        print("Existe una cantidad de " +str(controlador[0]) + " obras dentro del rango de años solicitiado")
        print("La exhibición con más obras tiene " + str(controlador[2]) + " m^2 de uso y se ocupan " + str(controlador[1]) + " m^2")

        for i in lt.iterator(controlador[3]):
            print({"Title":i["Title"] ,"Artists":i["Autores"]  , "Medium" : i["Medium"] , "Date":i["Date"] , "Dimensions": i["Dimensions"]})
    elif int(inputs[0]) == 0:
        pass
    else:
        sys.exit(0)
sys.exit(0)
