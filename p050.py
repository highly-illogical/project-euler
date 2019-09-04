
from math import sqrt

def isprime(k):
    for i in range(2,int(sqrt(k)+1)):
        if k%i==0: return False
    return True

def sieve(n):
    i = 1
    primes = []
    while (primes[-183]<n//183 if len(primes)>=183 else True):
        i += 1
        prime = True
        for p in primes:
            if i%p==0:
                prime = False
                break
        if prime: primes.append(i)
    return primes

primes = sieve(1000000)

most = 0
prime = 0
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        s = sum(primes[i:j])
        if isprime(s) and s<1000000 and j-i>most:
            prime = s
            most = j-i

print(prime, most)

