
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

    def __eq__(self, other):
        self.lowest()
        other.lowest()
        return self.n==other.n and self.d==other.d

    def __lt__(self, other):
        return self.n/self.d < other.n/other.d

    def lowest(self):
        k = gcd(self.n, self.d)
        if k != 0:
            self.n //= k
            self.d //= k

d = 10**6
fs = []
for i in range(d-100,d):
    m = int(i*3/7)
    low = m-7 if m-7 > 1 else 1
    high = m+1 if m+1 < i else i
    for j in range(low, high):
        f = Fraction(j,i)
        f.lowest()
        if f not in fs:
            fs.append(f)

fs.sort()
for i in range(10):
    print(fs[-i-1])

