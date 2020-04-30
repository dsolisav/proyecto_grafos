# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:14:57 2020

@author: Usuario
"""

class Cubo:
    #cara2 -> frente, cara4 -> atrás, cara5 -> izquierda, cara6 -> derecha, cara1 -> superior
    def __init__(self,cara1,cara2,cara3,cara4,cara5,cara6,num_cubo):
        self.color1 = cara1
        self.color2 = cara2
        self.color3 = cara3
        self.color4 = cara4
        self.color5 = cara5
        self.color6 = cara6

class Vertice:
    def __init__(self, color):
        self.etiqueta = color

class Arista:
    def __init__(self, cubo_asociado):
        self.peso = cubo_asociado