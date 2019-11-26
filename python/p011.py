
f = open('p011.txt','r')

a = []

for line in f:
    s = line.split()
    a.append([int(i) for i in s])

prod = 1

for i in range(20):
    for j in range(20):
        prodh = a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3] if j<17 else 0
        if prodh > prod:
            prod = prodh
        prodv = a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j] if i<17 else 0
        if prodv > prod:
            prod = prodv
        prodd1 = a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3] \
                 if i<17 and j<17 else 0
        if prodd1 > prod:
            prod = prodd1
        prodd2 = a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3] \
                 if i>2 and j<17 else 0
        if prodd2 > prod:
            prod = prodd2

print(prod)

