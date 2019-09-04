
def isfifth(n):
    return sum(int(i)**5 for i in str(n))==n

s = 0
for i in range(2,999999): s+=i if isfifth(i) else 0
print(s)

