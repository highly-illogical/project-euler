
def triangle(k): return k*(k+1)//2

def rects(m,n): return triangle(m)*triangle(n)

lim = 2*10**6
diff = 2*10**6
m,n = 0,0

i,j = 2001,1

while i>=j:
    while rects(i,j)>lim:
        i = i-1
        d = abs(lim-rects(i,j))
        if d < diff:
            diff = d
            m,n = i,j
    d = abs(lim-rects(i,j))
    if d < diff:
        diff = d
        m,n = i,j
    print(i,j)
    j = j+1
    
print(diff, m, n, m*n)

