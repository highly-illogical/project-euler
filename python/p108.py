
#again guesswork

def nsols(n):
    s = 0
    for i in range(n+1, 2*n+1):
        num = i-n
        den = i*n
        if den%num == 0:
            s += 1
    return s

m = 0
for i in range(2*10**5):
    if nsols(i) > m:
        m = nsols(i)
        print(i, m)

