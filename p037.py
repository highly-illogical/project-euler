
from math import sqrt

def isprime(k):
    if k<2: return False
    for i in range(2,int(sqrt(k)+1)):
        if k%i==0: return False
    return True

def truncatable(n):
    for i in range(len(str(n))):
        if not isprime(int(str(n)[:i+1])): return False
        if not isprime(int(str(n)[-i-1:])): return False
    return True

truncs = []
i=10
while len(truncs)<11:
    i+=1
    if truncatable(i): truncs.append(i)
print(truncs, sum(truncs))

