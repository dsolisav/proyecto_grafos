# -*- coding: utf-8 -*-
"""

Adaptado de prorum.com
Fuente principal en http://prorum.com/?qa=2605/como-resolver-puzzle-instant-insanity-usando-backtracking

"""

class cube:
    def __init__(self,facelist):
        self.facelist=facelist

    def __getitem__(self,key):
        return self.facelist[key]

    def turn_clockwise(self):
        return cube([self.facelist[1],self.facelist[2],self.facelist[3],self.facelist[0],self.facelist[4],self.facelist[5]])

    def turn_backwards(self):
        return cube([self.facelist[5],self.facelist[1],self.facelist[4],self.facelist[3],self.facelist[0],self.facelist[2]])

    def return_cube(self):
        facedict={}
        facedict['Frente']=self.facelist[0]
        facedict['Derecha']=self.facelist[1]
        facedict['Atras']=self.facelist[2]
        facedict['Izquierda']=self.facelist[3]
        facedict['Arriba']=self.facelist[4]
        facedict['Abajo']=self.facelist[5]
        return facedict

def isLegal(cubes):
    islegal=True
    n=len(cubes)
    for i in range(0,4):
        for j in range(1,n):
            for k in range(0,j):
                if cubes[j][i]==cubes[k][i]:
                    islegal=False
    return islegal

def positions(cube):
    positions=[]
    k=0
    while k<4:
        j=0
        while j<4:
            cube=cube.turn_clockwise()
            positions.append(cube)
            j=j+1
        cube=cube.turn_backwards()
        k=k+1
    cube=cube.turn_clockwise()
    cube=cube.turn_backwards()
    j=0
    while j<4:
        cube=cube.turn_clockwise()
        positions.append(cube)
        j=j+1
    cube=cube.turn_backwards()
    cube=cube.turn_backwards()
    j=0
    while j<4:
        cube=cube.turn_clockwise()
        positions.append(cube)
        j=j+1
    return positions

def getSolution(cubes,lista):
    positions1=positions(cubes[0])
    positions2=positions(cubes[1])
    positions3=positions(cubes[2])
    positions4=positions(cubes[3])
    for i in range(len(positions1)):
        cubes[0]=positions1[i]
        for j in range(len(positions2)):
            cubes[1]=positions2[j]
            for k in range(len(positions3)):
                cubes[2]=positions3[k]
                for l in range(len(positions4)):
                    cubes[3]=positions4[l]
                    if isLegal(cubes):
                        for cube in cubes:
                            # print(cube.return_cube())
                            lista.append(cube.return_cube())
                        break
                if isLegal(cubes):
                    break
            if isLegal(cubes):
                break
        if isLegal(cubes):
            break

def solvePuzzle(cubos,listaSolucion):
    cube1 = cube([cubos[0][1],cubos[0][5],cubos[0][3],cubos[0][4],cubos[0][0],cubos[0][2]])
    cube2 = cube([cubos[1][1],cubos[1][5],cubos[1][3],cubos[1][4],cubos[1][0],cubos[1][2]])
    cube3 = cube([cubos[2][1],cubos[2][5],cubos[2][3],cubos[2][4],cubos[2][0],cubos[2][2]])
    cube4 = cube([cubos[3][1],cubos[3][5],cubos[3][3],cubos[3][4],cubos[3][0],cubos[3][2]])
    final_cubes = [cube1,cube2,cube3,cube4]
    getSolution(final_cubes, listaSolucion)
