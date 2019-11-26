
def find_d(n):
    s = []
    i = 1
    while len(s)<n:
        for j in str(i): s.append(j)
        i += 1
    return int(s[n-1])

prod = 1
for i in range(7): prod *= find_d(10**i)
print(prod)

