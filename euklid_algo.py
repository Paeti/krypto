#!/usr/bin/env python3
__author__      = "Patrick Reckeweg"
__copyright__   = ""

import math
from random import *
import matplotlib as mlp
import matplotlib.pyplot as plt
import array as arr

def gcd_rek(a, b :int) -> int:
    return a if b == 0 else gcd_rek(b, a % b)

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
    return sum([gcd_steps(randint(0, n), randint(0, n)) for i in range(anz)]) / anz

def gcd_mid_stp_num_range(anz, m, n: int) -> float:
    return sum([gcd_steps(randint(m, n), randint(m, n)) for i in range(anz)]) / anz



def calc_inv(a, b: int) -> int:
    if gcd_it(a, b) != 1:
        return -1



print("Der gcd(282, 240) rekursiv berechnet: " , gcd_rek(282, 240))
print("Der gcd(282, 240) iterativ berechnet: " , gcd_it(282, 240))
print("Der gcd(9**100 +1, 10**100 +1) iterativ berechnet: "
      , gcd_it(9**100 +1, 10**100 +1 ))

#anz ist die Anzahl der zufaelligen Ziehungen
#stellen ist die Anzahl der Dezimalstellen
def experiment(anz, stellen: int) -> arr.array('f'):
    y = arr.array('f', [])
    for i in range(1,stellen):
        y.append(gcd_mid_stp_num(anz, 10**i -1))
    return y

y = experiment(1000, 10)

# Wertebereich für x-Achse festlegen:
x = arr.array('i', [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000])

print(x)
print(y)

def experiment_stellen(anz, stellen: int) -> arr.array('f'):
    y = arr.array('f', [])
    for i in range(1,stellen):
        y.append(gcd_mid_stp_num_range(anz, 10**(i-1), 10**i -1))
    return y

z = experiment_stellen(1000, 10)

print(x)
print(z)

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
b = [10**i for i in range (1,10)]

plt.subplot(211)
plt.plot(x, y, 'r--', x, z, 'g--')
plt.xlim([1, 10**9])
plt.ylim([0, 18])
plt.xscale("linear")
plt.grid(True)

plt.subplot(212)
plt.plot(x, y, 'r--', x, z, 'g--')
plt.xscale("log", nonposx = "clip")
plt.yscale("linear")
plt.xlim([10, 10**9])
plt.ylim([0, 18])
plt.grid(True)

plt.show()

plt.subplot(211)
plt.plot(a, b, 'y--')
plt.xlim(1, 9)
plt.ylim(0, 10**9)
plt.grid(True)

plt.subplot(212)
plt.plot(a, b, 'y--')
plt.xlim(1, 9)
plt.ylim(10**1, 10**9)
plt.yscale("log")
plt.grid(True)

plt.show()

