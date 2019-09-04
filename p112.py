
def isbouncy(n):
    num = [int(i) for i in list(str(n))]
    if num==sorted(num):
        return False
    if num[::-1]==sorted(num):
        return False
    return True

bn = 0
f = False
i = 0
while not f:
    i += 1
    bn += 1 if isbouncy(i) else 0
    prop = bn/i*100
    if prop >= 98.99:
        f = True

print(i)

