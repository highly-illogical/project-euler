
from math import factorial

def isfsum(n):
    return sum(factorial(int(i)) for i in str(n))==n

s = 0
for i in range(10,2540160):
    s += i if isfsum(i) else 0
print(s)

