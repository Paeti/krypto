#!/usr/bin/env python3
__author__      = "Patrick Reckeweg"
__copyright__   = ""

import math
from random import *
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

#anz ist die Anzahl der zufaelligen Ziehungen
#stellen ist die Anzahl der Dezimalstellen
def experiment(anz, stellen: int) -> arr.array('f'):
    y = arr.array('f', [])
    for i in range(1,stellen):
        y.append(gcd_mid_stp_num(anz, 10**i -1))
    return y

def experiment_stellen(anz, stellen: int) -> arr.array('f'):
    y = arr.array('f', [])
    for i in range(1,stellen):
        y.append(gcd_mid_stp_num_range(anz, 10**(i-1), 10**i -1))
    return y

#def egcd():

#def calc_inv(a, b: int) -> int:
#   if gcd_it(a, b) != 1:
# return -1
    
