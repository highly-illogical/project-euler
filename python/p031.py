
c = {1:1, 2:2, 3:5, 4:10, 5:20, 6:50, 7:100, 8:200}

def coinsums(p, i):
    if p <= 0 or i <= 0:
        return 0
    elif i == 1:
        return 1
    elif p < c[i]:
        return coinsums(p, i-1)
    else:
        s = coinsums(p, i-1)
        s += sum(coinsums(p-j, i-1) for j in range(c[i], p+1, c[i]))
        if p%c[i]==0:
            s += 1
        return s

print(coinsums(200,8))

