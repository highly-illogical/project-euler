
def identity(a,b):
     return str(a)+str(b)+str(a*b)

def ispan(s):
    return ''.join(sorted(list(s)))=='123456789'

prods = []
for i in range(10000):
    r = 100 if i<1000 else 10
    for j in range(r):
        m = identity(i,j)
        if ispan(m):
            if i*j not in prods:
                prods.append(i*j)

print(prods, sum(prods))

