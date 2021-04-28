"""
Created on Mon Apr  5 12:29:23 2021

Name: Domaci2

@author: marija
"""

import numpy as np
from zvezdanaAstronomija import *
from matplotlib import pyplot as plt

# 8       , 9       , 13, 16
# mi-alfa*, mi-delta, Pi, Vrad

broj, sopstvenoKretanjeAlfa, sopstvenoKretanjeDelta, paralaksa, radijalnaBrzina = np.loadtxt("arihip.dat", unpack=True, usecols=(0, 7, 8, 13, 15))
broj = broj.astype(int)
indeksBoje = np.loadtxt("hipparcos.dat", unpack=True, usecols=(1,))

zvezde = []
for i in range(len(broj)):
    if paralaksa[i] > 5 and -0.35 < indeksBoje[i] < 1.63:
        sopstvenoKretanje = izracunajIntenzitet(sopstvenoKretanjeAlfa[i], sopstvenoKretanjeDelta[i])
        tangencijalnaBrzina = izracunajTangencijalnuBrzinu(sopstvenoKretanje, paralaksa[i])
        brzina = izracunajBrzinu(tangencijalnaBrzina, radijalnaBrzina[i])
        zvezde.append([broj[i], brzina])
        
# print([row[1] for row in zvezde])

plt.xlabel('Brzina [km/s]')
plt.ylabel('Broj zvezdi')
plt.title('Histogram brzine')
plt.hist([row[1] for row in zvezde], rwidth=0.95, color='orange')
plt.show()

# plt.hist([row[0] for row in zvezde], bins= [1000, 35000, 60000, 120000],  rwidth = 0.95) # primer sa opsegom 
