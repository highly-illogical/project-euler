
def pileswith(n, i):
    if n < i:
        return pileswith(n, i-1)
    elif n <= 0 or i <= 0:
        return 0
    elif n == 1 or i == 1:
        return 1
    else:
        s = pileswith(n, i-1)
        s += sum(pileswith(n-j, i-1) for j in range(i,n+1,i))
        if n%i==0:
            s += 1
        return s

print(pileswith(100,100)-1)

