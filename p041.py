
from itertools import permutations
from math import sqrt

def isprime(k):
    if k<2: return False
    for i in range(2,int(sqrt(k)+1)):
        if k%i==0: return False
    return True

def check(n):
    mp = 0
    p = list(permutations([i+1 for i in range(n)]))
    for perm in p:
        num = int(''.join([str(j) for j in perm]))
        if isprime(num):
            mp = num
    return mp

mprime = 0
for i in range(1,10):
    k = check(i)
    if k > mprime: mprime = k
print(mprime)

