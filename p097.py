
def double(n):
    return int(''.join(list(str(n*2))[-10:]))

n = 1
for i in range(7830457):
    if len(str(n))<10: n *= 2
    else: n = double(n)
print(int(''.join(list(str(28433*n+1))[-10:])))

