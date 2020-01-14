import numpy as np
import math
from random import uniform
import matplotlib.pyplot as plt
from tkinter import *


"""----------------------------------   VARIABLES   ------------------------------------------"""

dt = 0.5
numax = 0.3
vitesse = 2.0
rayon = 2.0
pi = math.pi
tailleEspace = (500,500)
nombreIterations = 3


"""----------------------------------   FONCTIONS   ------------------------------------------"""
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


def correctionModulo(x) :
    borne = ((tailleEspace[0])/2)
    if x > borne : 
        x = - borne
    if x < - borne :
        x = borne
    return x


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
        x=correctionModulo(x)
        y = positions[i][1] + vitesse*dt*(math.sin(dtangles[i]))
        y=correctionModulo(y)
        dtpositions[i][0] = x
        dtpositions[i][1] = y
    return (dtpositions,dtangles)

def remplirPositions(ipositions,positions, i) :
    s=0
    for coord in ipositions :
        positions[i][0][s] = coord[0]
        positions[i][1][s] = coord[1]
        s+=1
    return positions

def remplirAngles(iangles,angles,i):
    s=0
    for angle in iangles :
        angles[i][s]= angle
        s+=1
    return angles

def convertitMatriceEnTupleListe(matrice) : #marche que pr matrice 2 lignes
    ListeDeTuples = []
    nombreColonnes = len(matrice[0])
    for i in range(nombreColonnes) :
        ListeDeTuples.append((matrice[0][i],matrice[1][i]))
    return ListeDeTuples

 

"""----------------------------------   INITIALISATION  ------------------------------------------"""

positionsInitiales = [
    (2.0,8.0),
    (3.0,7.0), (4.0,8.0), (1.0,1.0), (8.0,5.0),
    (6.0,2.0), (5.0,-4.0), (11.0,1.0), (-8.0,5.0), (0.0,5.0),
    ]
anglesInitiaux = [
    pi/2,
    pi/4, pi, pi/2, pi/2,
    -pi/4, -pi, -pi/2, -pi/2, -pi/4,
    ]

nombrePoissons = len(positionsInitiales)
positions = np.zeros((nombreIterations,2,nombrePoissons))
angles = np.zeros((nombreIterations,nombrePoissons))
remplirAngles(anglesInitiaux, angles, 0)
remplirPositions(positionsInitiales,positions, 0)

def Initialisation(positions,angles) :
    global nombreIterations
    for i in range(1,nombreIterations) : #-1 car on a  deja initialisé en 0
        temporaire = calculerProchainMouv(convertitMatriceEnTupleListe(positions[i]),angles[i])
        remplirPositions(temporaire[0], positions, i)
        remplirAngles(temporaire[1], angles, i)
    return positions, angles



"""----------------------------------   TKINTER   ------------------------------------------"""

fenetre = Tk()
largeur = tailleEspace[0]
hauteur = tailleEspace[1]
can = Canvas(fenetre, width=largeur, height = hauteur)
can.pack()

#fenetre.mainloop()


