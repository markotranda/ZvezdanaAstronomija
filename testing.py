from zvezdanaAstronomija import *

vR, vAlfa, vDelta, alfa, delta = 0.2, 1, 0.6, 0.3, 0.3
print("vR, vAlfa, vDelta", vR, vAlfa, vDelta)

Vx, Vy, Vz = astroTriedar2ekv(vR, vAlfa, vDelta, alfa, delta)
print("Vx, Vy, Vz", Vx, Vy, Vz)

vR, vAlfa, vDelta = ekv2astroTriedar(Vx, Vy, Vz, alfa, delta)
print("vR, vAlfa, vDelta", vR, vAlfa, vDelta)
