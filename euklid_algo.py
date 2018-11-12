import math
from random import *
import matplotlib as mlp
import matplotlib.pyplot as plt
import array as arr


def gcd_rek(a, b : int) -> int:
    if b == 0:
        return a
    c = a % b
    return gcd_rek(b, c)

def gcd_it(x, y: int) -> int:
    while(y):
      x, y = y, x % y
    return x

def gcd_steps(x,y: int) -> int:
    z = 0
    while(y):
        z += 1
        x, y = y, x%y
    return z

def gcd_mid_stp_num(anz, n: int) -> float:
    z = 0
    for i in range(anz):
        a = randint(0, n)
        b = randint(0, n)
        z += gcd_steps(a, b)
    return z/anz

def runtime(a, b: int) -> int:
    return log(a*b)**3

def calc_inv(a, b: int) -> int:
    if gcd_it(a, b) != 1:
        return -1



print("Der gcd(282, 240) rekursiv berechnet: " , gcd_rek(282, 240))
print("Der gcd(282, 240) iterativ berechnet: " , gcd_it(282, 240))
print("Der gcd(9**100 +1, 10**100 +1) iterativ berechnet: "
      , gcd_it(9**100 +1, 10**100 +1 ))
print("Die gcd_steps(9**100 +1, 10**100 +1) iterativ berechnet: "
      , gcd_steps(9**100 +1, 10**100 +1 ))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 9))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 99))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 999))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 9999))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 99999))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 999999))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 9999999))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 99999999))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 999999999))
print("Die mittlere gcd_steps bei Zahlen zwischen 0 und 9"
      , gcd_mid_stp_num(10000, 9999999999))

#anz ist die Anzahl der zufaelligen Ziehungen
#stellen ist die Anzahl der Dezimalstellen
def experiment(anz, stellen: int) -> arr.array('f'):
    y = arr.array('f', [])
    for i in range(1,stellen):
        y.append(gcd_mid_stp_num(anz, 10**i -1))
    return y    

y = experiment(1000, 10)
# Wertebereich für x-Achse festlegen:
x = [0, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

# Einzelne Diagramm-Linien plotten:
plt.plot(x, y, 'r--')

# Diagramm-Gitter einblenden:
plt.grid(True)

# Diagramm ausgeben:
plt.show()
