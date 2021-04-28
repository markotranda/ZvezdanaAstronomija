import numpy as np
from zvezdanaAstronomija import *
from matplotlib import pyplot as plt

# 0,    13, 16
# broj, Pi, m

apsolutnaMagnitudaSunca = 4.8

broj, paralaksa, prividnaMagnituda = np.loadtxt("arihip.dat", unpack=True, usecols=(0, 13, 16))
broj = broj.astype(int)
indeksBoje = np.loadtxt("hipparcos.dat", unpack=True, usecols=(1,))

Teff, _, B_V = np.loadtxt("Spektralni_tipovi.dat", skiprows=1, unpack=True)

zvezde = []
for i in range(len(broj)):
    if paralaksa[i] > 5 and -0.35 < indeksBoje[i] < 1.63:
        apsolutnaMagnituda = izracunajApsolutnuMagnitudu(prividnaMagnituda[i], paralaksa[i])
        TeffZvezde = np.interp(indeksBoje[i], B_V, Teff)
        zvezde.append([broj[i], apsolutnaMagnituda, indeksBoje[i], izracunajLuminoznost(apsolutnaMagnituda), TeffZvezde])

# print([row[0] for row in zvezde])

plt.scatter([row[2] for row in zvezde], [row[1] for row in zvezde], s=0.1)
plt.gca().invert_yaxis()
plt.xlabel("B-V")
plt.ylabel("Apsolutna Magnituda")
plt.show()

plt.scatter([row[4] for row in zvezde], [row[3] for row in zvezde], s=0.5)
plt.xlabel("Temperatura")
plt.ylabel("Luminoznost")
plt.show()

