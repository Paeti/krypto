import random
import math


def miller_rabin(n, it):
    if n != int(n) or n < 2:
            return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False

    if n==2 or n==3 or n==5 or n==7:
            return True
    for i in range(it):#number of trials
        a = random.randint(2, n - 2)
        if ist_zeuge(a, n):
            return False
    #print("uff")
    return True


def ist_zeuge(a, n):
    k = n - 1
    if pow(a, n - 1, n) != 1: # a**(n - 1) != 1 % n;  a**n - 1 % n != 1
        return True
    while True:
        k >>= 1
        #print("while, k = " + str(k))
        if k % 2 != 0:
            if pow(a, k, n) == 1 or pow(a, k, n) == n - 1:
            #print("ungerades k")
                return False
            return True
    #while k % 2 == 0:
        if pow(a,k, n) != 1:
            #print("!= 1 => " + str(pow(a, k, n)))
            if pow(a, k, n) == n - 1:
                return False
            else:
                return True
        #k >>= 1
    #print("a = " + str(a) + ", k = " + str(k))
    return False

def next_prime_mil_rab(n, it):
    if(n % 2 == 0):
        n += 1
    else:
        n += 2
    while True:
        pos_prim = miller_rabin(n, it)
        if(pos_prim == True):
            return n
        else:
            n += 2

def anz_zeugen(n):
    anz = 0
    for i in range(1, n - 1):
        if ist_zeuge(i, n) == True:
            anz += 1
        else:
            print(str(i) + " ist kein zeuge")
    return anz


def abstand_prim(anz, n, it):
    erg = 0
    for i in range(anz):
        m = random.randint(0, n)
        erg += next_prime_mil_rab(m, it) - m
        #print(next_prime_mil_rab(n, it))
    #print(erg)
    return erg / anz


#print(anz_zeugen(9))
#print(anz_zeugen(325))
#print(anz_zeugen(14))
#print(anz_zeugen(555))


#print(miller_rabin(13, 5))

#print(ist_zeuge(149, 555))
#print(miller_rabin(41, 15))
#print(miller_rabin(242454656665753, 300))
#print(miller_rabin(34, 5))

#print(next_prime(17,5))
#print(next_prime(32,5))
#print(next_prime(10**100, 10))

#print(ist_zeuge(54, 58))
#for i in range (1, 50):
    #print(str(i) + "    " + str(miller_rabin(i, 20)))

#print(miller_rabin(99054, 300))
print(next_prime_mil_rab(17, 5))
print(next_prime_mil_rab(32, 5))
print(next_prime_mil_rab(10**100, 10))


print(next_prime_mil_rab(89, 20))
print(abstand_prim(50, 250, 10))
