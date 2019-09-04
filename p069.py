
def divisors(n):
    div = []
    i = 2
    while i<n+1:
        if n%i==0:
            n //= i
            if i not in div: div.append(i)
        else:
            i += 1
    return div

def phi(n):
    rp = n-1
    d = divisors(n)
    for i in range(len(d)):
        j = 1
        while j<n//d[i]:
            elimed = d[:i]
            elim = False
            for e in elimed:
                if j%e==0:
                    elim = True
            if not elim:
                rp -= 1
            j += 1
    return rp

primes = [2,3,5,7,11,13,17,19]

j = 1
i = 0
while j<10**6:
    j *= primes[i]
    print(j, j/phi(j))
    i += 1
	
