
def nextp(t):
    s = t[:]
    permed = False
    i = 1
    while not permed:
        if i>=len(s):
            print("This is the last permutation.")
            break
        elif s[-i] > s[-i-1]:
            #marks first digit from right less than digit succeeding it
            to_perm = -i-1
            mi = -i
            #finds minimum digit in remaining list to right
            for j in range(1,i+1):
                if s[-j] > s[to_perm]:
                    if s[-j] < s[mi]:
                        mi = -j
            #swaps minimum and digit to permute
            k = s[to_perm]
            s[to_perm] = s[mi]
            s[mi] = k
            #sorts last i elements of list in ascending order
            sor = sorted(s[-i:])
            for j in range(1,i+1):
                s[-j] = sor[-j]
            permed = True
        i += 1
    return s

a = [[0], [0,1,2,3,4,5,6,7,8,9]]

while len(a)<=1000000:
    a.append(nextp(a[-1]))

print(a[-1])

