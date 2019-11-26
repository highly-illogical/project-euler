
'''
v --> row
|         1 black tile 2 black tiles 3 black tiles ...
| 1 tile
v 2 tiles
n 3 tiles
'''

def build(row, t):
    n = row//t
    v = [[] for i in range(n+1)]
    for i in range(n+1):
        for j in range(row+1):
            if i==0 or j==0:
                vij = 0
            elif j < t*i:
                vij = 0
            elif i==1:
                vij = j-t+1
            else:
                vij = sum(v[i-1][j-t-k] for k in range(j-t+1))
            v[i].append(vij)
    return v

r = build(50,2)
g = build(50,3)
b = build(50,4)
print(sum(k[-1] for k in b)+sum(k[-1] for k in g)+sum(k[-1] for k in r)) 

