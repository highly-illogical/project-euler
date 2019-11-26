
from math import sqrt

def isnugget(n):
    k = 5*n**2+2*n+1
    if int(sqrt(k))**2==k:
        return True
    return False

nug = 10803704
i = 9

while i < 15:
    start = int(nug*6.854)
    end = int(nug*6.855)
    for k in range(start, end):
        if isnugget(k):
            nug = k
            i += 1
            print(i, nug)
            break
			
