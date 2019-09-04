
def revadd(n):
    r = list(str(n))
    r.reverse()
    return n+int(''.join(r))

def ispalin(n):
    return str(n)==str(n)[::-1]

def lychrel(n):
    for i in range(50):
        n = revadd(n)
        if ispalin(n):
            return False
    return True

print(sum(1 for i in range(10000) if lychrel(i)))

