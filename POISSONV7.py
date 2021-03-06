#tiers
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:49:50 2020

@author: serban
"""

import numpy as np
import math
from random import uniform
import matplotlib.pyplot as plt
from tkinter import *
import time

"""----------------------------------   VARIABLES   ------------------------------------------"""

dt = 0.5
numaxAngles = 0.2
numaxVitesse = 0.4
vitesse = 1.0
rayon = 1
pi = math.pi
tailleEspace = (200,200)
nombreIterations = 100
nombreDePoisson = 5
pas = 7
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


def correctionModulo(x,abcisseOuOrdonnee):
    borne = ((tailleEspace[abcisseOuOrdonnee]))
    if x > borne : 
        x = 0
    if x < 0 :
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
        dtangles[i] = (np.mean(anglesProches) + uniform(-numaxAngles, numaxAngles))
        vitesseLocale = vitesse + uniform(-numaxVitesse, numaxVitesse)
        x = positions[i][0] + vitesseLocale*dt*(math.cos(dtangles[i]))
        x=correctionModulo(x,0)
        y = positions[i][1] + vitesseLocale*dt*(math.sin(dtangles[i]))
        y=correctionModulo(y,1)
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

def creerPositionsInitiales(nombreDePoissonsInitiaux) :
    global tailleEspace
    positionsInitiales = [0 for i in range(nombreDePoissonsInitiaux)]
    for i in range(len(positionsInitiales)) :
        positionsInitiales[i] = ((uniform(0,tailleEspace[0]),uniform(0,tailleEspace[1])))
    return positionsInitiales
        
def creerAnglesInitiaux(nombreDePoissonsInitiaux) :
    anglesInitiaux = [0 for i in range(nombreDePoissonsInitiaux)]
    for i in range(len(anglesInitiaux)) :
        anglesInitiaux[i] = (uniform(0,2*pi))
    return anglesInitiaux
        

"""----------------------------------   INITIALISATION  ----------------------------------------"""

#positionsInitiales = [(2.0,8.0), (3.0,7.0), (4.0,8.0), (1.0,1.0), (8.0,5.0),(6.0,2.0), (5.0,-4.0), (11.0,1.0), (-8.0,5.0), (0.0,5.0),]
#anglesInitiaux = [pi/2, pi/4, pi, pi/2, pi/2, -pi/4, -pi, -pi/2, -pi/2, -pi/4,]

positionsInitiales = creerPositionsInitiales(nombreDePoisson)
anglesInitiaux = creerAnglesInitiaux(nombreDePoisson)


nombrePoissons = len(positionsInitiales)
positions = np.zeros((nombreIterations,2,nombrePoissons))
angles = np.zeros((nombreIterations,nombrePoissons))
remplirAngles(anglesInitiaux, angles, 0)
remplirPositions(positionsInitiales,positions, 0)

def Initialisation(positions,angles) :
    global nombreIterations
    for i in range(1,nombreIterations) : # i = 1 car on a  deja initialisé en 0
        temporaire = calculerProchainMouv((np.transpose(positions[i-1])), angles[i-1])
        remplirPositions(temporaire[0], positions, i)
        remplirAngles(temporaire[1], angles, i)
        #plt.plot(temporaire[0],temporaire[1],"o")
    return positions, angles

Initialisation(positions,angles)

"""--------Prédateur---------"""

Rvisionpredateur = 100
positionsPredateur=[[0,0]]
anglesPredateur=nombreIterations*[1]
vitessePredateur =1.5*vitesse


def lePlusProche(L,t) :
    d=calculDistance(L[t][0][0],L[t][0][1],positionsPredateur[t][0],positionsPredateur[t][1])
    numero=-1
    print(d)
    for i in range (1,len(L[t][0])) :
        print(i)
        distance = calculDistance(L[t][0][i],L[t][1][i],positionsPredateur[t][0],positionsPredateur[t][1])
        print(distance)
        if distance <= Rvisionpredateur and distance<=d:
            numero=i
            d=distance
            
    return [numero,d]

def addition(liste1,liste2):
    if len(liste1)!=len(liste2):
        return "ERREUR de taille de liste"
    else:
        L=[]
        for i in range(len(liste1)):
            L += [liste1[i]+liste2[i]]
        return L
    
def nouvellePositionPredateur(numero,distance,t):
    x=positionsPredateur[t][0]
    y=positionsPredateur[t][1]
    vecteur=[vitessePredateur*(-x+positions[t][0][i])/distance , vitessePredateur*(-y+positions[t][1][i])/distance]
    return addition(positionsPredateur[t],vecteur)

def afficherPoisson(i,temps) :
    x = positions[t][0][i] + 0.5
    y = positions[t][1][i] + 0.5
    angle = angles[t][i]
    cosAdd = math.cos(angle)/2
    sinAdd = math.sin(angle)/2
    can.create_line(x*pas,y*pas, (x+cosAdd)*pas, (y+sinAdd)*pas, arrow = LAST, tags = "t"+str(temps), fill = 'MediumPurple1')
    for t in range(nombreIterations):
        positionsPredateur+=nouvellePositionPredateur(lePlusProche(positionsPredateur[-1],t)[0],lePlusProche(positionsPredateur[-1],t)[1],t)

def afficherPredateur(temps):
    x = positionsPredateur[t][0] + 0.5
    y = positionsPredateur[t][1] + 0.5
    angle = anglesPredateur[temps]
    cosAdd = math.cos(angle)/2
    sinAdd = math.sin(angle)/2
    can.create_line(x*pas,y*pas, (x+cosAdd)*pas, (y+sinAdd)*pas, arrow = LAST, tags = "t"+str(temps), fill = 'salmon')



#plt.show()
"""print("dt = " + str(dt))
print("numaxAngles = " + str(numaxAngles))
print("numaxVitesse = " + str(numaxVitesse))
print("vitesse = " + str(vitesse))
print("rayon = " + str(rayon))
print("nombreIterations = " + str(nombreIterations))
print("nombrePoissons = " + str(nombrePoissons))
print(positions)
print(angles)"""
"""----------------------------------   TKINTER   ------------------------------------------"""
def afficherPoisson(i,temps) :
    x = positions[t][0][i] + 0.5
    y = positions[t][1][i] + 0.5
    angle = angles[t][i]
    cosAdd = math.cos(angle)/2
    sinAdd = math.sin(angle)/2
    can.create_line(x*pas,y*pas, (x+cosAdd)*pas, (y+sinAdd)*pas, arrow = LAST, tags = "t"+str(temps), fill = 'MediumPurple1')

def supprimerPoissons(temps) :
    can.delete(fenetre,"t"+str(temps))

fenetre = Tk()
fenetre.configure(background ='dark slate gray') 
largeur = tailleEspace[0]*pas
hauteur = tailleEspace[1]*pas
can = Canvas(fenetre, width=largeur, height = hauteur, bg ='azure')
can.pack()

"""for t in range(nombreIterations) :
    for j in range(nombrePoissons) : 
            x = positions[t][0][j]
            y = positions[t][1][j]
            angle = angles[t][j]
            afficherPoisson((x,y), angle)"""            


for t in range(nombreIterations) :
    for i in range(nombrePoissons) :
         afficherPoisson(i,t)
    positionsPredateur+=[nouvellePositionPredateur(lePlusProche(positions,t)[0],lePlusProche(positions,t)[1],t)]
    print(positionsPredateur)
    afficherPredateur(t)
    can.update()
    time.sleep(0.1)
    supprimerPoissons(t)


def mort(i,t):
    if calculDistance(positions[t][0][i],positions[t][1][i],positionPredateur[t][0],positionsPredateur[t][1])<=estomac:
        return True
    else:
        return False



def pointeur(event):
    chaine.configure(text = "("+str(event.y//pas)+" , "+str(event.x//pas)+")")

Button(fenetre, text="Quitter", command=fenetre.quit)    
can.bind("<Button-1>", pointeur)
chaine = Label(fenetre)
chaine.pack()


fenetre.mainloop()
