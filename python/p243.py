
#basically guesswork

from math import sqrt

def sieve(n):
    primes = []
    pfs = []
    for i in range(2, n):
        j = 0
        num = i
        pfs.append([])
        while num > 1 and j < len(primes) and primes[j] <= sqrt(i)+1:
            if num%primes[j]==0:
                num //= primes[j]
                if len(pfs[i-2])==0 or pfs[i-2][-1]!=primes[j]:
                    pfs[i-2].append(primes[j])
            else:
                j += 1
        if num > 1:
            primes.append(num)
            pfs[i-2].append(num)
        if tot(i, pfs[i-2])/(i+1) < 18200/94744:
            print(i)
    return primes, pfs

def tot(n, pfs):
    t = n
    for p in pfs:
        t *= p-1
        t //= p
    return t

k = 30030

for i in range(1, 10**5):
    n = i*k
    pfs = []
    j = 2
    while n > 1:
        if n%j==0:
            n //= j
            if j not in pfs:
                pfs.append(j)
        else:
            j += 1
    n = i*k
    r = tot(n, pfs)/(n-1)
    if r < 0.17:
        print(n, r)

