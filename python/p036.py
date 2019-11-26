
def base2(n):
    s = []
    while n:
        s.insert(0,str(n%2))
        n //= 2
    return ''.join(s)

def ispalin(n): return str(n)==str(n)[::-1]

print(sum(i for i in range(1000000) if ispalin(i) and ispalin(base2(i))))

