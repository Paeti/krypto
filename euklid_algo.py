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

def egcd_it(b, a: int) -> [int, int, int]:
    x0, x1, y0, y1 = 1, 0, 0, 1
    while(a):
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  [b, x0, y0]

def solve_equ(c, d, m: int) -> int:
    #gcd(c, m)
    #d%gcd != 0 return -1
    if (d%gcd_it(c, m)) != 0:
        return -1

    #egcd, x nehmen (d/gcd)*x = p, return p%m
    t = egcd_it(c, m)
    x = (t[1]*(d//t[0]))%m 
    return x
