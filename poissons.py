import numpy as np
import math

dt = 0,1
nu = 0,2
vitesse = 2
rayon = 2
npoissons = 10

def creeMatrice (n) :
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
    dtpositions = creeMatrice(len(positions))
    dtangles = creeMatrice(len(angles))
    for i in range (len(positions)) :
        anglesProches = []
        listeAutour = quiEstAutour(positions, i)
        anglesProches += angles[listeAutour[i]]
        dtangles[i] += np.mean(anglesProches) + nu
        x = positions[i][0] + vitesse*dt*(math.cos(dtangles[i][0]))
        y = positions[i][1] + vitesse*dt*(math.sin(dtangles[i][1]))
        dtpositions[i] += (x, y)
    return (dtpositions,dtangles)