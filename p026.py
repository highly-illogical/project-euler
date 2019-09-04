
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0: return False
    return True

primes = [i for i in range(7,1000) if isprime(i)]

def cycle(n):
    s = str(10**2000//n)
    f = False
    i = 1
    while not f:
        if s[:i]==s[i:2*i]:
            f = True
            break
        i += 1
    return s[:i]

d = 7
for p in primes:
    if len(cycle(p))>len(cycle(d)):
        d = p
print(d, cycle(d), len(cycle(d)))

