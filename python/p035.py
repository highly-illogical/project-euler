
from math import sqrt

def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def circular(n):
    for i in range(len(str(n))):
        k = int(str(n)[i:]+str(n)[:i])
        if not isprime(k):
            return False
    return True

s = 0
for i in range(2,1000000):
    s += 1 if circular(i) else 0
print(s)

