import numpy as np
from zvezdanaAstronomija import *
from matplotlib import pyplot as plt

# Provera f-ja za astro triedar i zadatak za hijade


alfa3, alfa2, alfa1, delta3, delta2, delta1, muAlfa, muDelta, paralaksa, vRad = np.loadtxt("arihip.dat", unpack=True, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 13, 15))

Vx = []
Vy = []
Vz = []

for i in range(len(alfa3)):
    if vRad[i] == 1000 or paralaksa[i] == 0:
        continue
    
    alfa = deg2decDeg(alfa1[i], alfa2[i], alfa3[i])
    delta = deg2decDeg(delta1[i], delta2[i], delta3[i])
    vAlfa = izracunajTangencijalnuBrzinu(muAlfa[i], paralaksa[i])
    vDelta = izracunajTangencijalnuBrzinu(muDelta[i], paralaksa[i])
    alfa = np.deg2rad(alfa)
    delta = np.deg2rad(delta)

    Vx_, Vy_, Vz_ = astroTriedar2ekv(vRad[i], vAlfa, vDelta, alfa, delta)
    Vx.append(Vx_)
    Vy.append(Vy_)
    Vz.append(Vz_)

plt.hist(Vx, bins=1000)
plt.show()
plt.hist(Vy, bins=1000)
plt.show()
plt.hist(Vz, bins=1000)
plt.show()