
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0: return False
    return True

coeffs = [(a,b) for a in range(-999,1000) for b in range(-1000,1001)]

def nprimes(t):
    np = 0
    i = 0
    comp = False
    while not comp:
        q = i**2+t[0]*i+t[1]
        if q < 2: break
        if isprime(q):
            np += 1
            i += 1
        else:
            comp = True
    return np

maxp = 0
tp = (1,1)

for t in coeffs:
    numprim = nprimes(t)
    if maxp < numprim:
        maxp = numprim
        tp = t

print(maxp, tp, tp[0]*tp[1])

