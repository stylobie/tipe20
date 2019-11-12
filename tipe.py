import numpy as np



def initialisationPositions(nombreDePoissons,temps):
  positionsPourTous=np.zeros((nombreDePoissons,3,temps))
  for i in range(nombreDePoissons) :
    for j in range(3) :
      positionsPourTous[i][j][0] = int(input("coordonnée du " + str(i+1) +" ème poisson\n"))
  print(positionsPourTous)

def intialisationForces(nombreDePoissons) :
  forceAttraction = np.zeros((3,nombreDePoissons))
  forceRepulsion = np.zeros((3,nombreDePoissons))
  
def initialisationDesVitesses(nombreDePoissons):
  vitesses = np.zeros((3,nombreDePoissons))
  for j in range(nombreDePoissons) :
    for i in range(3) :
      vitesses[i][j] = int(input(" coordonée de la vitesse initiale du " + str(j+1) +" ème poisson\n"))
   print(vitesses)
  
def somme(liste):
  s=0
  for val in :
  s=s+val
  return s

def coordonneeBarycentre(liste):
  return somme(liste)/len(liste)

def barycentre(nombreDePoissons,instant):
  bary=[]
  coordonnees=[0,1,2]
  for coordonnee in coordonnees:
      listeDeCoordonnee=[]
      for i in range(nombreDePoissons):
        listeDeCoordonnee+=Positions[i][coordonnee][instant]
      bary+=coordoneeBarycentre(listeDeCoordonnee)
  return bary

def initialisationDistance(nombreDePoissons):
matriceDistance=np.zeros((3,nombreDePoissons))
for i in range(3):
for j in range(nombreDePoissons):
matriceDistance[i][j]=barycentre(nombreDePoissons,0)-initialisationPositions[j]:,0][i]
return matriceDistance
