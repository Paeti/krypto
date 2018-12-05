#!/usr/bin/env python3
__author__      = "Patrick Reckeweg"
__copyright__   = ""

import matplotlib as mlp
import matplotlib.pyplot as plt
from random import *
import array as arr
import miller_rabbin as ml


def draw_experiment():
    x = arr.array('i', [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000])

    a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = [10**i for i in range (1,10)]



    plt.figure(2)
    plt.subplot(211)
    plt.plot(a, b, 'y--')
    #plt.xlim(1, 9)
    plt.ylim(0, 10**9)
    plt.grid(True)

    plt.subplot(212)
    plt.plot(a, b, 'y--')
    #plt.xlim(1, 9)
    plt.ylim(10**1, 10**9)
    plt.yscale("log")
    plt.grid(True)

    plt.show()
