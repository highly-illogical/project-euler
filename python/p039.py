
def nsols(n):
    ns = 0
    for i in range(1,n//2+1):
        for j in range(1,n-i):
            k = n-i-j
            if i**2+j**2==k**2 or i**2+k**2==j**2 or j**2+k**2==i**2:
                ns += 1
    return ns//6

maxv = [0, 0]
for i in range(1, 1001):
    if nsols(i) > maxv[1]:
        maxv = [i, nsols(i)]

print(maxv)

