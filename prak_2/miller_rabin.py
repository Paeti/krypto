import random


import random

def is_Prime(n, it):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n) or n < 2:
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False

    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    #assert(2**s * d == n-1)

    #def trial_composite(a):
     #   if pow(a, d, n) == 1:
      #      return False
       # for i in range(s):
        #    if pow(a, 2**i * d, n) == n-1:
         #       return False
        #return True

    for i in range(it):#number of trials
        a = random.randrange(2, n)
        if trial_composite(a, d, n, s):
            return False

    return True

def trial_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True


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
        a = random.randrange(2, n - 1)
        if ist_zeuge(a, n):
            return False
    return True


def ist_zeuge(a, n):
    m = n - 1
    if pow(a, m, n) != 1:
        True

    while m % 2 == 0:
        m = m // 2
        if pow(a, m, n) == n - 1:
            print("bli" + str(a) + " " + str(m) + " " + str(n) + " " + str(pow(a, m, n)))
            return False
        if pow(a, m, n) != 1:
            print("bla" + str(a) + " " + str(m) + " " + str(n) + " " + str(pow(a, m, n)))
            return True
        #m = m // 2
    return False


def next_prime(n, it):
    if(n % 2 == 0):
        n += 1
    while True:
        pos_prim = is_Prime(n, it)
        if(pos_prim == True):
            return n
        else:
            n += 2


#def anz_zeugen(n):
 #   anz = 0
  #  for i in range(1, n - 1):
   #     if trial_composite(i, n - 1, ):


print(is_Prime(13, 2))
print(is_Prime(41, 3))
print(is_Prime(242454656665753, 300))

print(miller_rabin(13, 2))
print(miller_rabin(41, 3))
print(miller_rabin(242454656665753, 300))


print(next_prime(17,5))
print(next_prime(32,5))
print(next_prime(10**100, 10))

#for i in range(0, 50):
 #   print(str(i) + "   " + str(miller_rabin(i, i)))

#print(ist_zeuge(24, 29))
print(ist_zeuge(2, 10))
print(ist_zeuge(3, 10))
print(ist_zeuge(4, 10))
print(ist_zeuge(5, 10))
print(ist_zeuge(6, 10))
print(ist_zeuge(7, 10))
print(ist_zeuge(8, 10))
