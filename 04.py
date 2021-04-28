from matplotlib import pyplot as plt 
from zvezdanaAstronomija import *
import numpy as np

alfa1, alfa2, alfa3, delta1, delta2, delta3 = np.loadtxt('O-zvezde.txt', unpack= True)

alfa = []
delta = []
for i in range(len(alfa1)):    
    alfa.append(deg2decDeg(alfa1[i], alfa2[i], alfa3[i]) * 15)
    delta.append(deg2decDeg(delta1[i], delta2[i], delta3[i]))

alfa_ = np.deg2rad(alfa)
delta_ = np.deg2rad(delta)

yi = np.tan(delta_)
ys = np.sum(yi * np.sin(alfa_))
yc = np.sum(yi * np.cos(alfa_))
s2 = np.sum(np.sin(alfa_)**2)
c2 = np.sum(np.cos(alfa_)**2)
sc = np.sum(np.sin(alfa_) * np.cos(alfa)) 

A1 = (yc*sc - ys*c2)/(sc**2 - s2*c2)    
A2 = (yc*s2 - ys*sc)/(sc**2 - s2*c2)

inklinacija = izracunajInklinaciju(A1, A2)
longitudaUzlaznogCvora = izracunajLongituduUzlaznogCvora(A1, A2)
delta_novo = jnaGalEkv(inklinacija, alfa_, longitudaUzlaznogCvora)

inklinacija = np.rad2deg(inklinacija)
longitudaUzlaznogCvora = np.rad2deg(longitudaUzlaznogCvora)
print(inklinacija, longitudaUzlaznogCvora)

delta_novo = np.rad2deg(delta_novo)
alfa_novo = alfa
alfa, delta_novo = zip(*sorted(zip(alfa, delta_novo)))

plt.plot(alfa , delta_novo, 'r')
plt.scatter(alfa_novo, delta) 
plt.xlabel('Alfa')
plt.ylabel('Delta')  
plt.grid()
plt.show()
