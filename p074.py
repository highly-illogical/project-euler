
from math import factorial

def facsum(n): return sum(factorial(int(i)) for i in str(n))

def chain(n):
    c = [n]
    while len(c)<60:
        a = facsum(c[-1])
        if a in c: break
        else: c.append(a)
    return c

def is60(n): return len(chain(n))==60

n = 0
for i in range(1000000): n += 1 if is60(i) else 0
print(n)

