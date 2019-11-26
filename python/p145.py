
def rev(n):
    if n>9 and n%10==0: return False
    s = n+int(str(n)[::-1])
    while s:
        if s%2==0: return False
        s //= 10
    return True

count = 0
for i in range(1,1000000000):
    count += 1 if rev(i) else 0
print(count)

