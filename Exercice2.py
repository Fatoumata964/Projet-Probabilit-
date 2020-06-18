# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:33:03 2020

@author: Fatou Badji
"""

# Exercice 2
""" Dans tout mon exercice j'ai pris n = 10 comme exemple pour visualiser mes résultats"""

# 1. Grâce au logiciel Python, on tire des réalisations ty1, . . . , ynu des n variables tY1, . . . , Ynu

from scipy.stats import chi2
def échantillon(n):
    y=[chi2.rvs(2,4) for n in range(n)]
    return y
## Exemple:
print(échantillon(10))

# 2. On calcule une réalisation de la moyenne empirique Y n

def moyenne_empirique(y,n):
    y=[chi2.rvs(2,2) for n in range(n)] ## les (2,2) c'est pour l'esperance et l'ecart-type
    ybar = sum(y, 0.0) / n
    return ybar
## Exemple:
print(" Moyenne empirique: ",moyenne_empirique(échantillon(10),10))
# 3. À partir de la réalisation de la moyenne empirique ¯yn, on calcule une réalisation de cette variable transformée 
from math import sqrt
def transformée(ybar,n):
    zn = sqrt(n)*(ybar-2)/2
    return zn
print("transformée:",transformée(moyenne_empirique(échantillon(10),10),10))    
# 4.  On répéte cette procédure 5 000 fois (étapes 1 à 3)
simul1 = [moyenne_empirique(échantillon(10),10) for i in range(5000)]
simul2 = [échantillon(10) for i in range(5000)]
simul3 = [transformée(moyenne_empirique(échantillon(10),10),10) for i in range(5000)]

# 3.  On construit un histogramme de ces 5 000 réalisations et l’on compare cet histogramme à la densité d’une loi normale centrée réduite N p0, 1q.
# Histogramme des 5000 realisations

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(simul3)

# Histogramme loi normale centrée réduite
import numpy as np

data = np.random.randn(100000)

hx, hy, _ = plt.hist(data, bins=50, density=1,color="lightblue")

plt.ylim(0.0,max(hx)+0.05)
plt.title('Histogramme loi normale centrée réduite')
plt.grid()
plt.show()

""" Les deux histogrammes on la meme allure"""