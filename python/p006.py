
s = 0
ssq = 0

for i in range(1,101):
    ssq += i**2
    s += i

print(s**2 - ssq)

