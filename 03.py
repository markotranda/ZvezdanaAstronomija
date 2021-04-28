import numpy as np
from zvezdanaAstronomija import *
from matplotlib import pyplot as plt


broj, alfa3, alfa2, alfa1, delta3, delta2, delta1, paralaksa = np.loadtxt("arihip.dat", unpack=True, usecols=(0, 1, 2, 3, 4, 5, 6, 14))
alfa = (alfa1/3600 + alfa2/60 + alfa3) * 15
delta = delta1/3600 + delta2/60 + delta3
broj = broj.astype(int)
indeksBoje = np.loadtxt("hipparcos.dat", unpack=True, usecols=(1,))

zvezde = []
for i in range(len(broj)):
    if paralaksa[i] > 5 and -0.35 < indeksBoje[i] < 1.63:
        l, b = ekvatorske2galakticke(alfa[i], delta[i])
        zvezde.append([broj[i], alfa[i], delta[i], l, b])

print(zvezde[0])

