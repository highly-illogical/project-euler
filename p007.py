
def sieve(n):
    i = 1
    primes = []
    while len(primes)<n:
        i += 1
        prime = True
        for p in primes:
            if i%p==0:
                prime = False
                break
        if prime: primes.append(i)
    return primes[-1]

print(sieve(10001))

