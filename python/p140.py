
from math import sqrt

def isnugget(n):
    k = 5*n**2+14*n+1
    if int(sqrt(k))**2==k:
        return True
    return False

s = 0
j = 0
for i in range(1, 10**6+1):
    if isnugget(i):
        j += 1
        s += i
        print(j, i)

nug = 656357
i = 14

while i < 30:
    start = int(nug*1.93874) if i%2 else int(nug*3.5353)
    end = int(nug*1.93876) if i%2 else int(nug*3.5354)
    for k in range(start, end):
        if isnugget(k):
            nug = k
            i += 1
            s += nug
            print(i, nug)
            break

print(s)

