# -*- coding: utf-8 -*-

import core as cr
import igraph as ig
import solver as final

#-------------------------BEGINNING_OF_EXECUTION-------------------------------

#-------------------------CREACION GRAFO GENERAL-------------------------------

#cubo1 = cr.Cubo('Azul', 'Rojo', 'Blanco', 'Blanco', 'Verde', 'Rojo',1)
#cubo2 = cr.Cubo('Verde', 'Blanco', 'Rojo', 'Azul', 'Azul', 'Azul',2)
#cubo3 = cr.Cubo('Rojo', 'Azul', 'Verde', 'Verde', 'Blanco', 'Blanco',3)
#cubo4 = cr.Cubo('Blanco', 'Verde', 'Blanco', 'Rojo', 'Rojo', 'Verde',4)

cubo1 = cr.Cubo('Rojo', 'Verde', 'Blanco', 'Rojo', 'Azul', 'Verde',1)
cubo2 = cr.Cubo('Rojo', 'Rojo', 'Azul', 'Rojo', 'Verde', 'Azul',2)
cubo3 = cr.Cubo('Blanco', 'Blanco', 'Verde', 'Blanco', 'Rojo', 'Azul',3)
cubo4 = cr.Cubo('Rojo', 'Blanco', 'Blanco', 'Azul', 'Blanco', 'Verde',4)

#cubo1 = cr.Cubo('Rojo', 'Blanco', 'Azul', 'Azul', 'Rojo', 'Blanco',1)
#cubo2 = cr.Cubo('Rojo', 'Blanco', 'Verde', 'Verde', 'Verde', 'Azul',2)
#cubo3 = cr.Cubo('Rojo', 'Blanco', 'Blanco', 'Blanco', 'Rojo', 'Verde',3)
#cubo4 = cr.Cubo('Rojo', 'Blanco', 'Azul', 'Azul', 'Verde', 'Azul',4)

#cubo1 = cr.Cubo('Rojo', 'Rojo', 'Azul', 'Blanco', 'Blanco', 'Azul',1)
#cubo2 = cr.Cubo('Azul', 'Verde', 'Azul', 'Azul', 'Rojo', 'Blanco',2)
#cubo3 = cr.Cubo('Rojo', 'Rojo', 'Azul', 'Blanco', 'Blanco', 'Verde',3)
#cubo4 = cr.Cubo('Rojo', 'Blanco', 'Verde', 'Verde', 'Verde', 'Azul',4)

#cubo1 = cr.Cubo('Blanco', 'Azul', 'Verde', 'Azul', 'Blanco', 'Rojo',1)
#cubo2 = cr.Cubo('Rojo', 'Rojo', 'Blanco', 'Azul', 'Blanco', 'Verde',2)
#cubo3 = cr.Cubo('Verde', 'Azul', 'Blanco', 'Verde', 'Blanco', 'Blanco',3)
#cubo4 = cr.Cubo('Rojo', 'Azul', 'Verde', 'Verde', 'Verde', 'Blanco',4)

#cubo1 = cr.Cubo('Rojo', 'Azul', 'Rojo', 'Azul', 'Blanco', 'Verde',1)
#cubo2 = cr.Cubo('Rojo', 'Azul', 'Rojo', 'Azul', 'Blanco', 'Verde',2)
#cubo3 = cr.Cubo('Rojo', 'Azul', 'Rojo', 'Azul', 'Blanco', 'Verde',3)
#cubo4 = cr.Cubo('Blanco', 'Verde', 'Blanco', 'Rojo', 'Verde', 'Azul',4)


color_list1 = cubo1.get_colors()
color_list2 = cubo2.get_colors()
color_list3 = cubo3.get_colors()
color_list4 = cubo4.get_colors()

# print(color_list1)
# print(color_list2)
# print(color_list3)
# print(color_list4)


color_list_all = [color_list1,color_list2,color_list3,color_list4]
# print(color_list_all)

#Creacion de adyacencias


adyacenciaFA = []
adyacenciaDI = []
adyacenciaAA = []

cr.definirAdyacencias(adyacenciaFA, adyacenciaDI, adyacenciaAA, color_list_all)


#Creacion de vertices

verticeR = cr.Vertice('Rojo')
verticeV = cr.Vertice('Verde')
verticeA = cr.Vertice('Azul')
verticeB = cr.Vertice('Blanco')

verticeR_2 = cr.Vertice('Rojo')
verticeV_2 = cr.Vertice('Verde')
verticeA_2 = cr.Vertice('Azul')
verticeB_2 = cr.Vertice('Blanco')

verticeR_3 = cr.Vertice('Rojo')
verticeV_3 = cr.Vertice('Verde')
verticeA_3 = cr.Vertice('Azul')
verticeB_3 = cr.Vertice('Blanco')

#Creacion de aristas

lista_aristas_FA = cr.buildAristasFA(adyacenciaFA,verticeR, verticeB, verticeV, verticeA)
lista_aristas_DI = cr.buildAristasDI(adyacenciaDI,verticeR, verticeB, verticeV, verticeA)
lista_aristas_AA = cr.buildAristasAA(adyacenciaAA,verticeR, verticeB, verticeV, verticeA)

#----------------Comprobar aristas y diccionarios de adyacencia-----------------

cr.check_aristas(lista_aristas_FA, adyacenciaFA)
cr.check_aristas(lista_aristas_DI, adyacenciaDI)
cr.check_aristas(lista_aristas_AA, adyacenciaAA)

#-------------------Comprobar grados de los vertices---------------------------

# print(verticeR.get_grado())
# print(verticeB.get_grado())
# print(verticeA.get_grado())
# print(verticeV.get_grado())

#-------------------------------------------------------------------------------

lista_solucion_final = []
vertex_dict = {'Rojo':0,'Azul':1,'Verde':2,'Blanco':3}
inverse_dict = {0:'Rojo',1:'Azul',2:'Verde',3:'Blanco'}

numAristasFA = cr.numEdgesFA(lista_aristas_FA, vertex_dict)
numAristasDI = cr.numEdgesDI(lista_aristas_DI, vertex_dict)
numAristasAA = cr.numEdgesAA(lista_aristas_AA, vertex_dict)

#-------------------------------------------------------------------------------

# print(cr.numEdgesFA(lista_aristas_FA, vertex_dict)) #Aristas numericas Frente/Atras
# print(cr.numEdgesDI(lista_aristas_DI, vertex_dict)) #Aristas numericas Derecha/Izquierda
# print(cr.numEdgesAA(lista_aristas_AA, vertex_dict)) ##Aristas numericas Arriba/Abajo

#-------------------------------------------------------------------------------


allNumericEdges_list = cr.AllNumericEdges(numAristasFA,numAristasDI,numAristasAA)
#print(allNumericEdges_list) #Lista con todas las aristas para graficar el grafo general


#------------------GENERAL GRAPH PLOT-------------------------------------------
generalWeight = [1,2,3,4,1,2,3,4,1,2,3,4]

generalGraph = ig.Graph()
generalGraph.add_vertices(4)
generalGraph.add_edges(allNumericEdges_list)
#generalGraph.es["pesos"] = generalWeight
#generalGraph.es["label"] = generalGraph.es["pesos"]
visualstyle0 = {}
visualstyle0["vertex_size"] = 50
visualstyle0["margin"] = 100
visualstyle0["bbox"] = (500,500)
visualstyle0["vertex_color"] = ['red','blue','green','white']
layout = generalGraph.layout_kamada_kawai()
ig.plot(generalGraph, layout = layout,**visualstyle0)
#-------------------------------------------------------------------------------

final.solvePuzzle(color_list_all,lista_solucion_final)
#print(lista_solucion_final) #Diccionarios con la solucion de los cubos

numericSolutionFA, numericSolutionDI = cr.solutionEdges(vertex_dict, lista_solucion_final)
if (len(numericSolutionFA) != 4 and len(numericSolutionFA) != 4):
    raise ValueError('¡El problema no tiene solucion!')

#----------------ESTAS SON LAS ARISTAS QUE HAY QUE GRAFICAR---------------------

print(numericSolutionFA) #Aristas con la orientacion Frente/Atras de la solucion
print(numericSolutionDI) #Aristas con la orientacion Derecha/Izquierda de la solucion

#-------------------------------------------------------------------------------


stringFA = cr.inverseFA_str(numericSolutionFA,inverse_dict)
stringDI = cr.inverseFA_str(numericSolutionDI,inverse_dict)

finalDictFA, finalDictDI = cr.define_solutions(stringFA, stringDI)

#-------------------------------------------------------------------------------
print(finalDictFA)
print(finalDictDI)
#-------------------------------------------------------------------------------


#-------------------------PLOT DE GRAFOS SOLUCION-------------------------------

we = [1,2,3,4]

solution1 = ig.Graph()
solution1.add_vertices(4)
solution1.add_edges(numericSolutionFA)
solution1.es["pesos"] = we
solution1.es["label"] = solution1.es["pesos"]
visualstyle1 = {}
visualstyle1["vertex_size"] = 50
visualstyle1["margin"] = 100
visualstyle1["bbox"] = (500,500)
visualstyle1["vertex_color"] = ['red','blue','green','white']
layout = solution1.layout_kamada_kawai()
ig.plot(solution1, layout = layout,**visualstyle1)



solution2 = ig.Graph()
solution2.add_vertices(4)
solution2.add_edges(numericSolutionDI)
solution2.es["pesos"] = we
solution2.es["label"] = solution2.es["pesos"]
visualstyle2 = {}
visualstyle2["vertex_size"] = 50
visualstyle2["margin"] = 100
visualstyle2["bbox"] = (500,500)
visualstyle2["vertex_color"] = ['red','blue','green','white']
layout = solution2.layout_kamada_kawai()
ig.plot(solution2, layout = layout,**visualstyle2)


#-------------------------------------------------------------------------------
# lista_solucion_f.clear()
