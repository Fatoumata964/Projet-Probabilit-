# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:33:29 2020

@author: Fatou Badji
"""

## Exercice 1:

## 1. Grâce au logiciel Python, on tire des réalisations ty1, ..., ynu des n variables tY1,    , Ynu.

from scipy.stats import uniform
def échantillon(n):
    y= [uniform.rvs(5,2.8) for n in range(n)] ##les (5,2.8) c'est pour l'esperance et l'ecart-type
    return y
## Exemple:
print(échantillon(10))
## 2. On calcule une réalisation de la moyenne empirique Y n
def moyenne_empirique(y,n):
    y=[uniform.rvs(5,8.4) for n in range(n)]
    ybar = sum(y) / n
    return ybar
## Exemple:
print(" Moyenne empirique: ",moyenne_empirique(échantillon(10),10))
## 3. On répète 5 000 fois les étapes 1 et 2. On obtient ainsi 5 000 réalisations 

simul1 = [moyenne_empirique(échantillon(10),10) for i in range(5000)]
simul2 = [échantillon(10) for i in range(5000)]
 
## 4. On construit l’histogramme de ces 5 000 réalisations.
import seaborn as sns

sns.distplot(simul1)
print('/n')
## 5. On répète l’expérience pour différentes valeurs de la dimension n (taille d’échantillon). 
## Tracer les histogrammes des 10000 réalisations ¯yn obtenues pour quatre valeurs de n.
# n = 10, n = 100, n = 1000 et n = 10000
simul3 = [moyenne_empirique(échantillon(10),10) for i in range(1000)]
simul4 = [moyenne_empirique(échantillon(100),100) for i in range(1000)]
simul5 = [moyenne_empirique(échantillon(1000),1000) for i in range(1000)]
simul6 = [moyenne_empirique(échantillon(10000),10000) for i in range(1000)]
sns.distplot(simul3)
sns.distplot(simul4)
sns.distplot(simul5)
sns.distplot(simul6)