
from itertools import permutations as p

primes = {2:2, 3:3, 4:5, 5:7, 6:11, 7:13, 8:17}

a = list(p('1234567890'))

s = 0
for num in a:
    n = ''.join(num)
    f = True
    if n[0]=='0': f = False
    for i in range(2,9):
        d = int(n[i-1:i+2])
        if d%primes[i]:
            f = False
    if f:
        s += int(n)

print(s)

