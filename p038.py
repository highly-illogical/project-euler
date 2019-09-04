
def concat(n):
    c = []
    m = 0
    while len(c)<9:
        m += 1
        mul = n*m
        for k in str(mul): c.append(k)
    return ''.join(c)

def ispandigital(s):
    t = list(str(s))
    if ''.join(sorted(t))=='123456789':
        return True
    return False

maxp = 0

for i in range(10000):
    d = concat(i)
    if ispandigital(d):
        print(i, d)
        if int(d) > maxp:
            maxp = int(d)

print(maxp)

