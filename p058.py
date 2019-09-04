
from math import sqrt

def isprime(k):
    for i in range(2,int(sqrt(k)+1)):
        if k%i==0: return False
    return True

i = 1
diags = [1]
n,d = 0,1
side = 1

while (not n) or n/d >= 0.1:
    side = i*2+1
    for j in range(4):
        a = side**2-(side-1)*(3-j)
        diags.append(a)
        d += 1
        if isprime(a): n += 1
    i += 1

print(side)

