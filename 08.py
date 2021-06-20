import numpy as np
from zvezdanaAstronomija import *
from matplotlib import pyplot as plt

broj, alfa1, alfa2, alfa3, delta1, delta2, delta3, muAlfa, muDelta, _, _, _, _, paralaksa, _, radijalnaBrzina, _, _, _, _ = np.loadtxt('arihip.dat', unpack=True)

sopstvenoKretanje = izracunajSopstvenoKretanje(muAlfa, muDelta)

alfa = []
delta = []
for i in range(len(broj)):
    alfa.append(deg2decDeg(alfa1[i], alfa2[i], alfa3[i]) * 15)
    delta.append(deg2decDeg(delta1[i], delta2[i], delta3[i]))
    

tangencijalnaBrzina = izracunajTangencijalnuBrzinu(sopstvenoKretanje, paralaksa)

ugaoBrzine = tangencijalnaBrzina / radijalnaBrzina

rastojanjeJata = izracunajRastojanjeJata(radijalnaBrzina, sopstvenoKretanje, ugaoBrzine)
print(rastojanjeJata)
