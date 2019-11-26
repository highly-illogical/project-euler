
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

def sum_digits(n):
    return sum(int(i) for i in str(n))

def repr_e(n):
    r = [2]
    for i in range(n):
        if i%3==0 or i%3==2:
            r.append(1)
        if i%3==1:
            r.append(2*(i+2)//3)
    return r

def expand_e(n):
    r = repr_e(n)
    if n == 0:
        return Fraction(r[0],1)
    else:
        w = Fraction(r[-1],1)
        for i in range(n-1):
            w = Fraction(r[-2-i], 1) + w.reciprocal()
        return Fraction(r[0],1) + w.reciprocal()

print(sum_digits(expand_e(99).n))

