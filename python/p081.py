
a = []

with open('p081_matrix.txt', 'r') as f:
    for line in f:
        k = line.split(',')
        a.append([int(i) for i in k])

for i in range(len(a)):
    for j in range(i,len(a)):
        if i==0 and j!=0:
            a[i][j] += a[i][j-1]
            if j!=i:
                a[j][i] += a[j-1][i]
        if i>0:
            a[i][j] += min(a[i-1][j], a[i][j-1])
            if j!=i:
                a[j][i] += min(a[j-1][i], a[j][i-1])

print(a[-1][-1])

f.close()

