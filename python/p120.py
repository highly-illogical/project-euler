
def rmax(a):
    if a%2:
        return a**2 - a
    else:
        return a**2 - 2*a

print(sum(rmax(i) for i in range(3,1001)))

