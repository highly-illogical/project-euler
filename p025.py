
f1,f2 = 1,1

index = 2

while len(str(f2)) < 1000:
    f2 += f1
    f1 = f2-f1
    index += 1

print(f2, index)

