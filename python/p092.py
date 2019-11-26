
def arriveat89(n):
    k = n
    while k!=1 and k!=89:
        k = sum(int(i)**2 for i in str(k))
    return k==89

print(sum(1 for i in range(1,10000001) if arriveat89(i)))

