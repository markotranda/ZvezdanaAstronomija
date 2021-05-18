import numpy as np
from zvezdanaAstronomija import *
from matplotlib import pyplot as plt

# alfa[h], alfa[m], alfa[s], delta[s], delta[m], delta[s], mV, B-V, mua[mas], mud[mas]
alfa1, alfa2, alfa3, delta1, delta2, delta3, muAlfa, muDelta = np.loadtxt("Hyades_50.txt", skiprows=4, unpack= True, usecols=(0,1,2,3,4,5,8,9)) 

alfa = []
delta = []
for i in range(len(alfa1)):
    alfa_ = deg2decDeg(alfa1[i], alfa2[i], alfa3[i])
    delta_ = deg2decDeg(delta1[i], delta2[i], delta3[i])
    alfa.append(alfa_)
    delta.append(delta_)
# print(alfa)
alfa = np.deg2rad(alfa)
delta = np.deg2rad(delta)

a = muAlfa*np.cos(alfa)*np.sin(delta)*np.cos(delta) - muDelta*np.sin(alfa)
b = muAlfa*np.sin(alfa)*np.sin(delta)*np.cos(delta) + muDelta*np.cos(alfa)
c = muAlfa*(np.cos(delta))**2

A2 = np.sum(a**2)
B2 = np.sum(b**2)
AB = np.sum(a*b)
AC = np.sum(a*c)
BC = np.sum(b*c)

Y = (AC*BC - AB*AC) / (A2*B2 - AB**2)
X = (AC - AB) / A2 

alfaRadijenta = np.arctan2(Y,X)
deltaRadijenta = np.arctan(1 / (np.sqrt(X**2 + Y**2)))

print(np.rad2deg(alfaRadijenta), np.rad2deg(deltaRadijenta))