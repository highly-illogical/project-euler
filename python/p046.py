
from math import sqrt

def isprime(k):
    if k<2: return False
    for i in range(2,int(sqrt(k)+1)):
        if k%i==0: return False
    return True

f = False
i = 2
while not f:
    if not isprime(i) and i%2:
        w = False
        for j in range(1,int(sqrt(i))+2):
            if isprime(i-2*j**2):
                w = True
                break
        if not w:
            print(i)
            f = True
    i += 1

