
def commondigit(a,b):
    for i in str(a):
        if i in str(b):
            return i
    return None

fracs = [[n,d] for n in range(10,100) for d in range(10,100) if n<d \
         and commondigit(n,d) is not None and n%10 and d%10]

prod=[1,1]
for f in fracs:
    n,d = f[0],f[1]
    eq = False
    if n//10==d//10:
        n %= 10
        d %= 10
        eq = n/d == f[0]/f[1]
    if n%10==d%10:
        n //= 10
        d //= 10
        eq = n/d == f[0]/f[1]
    if n//10==d%10:
        n %= 10
        d //= 10
        eq = n/d == f[0]/f[1]
    if n%10==d//10:
        n //=10
        d %= 10
        eq = n/d == f[0]/f[1]
    if eq:
        prod[0] *= n
        prod[1] *= d

print(prod[0]//8, prod[1]//8)

