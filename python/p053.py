
from math import factorial

def ncr(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

n = 0
for i in range(1,101):
    for j in range(1,i+1):
        if ncr(i,j) > 10**6:
            n += 1

print(n)

