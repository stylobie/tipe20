#cette version est bugée

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:49:03 2019

@author: serban
"""
import numpy as np
import math
from random import uniform
import matplotlib.pyplot as plt


dt = 0.5
numax = 0.3
vitesse = 1.0
rayon = 2.0
pi = math.pi
tailleEspace = (500,500)


def creeMatrice(n, p):
   return np.zeros((n, p))


def creeArray(n) :
   return np.zeros(n)


def calculDistancePos(p1, p2):
   return calculDistance(p1[0], p1[1], p2[0], p2[1])


def calculDistance(x1, y1, x2, y2) :
   return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))


def quiEstAutour(positions,numeroDePoisson) :
   listeAutour =[]
   for i in range (len(positions)) :
       distance = calculDistancePos(positions[i],positions[numeroDePoisson])
       if distance <= rayon :
           listeAutour += [i]
   return listeAutour


def correctionModulo(x, y) :
    borneX = ((tailleEspace[0])/2) 
    borneY = ((tailleEspace[1])/2)
    for i in range(len(x)) :
        if x[i] > borneX : 
            x[i] = - borneX
        if x[i] < - borneX :
            x[i] = borneX
        if y[i] > borneY : 
            y[i] = -borneY
        if y[i] < - borneY :
            y[i] = borneY
    return (x, y)


def calculerProchainMouv(positions, angles):
    dtpositions = creeMatrice(len(positions),2)
    dtangles = creeArray(len(angles))
    for i in range (len(positions)) :
        anglesProches = []
        listeAutour = quiEstAutour(positions, i)
        for val in listeAutour :
            anglesProches += [angles[val]]
        dtangles[i] = np.mean(anglesProches) + uniform(-numax, numax)
        x = positions[i][0] + vitesse*dt*(math.cos(dtangles[i]))
        y = positions[i][1] + vitesse*dt*(math.sin(dtangles[i]))
        dtpositions = correctionModulo(x, y)
        #dtpositions[i][0] = x
        #dtpositions[i][1] = y
    #dtpositions = correctionModulo(dtpositions[:][0], dtpositions[:][1])
    return (dtpositions,dtangles)

# initialisation

positions_initiales = [
    (0.0,0.0)
    (2.0,8.0),
    (3.0,7.0), (4.0,8.0), (1.0,1.0), (8.0,5.0),
    (6.0,2.0), (5.0,-4.0), (11.0,1.0), (-8.0,5.0), (0.0,5.0),
    ]
angles_initiaux = [
    pi/2,
    pi/4, pi, pi/2, pi/2,
    -pi/4, -pi, -pi/2, -pi/2, -pi/4,
    ]

nombreIterations = 100

positions_as_mat_list = []

# First position

positions = positions_initiales
positions_as_mat = creeMatrice(len(positions), 2)
for i in range(len(positions)):
    positions_as_mat[i] = positions[i]
positions_as_mat_list.append(positions_as_mat)

angles = angles_initiaux
angles_as_array = creeArray(len(angles))
for i in range(len(angles)):
    angles_as_array[i] = angles[i]
current_angles = angles_as_array

for i in range(nombreIterations):
    previous = positions_as_mat_list[i]
    result = calculerProchainMouv(previous, current_angles)
    positions_as_mat_list.append(result[0])
    current_angles = result[1]
    
for i in range(nombreIterations):
    current = positions_as_mat_list[i]
    plt.plot(current[:,0],current[:,1],"o", label="pas de ligne")

plt.show()

  

