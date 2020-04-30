# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:32:41 2020

@author: Usuario
"""



class Cubo:
    #cara2 -> frente, cara4 -> atrás, cara5 -> izquierda
    #cara6 -> derecha, cara1 -> superior, cara 3 -> inferior
    #cara1 opuesta a cara3
    #cara2 opuesta a cara4
    #cara5 opuesta a cara6
    def __init__(self,cara1,cara2,cara3,cara4,cara5,cara6,num_cubo):
        self.color1 = cara1
        self.color2 = cara2
        self.color3 = cara3
        self.color4 = cara4
        self.color5 = cara5
        self.color6 = cara6
        self.num_cubo = num_cubo
    def get_colors(self):
        lista_de_colores = [self.color1, self.color2, self.color3, self.color4, self.color5, self.color6]
        return lista_de_colores
    
    def get_cube(self):
        return self.num_cubo

class Vertice:
    def __init__(self, color, grado=0, ady = []):
        self.etiqueta = color
        self.adyacentes = ady
    
    def set_grado(self, new_grado):
        self.grado = new_grado
    
    def set_adyacentes(self, lista_de_vertices):
        self.adyacentes = lista_de_vertices

class Arista:
    def __init__(self, extremo1, extremo2, cubo_asociado=0):
        self.vertice1 = extremo1
        self.vertice2 = extremo2
        self.peso = cubo_asociado

cubo1 = Cubo('Azul', 'Rojo', 'Blanco', 'Blanco', 'Verde', 'Rojo',1)
cubo2 = Cubo('Verde', 'Blanco', 'Rojo', 'Azul', 'Azul', 'Azul',2)
cubo3 = Cubo('Rojo', 'Azul', 'Verde', 'Verde', 'Blanco', 'Blanco',3)
cubo4 = Cubo('Blanco', 'Verde', 'Blanco', 'Rojo', 'Rojo', 'Verde',4)

color_list1 = cubo1.get_colors()
color_list2 = cubo2.get_colors()
color_list3 = cubo3.get_colors()
color_list4 = cubo4.get_colors()

# print(color_list1)

color_list_all = [color_list1,color_list2,color_list3,color_list4]
# print(color_list_all)

#Creacion de adyacencias

adyacenciaFA = {} #Adyacencia de caras Frente/Atras
adyacenciaDI = {} #Adyacencia de caras Derecha/Izquierda
adyacenciaAA = {} #Adyacencia de caras Arriba/Abajo
for cubo in color_list_all:
    #Introduzco en el diccionario las relaciones de adyacencia
    #print(cubo)
    adyacenciaFA[cubo[0]] = cubo[2]
    adyacenciaDI[cubo[1]] = cubo[3]
    adyacenciaAA[cubo[4]] = cubo[5]

#EL INDICE DEL DICCIONARIO CORRESPONDE AL NUMERO DEL CUBO
#por ejemplo, la primera pareja clave-valor de adyacenciaFA se refiere a
#la correspondencia frente/atras del cubo 1

# print(adyacenciaFA)
# print(adyacenciaDI)
# print(adyacenciaAA)

#Creación de vertices

verticeR = Vertice('Rojo')
verticeV = Vertice('Verde')
verticeA = Vertice('Azul')
verticeB = Vertice('Blanco')








        