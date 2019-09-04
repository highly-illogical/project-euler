
def fact(n):
    return 1 if n<=1 else n*fact(n-1)

k = str(fact(100))
s = 0

for i in k:
    s += int(i)

print(s)

