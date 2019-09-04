
from math import sqrt

def isprime(k):
    for i in range(2,int(sqrt(k)+1)):
        if k%i==0: return False
    return True

def sumprime(n):
    s=0
    for i in range(2,n):
        s += i if isprime(i) else 0
    return s

print(sumprime(2000000))

