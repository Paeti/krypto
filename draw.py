#!/usr/bin/env python3
__author__      = "Patrick Reckeweg"
__copyright__   = ""

import matplotlib as mlp
import matplotlib.pyplot as plt
import euklid_algo as euc
import array as arr

def output_examples():
    print("Der gcd(282, 240) rekursiv berechnet: " , euc.gcd_rek(282, 240))
    print("Der gcd(282, 240) iterativ berechnet: " , euc.gcd_it(282, 240))
    print("Der gcd(9**100 +1, 10**100 +1) iterativ berechnet: "
      , euc.gcd_it(9**100 +1, 10**100 +1 ))

def draw_experiment():
    x = arr.array('i', [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000])
    y = euc.experiment(1000, 10)
    z = euc.experiment_stellen(1000, 10)

    a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = [10**i for i in range (1,10)]

    plt.figure(1)
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


    plt.figure(2)
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

