
def diagonalsum(n):
    dsum = 0
    for i in range(1,n+1,2):
        if i==1:
            dsum += 1
        if i>1:
            dsum += 4*i**2-6*(i-1)
    return dsum

print(diagonalsum(1001))

