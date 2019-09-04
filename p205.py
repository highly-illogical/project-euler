
from itertools import product

a = [1,2,3,4]
b = [1,2,3,4,5,6]

ap = sorted(list(map(sum, product(a,a,a,a,a,a,a,a,a))))
bp = sorted(list(map(sum, product(b,b,b,b,b,b))))

pete = [sum(map(lambda x: 1, (filter(lambda x: x==i+1, ap)))) \
        for i in range(36)]
colin = [sum(map(lambda x: 1, (filter(lambda x: x==i+1, bp)))) \
         for i in range(36)]

d = sum(colin)*sum(pete)
pete_wins = sum([sum(pete[i+1:])*colin[i]/d for i in range(36)])
print(pete_wins)

