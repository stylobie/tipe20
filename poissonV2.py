#version qui marche, il y a seulement un petit souci,
#le prochain mouv renvoie des nan (Not A Number) pour les poissons qui n'intéragissent avec personne. 
#A régler.
import numpy as np
import math
from random import uniform


dt = 1
numax = 0
vitesse = 1
rayon = 2
pi = math.pi


def creeMatrice (n,p) :
    return np.zeros((n,p))


def creeArray (n) :
    return np.zeros(n)


def calculDistancePos(p1, p2): 
    return calculDistance(p1[0], p1[1], p2[0], p2[1])


def calculDistance(x1,y1,x2,y2) :
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))


def quiEstAutour(positions,numeroDePoisson) :
    listeAutour =[]
    for i in range (len(positions)) :
        # on saute le poisson courant
        if i== numeroDePoisson :
            continue
        distance = calculDistancePos(positions[i],positions[numeroDePoisson])
        if distance <= rayon :
            listeAutour += [i]
    return listeAutour


def calculerProchainMouv (positions,angles):
    dtpositions = creeMatrice(len(positions),2)
    dtangles = creeArray(len(angles))
    for i in range (len(positions)) :
        anglesProches = []
        listeAutour = quiEstAutour(positions, i)
        for val in listeAutour : 
            anglesProches += [angles[val]]
        dtangles[i] = np.mean(anglesProches) + uniform(0, numax)
        x = positions[i][0] + vitesse*dt*(math.cos(dtangles[i]))
        y = positions[i][1] + vitesse*dt*(math.sin(dtangles[i]))
        dtpositions[i][0] = x
        dtpositions[i][1] = y
    return (dtpositions,dtangles)


positions_test = [(2,8),(3,7),(4,8),(1,1),(8,5)]
angles_test = [pi/2, pi/4, pi, pi/2, pi/2]

calculerProchainMouv(positions_test, angles_test)

