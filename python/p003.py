
n = 600851475143
factors = []

i=2
while i<n+1:
    if n%i==0:
        n /= i
        factors.append(i)
    else:
        i += 1

print(factors[-1])

