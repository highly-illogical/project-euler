
from math import sqrt

def isprime(n):
    i = 1
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        while i < int(sqrt(n))+1:
            i = i+1
            if n%i == 0:
                return False
    return True

def sieve(n):
    a = []
    for i in range(n):
        if isprime(i):
            a.append(i)
    return a

def rem(n, primes):
    return ((primes[n-1]-1)**n+(primes[n-1]+1)**n)%primes[n-1]**2

def rem2(n, primes):
    return 2*n*primes[n-1] % primes[n-1]**2

p = sieve(10**6)

for i in range(len(p)):
    if rem2(i, p) > 10**10 and i%2:
        print(i, p[i-1])
        break

