
from functools import reduce

def sieve(n):
    a = [[1] for i in range(n+1)]
    p = 2
    while p < n:
        for i in range(p, n+1, p):
            a[i-1].append(p)
        p += 1
        while a[p-1]!=[1]:
            p += 1
    return a[:-1]

flist = sieve(10**5)

flist = [(reduce(lambda x,y: x*y, flist[i]), i+1) for i in range(len(flist))]
flist.sort()

n = 10**4
print(flist[n-1][1])

