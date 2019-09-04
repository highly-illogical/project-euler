
from math import sqrt

lim = 10**12*(10**12-1)//2

lower = 10**11
upper = 10**12

f = False
while not f:
    mid = (lower+upper)//2
    if mid*(mid-1) < lim:
        lower = mid
    if mid*(mid-1) > lim:
        upper = mid
    #print(lower,upper)
    if lower==upper:
        break
    if mid*(mid-1) > lim and (mid-1)*(mid-2) <= lim:
        f = True
        print(mid)

def findnext(lower,upper):
    f = False
    i = lower-1
    while not f and i<=upper:
        i += 1
        a = 8*i**2-8*i+1
        q = round(sqrt(a))
        if q**2==a and a%2:
            f = True
            print(i, q)
    return i,q

lower,upper = 3,7
oldi, oldq = 1,1
while oldi<mid:
    i, q = findnext(lower,upper)
    lower = round(i*(i/oldi))
    upper = round(i*(q/oldq))
    oldi,oldq = i,q

print(oldi)

