
def coll_length(n):
    i = 1
    while n!=1:
        if n%2:
            n = 3*n+1
        else:
            n = n/2
        i += 1
    return i

maxnum = 1
maxlength = 1

for i in range(1,1000000):
    if coll_length(i) > maxlength:
        maxlength = coll_length(i)
        maxnum = i

print(maxnum, maxlength)

