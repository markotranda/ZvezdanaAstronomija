import numpy as np

# konstante
apsolutnaMagnitudaSunca = 4.8
k = 4.738
# galakticke koordinate
alfaG = 192.25  # deg (12 + 49/60)*15
deltaG = 27.4  # deg
tetaG = 123  # deg
# jos konstanti
alfaOm = np.deg2rad(282.86)
inklinacija = np.deg2rad(62.87)
lOm = np.deg2rad(32.93)


def izracunajApsolutnuMagnitudu(prividnaMagnituda, paralaksa):
    apsolutnaMagnituda = prividnaMagnituda + 5 + 5*np.log10(paralaksa/1000)
    return apsolutnaMagnituda

def izracunajLuminoznost(apsolutnaMagnituda):
    _apsolutnaMagnitudaSunca = apsolutnaMagnitudaSunca
    luminoznost = 10**((_apsolutnaMagnitudaSunca - apsolutnaMagnituda)/2.5)
    return luminoznost


###

def izracunajSopstvenoKretanje(sopstvenoKretanjeAlfa_, sopstvenoKretanjeDelta):
    sopstvenoKretanje= np.sqrt(sopstvenoKretanjeAlfa_**2 + sopstvenoKretanjeDelta**2)
    return sopstvenoKretanje

def izracunajTangencijalnuBrzinu(sopstvenoKretanje, paralaksa):
    Vtan = k*sopstvenoKretanje/paralaksa    
    return Vtan

def izracunajBrzinu(tangencijalnaBrzina, radijalnaBrzina):
    brzina = np.sqrt(tangencijalnaBrzina**2 + radijalnaBrzina**2)
    return brzina

def izracunajIntenzitet(a, b):
    return np.sqrt(a**2 + b**2)

def ekvatorske2galakticke(alfa, delta):
    b = np.arcsin(np.sin(delta)*np.sin(deltaG) + np.cos(delta)*np.cos(deltaG)*np.cos(alfa-alfaG))
    l = tetaG - np.arctan2(np.cos(delta)*np.sin(alfa-alfaG), np.sin(tetaG)*np.cos(deltaG) - np.cos(delta)*np.sin(deltaG)*np.cos(alfa-alfaG))
    return l, b

###


def ast2ekv(alfa, delta, vAlfa, vDelta, vRad):
    A = [[np.cos(alfa)*np.cos(delta), -np.sin(alfa), -np.cos(alfa)*np.sin(delta)],
         [np.sin(alfa)*np.cos(delta), np.cos(alfa), -np.sin(alfa)*np.sin(delta)],
         [np.sin(alfa), 0 , np.cos(delta)]
        ]
    
    Vx, Vy, Vz = np.dot(A, np.array([vRad, vAlfa, vDelta]))
    return Vx, Vy, Vz

def ekv2gal(Vx, Vy, Vz):
    
    B = [[np.cos(alfaOm)*np.cos(lOm) + np.cos(inklinacija)*np.sin(alfaOm)*np.sin(lOm), np.sin(alfaOm)*np.cos(lOm) - np.cos(inklinacija)*np.cos(alfaOm)*np.sin(lOm), -np.sin(inklinacija)*np.sin(lOm)],
         [np.cos(alfaOm)*np.sin(lOm) - np.cos(inklinacija)*np.sin(alfaOm)*np.cos(lOm), np.sin(alfaOm)*np.sin(lOm) + np.cos(inklinacija)*np.cos(alfaOm)*np.cos(lOm),  np.sin(inklinacija)*np.cos(lOm)],
         [np.sin(inklinacija)*np.sin(alfaOm), -np.sin(inklinacija)*np.cos(alfaOm), np.cos(inklinacija)]
        ]
    
    u, v, w = np.dot(B, [Vx, Vy, Vz])
    return u,v,w

###

def izracunajLongituduUzlaznogCvora(A1, A2):  
    lOmega = np.arctan2(A2, A1)  
    return lOmega
    
def izracunajInklinaciju(A1, A2):
    inklinacija = np.sqrt(A1**2 + A2**2)
    inklinacija = np.arctan(inklinacija)
    return inklinacija

def jnaGalEkv(inklinacija, alfa, longCvora):
    delta = np.arctan(np.tan(inklinacija)*np.sin(alfa-longCvora))
    return delta
  
def deg2decDeg(deg, minut, sec):
    if deg > 0:
        return deg + minut/60 + sec/3600
    else:
        return deg - minut/60 - sec/3600

###

def ukupna_magnituda(magnitude):
    # const c
    c = 2.51188643150958
    magnituda_ukupna = np.sum(magnitude)
    magnituda_grupe = magnituda_ukupna - 2.5*np.log(np.sum(c**(magnituda_ukupna - magnitude)))
    return magnituda_grupe

###

def astroTriedar2ekv(vR, vAlfa, vDelta, alfa, delta):
    R = [[np.cos(alfa)*np.cos(delta), -np.sin(alfa), -np.cos(alfa)*np.sin(delta)],
         [np.sin(alfa)*np.cos(delta), np.cos(alfa), -np.sin(alfa)*np.sin(delta)],
         [np.sin(delta), 0, np.cos(alfa)]
        ]
    Vx, Vy, Vz = np.dot(R, [vR, vAlfa, vDelta])

    return Vx, Vy, Vz


def ekv2astroTriedar(Vx, Vy, Vz, alfa, delta):
    R1 = [ [np.cos(alfa)*np.cos(delta),  np.sin(alfa)*np.cos(delta),  np.sin(delta)],
           [-np.sin(alfa), np.cos(alfa),  0],
           [-np.cos(alfa)*np.sin(delta), -np.sin(alfa)*np.sin(delta), np.cos(delta)]
         ]
    vR, vAlfa, vDelta = np.dot(R1, [ Vx, Vy, Vz])

    return vR, vAlfa, vDelta
