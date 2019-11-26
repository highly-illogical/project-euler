
def sieve(n):
    i = 1
    primes = []
    while (primes[-1]<n if len(primes) else True):
        i += 1
        prime = True
        for p in primes:
            if i%p==0:
                prime = False
                break
        if prime: primes.append(i)
    return primes[:-1]

primes = [i for i in sieve(10000) if i>999]

def is_perm(n1,n2):
    return sorted(list(str(n1)))==sorted(list(str(n2)))

for i in range(len(primes)):
    a = primes[i]
    for j in range(i+1,len(primes)):
        b = primes[j]
        if is_perm(a,b):
            c = b+(b-a)
            if c in primes and is_perm(b,c):
                print(a,b,c)

