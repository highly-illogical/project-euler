
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    while a%b:
        k = b
        b = a%b
        a = k
    return abs(b)

class Fraction:
    def __init__(self, n=0, d=1):
        self.n = n
        self.d = d

    def __str__(self):
        return str(int(self.n))+"/"+str(int(self.d))

    def __add__(self, other):
        f = Fraction()
        f.n = other.d*self.n + self.d*other.n
        f.d = other.d*self.d
        f.lowest()
        return f

    def lowest(self):
        k = gcd(self.n, self.d)
        if k != 0:
            self.n //= k
            self.d //= k

    def reciprocal(self):
        return Fraction(self.d, self.n)

def ndigits(n):
    return len(str(n))

def expand(n):
    if n == 0:
        return Fraction(1,1)
    else:
        w = Fraction(2,1)
        for i in range(n-1):
            w = Fraction(2, 1) + w.reciprocal()
        return Fraction(1,1) + w.reciprocal()

t = 0           
for i in range(1000):
    f = expand(i+1)
    if ndigits(f.n) > ndigits(f.d):
        t += 1

print(t)

