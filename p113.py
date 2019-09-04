
from math import factorial

def C(n, r):
    return factorial(n)//factorial(r)//factorial(n-r)

print(sum(C(i, 9)+C(i-1, 8) for i in range(10, 110))-1000)
