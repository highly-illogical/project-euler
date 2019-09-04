
from math import sqrt

def sieve(n):
    i = 1
    primes = []
    while not len(primes) or primes[-1]<n:
        i += 1
        prime = True
        for p in primes:
            if i%p==0:
                prime = False
                break
        if prime: primes.append(i)
    return primes

primes = sieve(10**4)

def divisors(n):
    div = {}
    for p in primes:
        if p > int(sqrt(n))+1: break
        while n%p==0 and n>1:
            n //= p
            if p not in div:
                div[p] = 1
            else:
                div[p] += 1
        if n==1: break
    if n>1: div[n] = 1
    return div

def ndiv(n):
    d = list(divisors(n).values())
    prod = 1
    for v in d:
        prod *= v+1
    return prod

n = 0
for i in range(2,10**7):
    if ndiv(i)==ndiv(i+1):
        n += 1

print(n)

