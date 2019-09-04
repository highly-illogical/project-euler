def R(i, k):
    if i < k:
        return 0
    return RL[i-1] + GL[i-k]

def G(i, k):
    if i < k:
        return 1
    return RL[i-1] + GL[i-1]

def F(n, m):
    return G(n+1, m)

RL = []
GL = []
k = 50

for i in range(500):
    RL.append(R(i, k))
    GL.append(G(i, k))
    if G(i, k) > 10**6:
        print(i-1)
        break