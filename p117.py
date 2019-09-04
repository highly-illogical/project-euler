
def N(i):
    if i < 1:
        return 0
    if i == 1:
        return 1
    return NL[i-1] + NL[i-2] + NL[i-3] + NL[i-4]

NL = [0, 1, 1, 2]

for i in range(4, 100):
    NL.append(N(i))

print(NL[51])

