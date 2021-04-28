import numpy as np
from zvezdanaAstronomija import *
from matplotlib import pyplot as plt

broj, alfa3, alfa2, alfa1, delta3, delta2, delta1, sopstvenoKretanjeAlfa, sopstvenoKretanjeDelta, paralaksa, radijalnaBrzina = np.loadtxt("arihip.dat", unpack=True, usecols=(0, 1, 2, 3, 4, 5, 6,7,8, 13,15))
alfa = (alfa1/3600 + alfa2/60 + alfa3) * 15
delta = delta1/3600 + delta2/60 + delta3
broj = broj.astype(int)
indeksBoje = np.loadtxt("hipparcos.dat", unpack=True, usecols=(1,))

U = []
V = []
W = []

for i in range(len(broj)):   
    if paralaksa[i] > 5 and radijalnaBrzina[i] != 1000 and -0.35 < indeksBoje[i] < 1.63:
        vAlfa = izracunajTangencijalnuBrzinu(sopstvenoKretanjeAlfa[i], paralaksa[i])
        vDelta = izracunajTangencijalnuBrzinu(sopstvenoKretanjeDelta[i], paralaksa[i])
        
        Vx, Vy, Vz = ast2ekv(alfa[i], delta[i], vAlfa, vDelta, radijalnaBrzina[i])
        u, v, w = ekv2gal(Vx, Vy, Vz)
        U.append(u)
        V.append(v)
        W.append(w)
        
plt.hist(U, bins=100)
plt.title('Histogram U')
plt.xlabel('U')
plt.ylabel('Broj zvezda')
plt.show()

plt.hist(V, bins=100)
plt.title('Histogram brzine')
plt.xlabel('Brzina')
plt.ylabel('Broj zvezda')
plt.show()

plt.hist(W, bins=100)
plt.title('Histogram W')
plt.xlabel('W')
plt.ylabel('Broj zvezda')
plt.show()
