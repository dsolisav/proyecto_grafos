# -*- coding: utf-8 -*-


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

def buildAristasFA(lista_adyacenciaFA,verticeR1, verticeB1, verticeV1, verticeA1):
    #Construyo las aristas y sumo los grados a los extremos
    lista_aristasFA = []
    numero_cubo = 1
    for tupla in lista_adyacenciaFA:
        if tupla[0] == 'Rojo' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeR1,verticeR1,numero_cubo)
            verticeR1.sum_grado(2)
            lista_aristasFA.append(NewArista)
        if tupla[0]=='Rojo' and tupla[1] == 'Azul':
            NewArista = Arista(verticeR1,verticeA1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasFA.append(NewArista)
        if tupla[0] == 'Rojo' and tupla[1] == 'Verde':
            NewArista = Arista(verticeR1,verticeV1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Rojo' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeR1,verticeB1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Azul':
            NewArista = Arista(verticeA1,verticeA1,numero_cubo)
            verticeA1.sum_grado(2)
            lista_aristasFA.append(NewArista)

        if tupla[0]=='Azul' and tupla[1] == 'Verde':
            NewArista = Arista(verticeA1,verticeV1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeA1,verticeR1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeA1,verticeB1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Verde':
            NewArista = Arista(verticeV1,verticeV1,numero_cubo)
            verticeV1.sum_grado(2)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Azul':
            NewArista = Arista(verticeV1,verticeA1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeV1,verticeR1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeV1,verticeB1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeB1,verticeB1,numero_cubo)
            verticeB1.sum_grado(2)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Azul':
            NewArista = Arista(verticeB1,verticeA1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Verde':
            NewArista = Arista(verticeB1,verticeV1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeB1,verticeR1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasFA.append(NewArista)

        numero_cubo += 1
    return lista_aristasFA

def buildAristasDI(lista_adyacenciaDI,verticeR1, verticeB1, verticeV1, verticeA1):
    #Construyo las aristas y sumo los grados a los extremos
    lista_aristasDI = []
    numero_cubo = 1
    for tupla in lista_adyacenciaDI:
        if tupla[0] == 'Rojo' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeR1,verticeR1,numero_cubo)
            verticeR1.sum_grado(2)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Rojo' and tupla[1] == 'Azul':
            NewArista = Arista(verticeR1,verticeA1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Rojo' and tupla[1] == 'Verde':
            NewArista = Arista(verticeR1,verticeV1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Rojo' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeR1,verticeB1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Azul':
            NewArista = Arista(verticeA1,verticeA1,numero_cubo)
            verticeA1.sum_grado(2)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Verde':
            NewArista = Arista(verticeA1,verticeV1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeA1,verticeR1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeA1,verticeB1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Verde':
            NewArista = Arista(verticeV1,verticeV1,numero_cubo)
            verticeV1.sum_grado(2)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Azul':
            NewArista = Arista(verticeV1,verticeA1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeV1,verticeR1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeV1,verticeB1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeB1,verticeB1,numero_cubo)
            verticeB1.sum_grado(2)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Azul':
            NewArista = Arista(verticeB1,verticeA1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Verde':
            NewArista = Arista(verticeB1,verticeV1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeB1,verticeR1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasDI.append(NewArista)

        numero_cubo += 1
    return lista_aristasDI

def buildAristasAA(lista_adyacenciaAA, verticeR1, verticeB1, verticeV1, verticeA1):
    #Construyo las aristas y sumo los grados a los extremos
    lista_aristasAA = []
    numero_cubo = 1
    for tupla in lista_adyacenciaAA:
        if tupla[0] == 'Rojo' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeR1,verticeR1,numero_cubo)
            verticeR1.sum_grado(2)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Rojo' and tupla[1] == 'Azul':
            NewArista = Arista(verticeR1,verticeA1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Rojo' and tupla[1] == 'Verde':
            NewArista = Arista(verticeR1,verticeV1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Rojo' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeR1,verticeB1,numero_cubo)
            verticeR1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Azul':
            NewArista = Arista(verticeA1,verticeA1,numero_cubo)
            verticeA1.sum_grado(2)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Verde':
            NewArista = Arista(verticeA1,verticeV1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeA1,verticeR1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Azul' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeA1,verticeB1,numero_cubo)
            verticeA1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Verde':
            NewArista = Arista(verticeV1,verticeV1,numero_cubo)
            verticeV1.sum_grado(2)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Azul':
            NewArista = Arista(verticeV1,verticeA1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeV1,verticeR1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Verde' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeV1,verticeB1,numero_cubo)
            verticeV1.sum_grado(1)
            verticeB1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Blanco':
            NewArista = Arista(verticeB1,verticeB1,numero_cubo)
            verticeB1.sum_grado(2)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Azul':
            NewArista = Arista(verticeB1,verticeA1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeA1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Verde':
            NewArista = Arista(verticeB1,verticeV1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeV1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        if tupla[0] == 'Blanco' and tupla[1] == 'Rojo':
            NewArista = Arista(verticeB1,verticeR1,numero_cubo)
            verticeB1.sum_grado(1)
            verticeR1.sum_grado(1)
            lista_aristasAA.append(NewArista)

        numero_cubo += 1
    return lista_aristasAA

def check_aristas(lista_aristas, lista_adyacencia):
    print(lista_adyacencia)
    for arista in lista_aristas:
        arista.display_arista()

def definirAdyacencias(FrenteAtras_list, DerechaIzquierda_list, ArribaAbajo_list, TodosLosCubos_lista):
    for cubo in TodosLosCubos_lista:
        #Introduzco en la lista de tuplas las relaciones de adyacencia


        FrenteAtras_list.append((cubo[1],cubo[3]))
        DerechaIzquierda_list.append((cubo[4],cubo[5]))
        ArribaAbajo_list.append(((cubo[0],cubo[2])))



def numEdgesFA(AristasFrenteAtras, diccionarioVertices):
    tuple_list = []
    for arista in AristasFrenteAtras:
        edge1 = diccionarioVertices[arista.vertice1.show_color()]
        edge2 = diccionarioVertices[arista.vertice2.show_color()]
        tuple_list.append((edge1, edge2))
    return tuple_list

def numEdgesDI(AristasDerechaIzquierda, diccionarioVertices):
    tuple_list = []
    for arista in AristasDerechaIzquierda:
        edge1 = diccionarioVertices[arista.vertice1.show_color()]
        edge2 = diccionarioVertices[arista.vertice2.show_color()]
        tuple_list.append((edge1, edge2))
    return tuple_list

def numEdgesAA(AristasArribaAbajo, diccionarioVertices):
    tuple_list = []
    for arista in AristasArribaAbajo:
        edge1 = diccionarioVertices[arista.vertice1.show_color()]
        edge2 = diccionarioVertices[arista.vertice2.show_color()]
        tuple_list.append((edge1, edge2))
    return tuple_list

def AllNumericEdges(AristasNumericasFA,AristasNumericasDI,AristasNumericasAA):
    allEdges = []
    for tupla in AristasNumericasFA:
        allEdges.append(tupla)
    for tupla in AristasNumericasDI:
        allEdges.append(tupla)
    for tupla in AristasNumericasAA:
        allEdges.append(tupla)
    return allEdges

def solutionEdges(diccionario_vertices,lista_final):
    lista_solucion_FA = []
    lista_solucion_DI = []
    for diccionario_sol in lista_final:
        lista_solucion_FA.append((diccionario_vertices[diccionario_sol["Frente"]],diccionario_vertices[diccionario_sol["Atras"]]))
        lista_solucion_DI.append((diccionario_vertices[diccionario_sol["Derecha"]],diccionario_vertices[diccionario_sol["Izquierda"]]))
    return lista_solucion_FA, lista_solucion_DI



def inverseFA_str(numericEdges, inverse_dictionary):
    str_tuplesFA = []
    for tupla in numericEdges:
        str_tuplesFA.append((inverse_dictionary[tupla[0]],inverse_dictionary[tupla[1]]))
    return str_tuplesFA

def inverseDI_str(numericEdges, inverse_dictionary):
    str_tuplesDI = []
    for tupla in numericEdges:
        str_tuplesDI.append((inverse_dictionary[tupla[0]],inverse_dictionary[tupla[1]]))
    return str_tuplesDI

def define_solutions(stringFA_list,stringDI_list):
    counter1 = 1
    counter2 = 1
    final_dict_FA = {}
    final_dict_DI = {}
    for tupla in stringFA_list:
        final_dict_FA[tupla] = counter1
        counter1 += 1
    for tupla in stringDI_list:
        final_dict_DI[tupla] = counter2
        counter2 += 1
    return final_dict_FA, final_dict_DI
