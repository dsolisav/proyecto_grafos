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
    def __init__(self, color, grado=0):
        self.etiqueta = color
        self.grado = grado
    
    def sum_grado(self, new_grado):
        self.grado += new_grado
        
    def get_grado(self):
        return self.grado
    
    def set_adyacentes(self, lista_de_vertices):
        self.adyacentes = lista_de_vertices
        
    def show_color(self):
        return(self.etiqueta)
    

class Arista:
    def __init__(self, extremo1, extremo2, cubo_asociado=0):
        self.vertice1 = extremo1
        self.vertice2 = extremo2
        self.peso = cubo_asociado
    
    def get_extremos(self):
        return (self.vertice1, self.vertice2)
    
    def display_arista(self):
        print(" Extremo 1: ", self.vertice1.show_color(),"\n Extremo 2: ", self.vertice2.show_color(), "\n Cubo asociado: ",self.peso,"\n")

def buildAristasFA(diccionario_adyacenciaFA):
    lista_aristasFA = []
    numero_cubo = 1
    for clave in adyacenciaFA:
        if clave == 'Rojo' and adyacenciaFA[clave] == 'Rojo':
            NewArista = Arista(verticeR,verticeR,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaFA[clave] == 'Azul':
            NewArista = Arista(verticeR,verticeA,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaFA[clave] == 'Verde':
            NewArista = Arista(verticeR,verticeV,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaFA[clave] == 'Blanco':
            NewArista = Arista(verticeR,verticeB,numero_cubo)
            lista_aristasFA.append(NewArista)
        
        if clave == 'Azul' and adyacenciaFA[clave] == 'Azul':
            NewArista = Arista(verticeA,verticeA,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Azul' and adyacenciaFA[clave] == 'Verde':
            NewArista = Arista(verticeA,verticeV,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Azul' and adyacenciaFA[clave] == 'Rojo':
            NewArista = Arista(verticeA,verticeR,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Azul' and adyacenciaFA[clave] == 'Blanco':
            NewArista = Arista(verticeA,verticeB,numero_cubo)
            lista_aristasFA.append(NewArista)
        
        if clave == 'Verde' and adyacenciaFA[clave] == 'Verde':
            NewArista = Arista(verticeV,verticeV,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Verde' and adyacenciaFA[clave] == 'Azul':
            NewArista = Arista(verticeV,verticeA,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Verde' and adyacenciaFA[clave] == 'Rojo':
            NewArista = Arista(verticeV,verticeR,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Verde' and adyacenciaFA[clave] == 'Blanco':
            NewArista = Arista(verticeV,verticeB,numero_cubo)
            lista_aristasFA.append(NewArista)
        
        if clave == 'Blanco' and adyacenciaFA[clave] == 'Blanco':
            NewArista = Arista(verticeB,verticeB,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaFA[clave] == 'Azul':
            NewArista = Arista(verticeB,verticeA,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaFA[clave] == 'Verde':
            NewArista = Arista(verticeB,verticeV,numero_cubo)
            lista_aristasFA.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaFA[clave] == 'Rojo':
            NewArista = Arista(verticeB,verticeR,numero_cubo)
            lista_aristasFA.append(NewArista)
        
        numero_cubo += 1
    return lista_aristasFA

def buildAristasDI(diccionario_adyacenciaDI):
    lista_aristasDI = []
    numero_cubo = 1
    for clave in adyacenciaDI:
        if clave == 'Rojo' and adyacenciaDI[clave] == 'Rojo':
            NewArista = Arista(verticeR,verticeR,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaDI[clave] == 'Azul':
            NewArista = Arista(verticeR,verticeA,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaDI[clave] == 'Verde':
            NewArista = Arista(verticeR,verticeV,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaDI[clave] == 'Blanco':
            NewArista = Arista(verticeR,verticeB,numero_cubo)
            lista_aristasDI.append(NewArista)
        
        if clave == 'Azul' and adyacenciaDI[clave] == 'Azul':
            NewArista = Arista(verticeA,verticeA,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Azul' and adyacenciaDI[clave] == 'Verde':
            NewArista = Arista(verticeA,verticeV,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Azul' and adyacenciaDI[clave] == 'Rojo':
            NewArista = Arista(verticeA,verticeR,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Azul' and adyacenciaDI[clave] == 'Blanco':
            NewArista = Arista(verticeA,verticeB,numero_cubo)
            lista_aristasDI.append(NewArista)
        
        if clave == 'Verde' and adyacenciaDI[clave] == 'Verde':
            NewArista = Arista(verticeV,verticeV,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Verde' and adyacenciaDI[clave] == 'Azul':
            NewArista = Arista(verticeV,verticeA,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Verde' and adyacenciaDI[clave] == 'Rojo':
            NewArista = Arista(verticeV,verticeR,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Verde' and adyacenciaDI[clave] == 'Blanco':
            NewArista = Arista(verticeV,verticeB,numero_cubo)
            lista_aristasDI.append(NewArista)
        
        if clave == 'Blanco' and adyacenciaDI[clave] == 'Blanco':
            NewArista = Arista(verticeB,verticeB,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaDI[clave] == 'Azul':
            NewArista = Arista(verticeB,verticeA,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaDI[clave] == 'Verde':
            NewArista = Arista(verticeB,verticeV,numero_cubo)
            lista_aristasDI.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaDI[clave] == 'Rojo':
            NewArista = Arista(verticeB,verticeR,numero_cubo)
            lista_aristasDI.append(NewArista)
        
        numero_cubo += 1
    return lista_aristasDI

def buildAristasAA(diccionario_adyacenciaAA):
    lista_aristasAA = []
    numero_cubo = 1
    for clave in adyacenciaAA:
        if clave == 'Rojo' and adyacenciaAA[clave] == 'Rojo':
            NewArista = Arista(verticeR,verticeR,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaAA[clave] == 'Azul':
            NewArista = Arista(verticeR,verticeA,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaAA[clave] == 'Verde':
            NewArista = Arista(verticeR,verticeV,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Rojo' and adyacenciaAA[clave] == 'Blanco':
            NewArista = Arista(verticeR,verticeB,numero_cubo)
            lista_aristasAA.append(NewArista)
        
        if clave == 'Azul' and adyacenciaAA[clave] == 'Azul':
            NewArista = Arista(verticeA,verticeA,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Azul' and adyacenciaAA[clave] == 'Verde':
            NewArista = Arista(verticeA,verticeV,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Azul' and adyacenciaAA[clave] == 'Rojo':
            NewArista = Arista(verticeA,verticeR,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Azul' and adyacenciaAA[clave] == 'Blanco':
            NewArista = Arista(verticeA,verticeB,numero_cubo)
            lista_aristasAA.append(NewArista)
        
        if clave == 'Verde' and adyacenciaAA[clave] == 'Verde':
            NewArista = Arista(verticeV,verticeV,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Verde' and adyacenciaAA[clave] == 'Azul':
            NewArista = Arista(verticeV,verticeA,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Verde' and adyacenciaAA[clave] == 'Rojo':
            NewArista = Arista(verticeV,verticeR,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Verde' and adyacenciaAA[clave] == 'Blanco':
            NewArista = Arista(verticeV,verticeB,numero_cubo)
            lista_aristasAA.append(NewArista)
        
        if clave == 'Blanco' and adyacenciaAA[clave] == 'Blanco':
            NewArista = Arista(verticeB,verticeB,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaAA[clave] == 'Azul':
            NewArista = Arista(verticeB,verticeA,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaAA[clave] == 'Verde':
            NewArista = Arista(verticeB,verticeV,numero_cubo)
            lista_aristasAA.append(NewArista)
            
        if clave == 'Blanco' and adyacenciaAA[clave] == 'Rojo':
            NewArista = Arista(verticeB,verticeR,numero_cubo)
            lista_aristasAA.append(NewArista)
        
        numero_cubo += 1
    return lista_aristasAA

def check_aristas(lista_aristas, diccionario_adyacencia):
    print(diccionario_adyacencia)
    for arista in lista_aristas:
        arista.display_arista()
        


#---------------------------BEGIN_OF_EXECUTION---------------------------------
    
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
    

#Creacion de vertices

verticeR = Vertice('Rojo')
verticeV = Vertice('Verde')
verticeA = Vertice('Azul')
verticeB = Vertice('Blanco')


#Creacion de aristas
    
lista_aristas_FA = buildAristasFA(adyacenciaFA)
lista_aristas_DI = buildAristasDI(adyacenciaDI)
lista_aristas_AA = buildAristasAA(adyacenciaAA)

#----------------Comprobar dicconarios de adyacencia y aristas-----------------

# check_aristas(lista_aristas_FA, adyacenciaFA)
# check_aristas(lista_aristas_DI, adyacenciaDI)
# check_aristas(lista_aristas_AA, adyacenciaAA)

#------------------------------------------------------------------------------


    











        