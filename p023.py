
from math import sqrt

def divisorsum(n):
    s = 0
    for k in range(1,int(sqrt(n))+1):
        if not n%k:
            s += k
            s += n//k if k**2!=n else 0
    return s-n

def abundant(n):
    return divisorsum(n)>n

abuns = [i for i in range(1,28124) if abundant(i)]

def abunsum(n):
    for i in abuns:
        if i >= n//2+1:
            break
        if abundant(n-i):
            return True
    return False

s = 0
for i in range(1,28124):
    s += i if not abunsum(i) else 0
print(s)

