
def digitsum(n):
    return sum(int(i) for i in str(n))

nums = []
for i in range(2,201):
    for j in range(2,201):
        if digitsum(i**j)==i:
            print(i, i**j)
            nums.append(i**j)

nums.sort()

