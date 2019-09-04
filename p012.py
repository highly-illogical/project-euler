
from math import sqrt

def triangle(n): return n*(n+1)//2

def ndivisors(n):
    factors = []
    for k in range(1,int(sqrt(n))+1):
        if not n%k:
            factors.append(k)
            factors.append(n//k) if k**2!=n else 0
    return len(factors)

i = 1
while True:
    if ndivisors(triangle(i))>500:
        print(triangle(i))
        break
    i += 1
	
