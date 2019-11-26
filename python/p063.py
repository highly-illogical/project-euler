
n=0
for i in range(1,31):
    for j in range(1,10):
        n += 1 if len(str(j**i))==i else 0
print(n)

