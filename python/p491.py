
from itertools import combinations as cmb
from math import factorial

c = cmb(list(range(10))*2, 10)
c = filter(lambda x: (90-2*sum(x))%11==0, c)
c = sorted([''.join(sorted([str(a) for a in i])) for i in c])
c = [c[0]] + [c[i] for i in range(1,len(c)) if c[i]!=c[i-1]]

def pairs(s):
    t = sorted(s)
    p = 0
    for i in range(len(t)):
        if t[i]==t[i-1]:
            p += 1
    return p

def zeroes(s):
    return sum(1 for i in s if int(i)==0)

d1 = [(len(i)-zeroes(i))*factorial(9)//2**pairs(i) for i in c]
d2 = [factorial(10)//2**pairs(i) for i in c]

d3 = [d1[i]*d2[i] for i in range(len(d1))]

print(sum(d3))
